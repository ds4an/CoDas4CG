import re
import os
import logging
import ast
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import astor

from lang.parse import tokenize_code, de_canonicalize_code


def tokenize_for_bleu_eval(code):
    code = re.sub(r'([^A-Za-z0-9_])', r' \1 ', code)
    code = re.sub(r'([a-z])([A-Z])', r'\1 \2', code)
    code = re.sub(r'\s+', ' ', code)
    code = code.replace('"', '`')
    code = code.replace('\'', '`')
    tokens = [t for t in code.split(' ') if t]

    return tokens


def evaluate_decode_result(data_entry,
                           result_id,
                           decode_cand,
                           out_dir):

    query_tokens = data_entry['query_tokens']
    str_map = data_entry['str_map']
    ref_code_raw = data_entry['code_raw']
    ref_code = data_entry['code']

    f = open(os.path.join(out_dir, 'exact_match.txt'), 'a')
    exact_match_ids = []
    f_decode = open(os.path.join(out_dir, 'decode_results.txt'), 'a')
    f_bleu_eval_ref = open(os.path.join(out_dir, 'ref.txt'), 'a')
    f_bleu_eval_hyp = open(os.path.join(out_dir, 'hyp.txt'), 'a')
    f_generated_code = open(os.path.join(out_dir, 'geneated_code.txt'), 'a')

    acc = 0.0
    error = 0.0
    refer_source = ''
    sm = SmoothingFunction()
    p_tree = ast.parse(ref_code)    
    for t in p_tree.body:
        refer_source =refer_source + astor.to_source(t)
    #print(refer_source)  
    #ref_ast_tree = ast.parse(ref_code).body[0]
    #refer_source = astor.to_source(ref_ast_tree).strip()
    refer_tokens = tokenize_code(refer_source)
    #print("hhhhh")
    #print(ref_ast_tree,refer_source,refer_tokens)
    cid, cand, ast_tree, code = decode_cand
    code = ''
    for c in ast_tree.children:
        code += astor.to_source(c).strip() +'\n'
    #code = astor.to_source(ast_tree).strip()

    try:
        predict_tokens = tokenize_code(code)
    except:
        error = 1.0
        logging.info('error in tokenizing [%s]', code)
        predict_tokens = []

    if refer_tokens == predict_tokens:
        acc += 1

        exact_match_ids.append(result_id)
        f.write('-' * 60 + '\n')
        f.write('example_id: {}\n'.format(result_id))
        f.write(code + '\n')
        f.write('-' * 60 + '\n')

    ref_code_for_bleu = ref_code_raw
    pred_code_for_bleu = de_canonicalize_code(code, ref_code_raw)
    for literal, place_holder in str_map.items():
        pred_code_for_bleu = pred_code_for_bleu.replace('\'' + place_holder + '\'', literal)

    # we apply Ling Wang's trick when evaluating BLEU scores
    refer_tokens_for_bleu = tokenize_for_bleu_eval(ref_code_for_bleu)
    pred_tokens_for_bleu = tokenize_for_bleu_eval(pred_code_for_bleu)

    shorter = len(pred_tokens_for_bleu) < len(refer_tokens_for_bleu)

    ngram_weights = [0.25] * min(4, len(refer_tokens_for_bleu))
    bleu = sentence_bleu([refer_tokens_for_bleu], pred_tokens_for_bleu, weights=ngram_weights, smoothing_function=sm.method3)

    f_decode.write('-' * 60 + '\n')
    f_decode.write('example_id: %d\n' % result_id)
    f_decode.write('intent: \n')
    f_decode.write(' '.join(query_tokens) + '\n')
    f_decode.write('canonicalized reference: \n')
    f_decode.write(refer_source + '\n')
    f_ref_source = open('py/ref/%s.py'% result_id,'w')
    f_ref_source.write(refer_source)
    f_decode.write('canonicalized prediction: \n')
    f_decode.write(code + '\n')
    f_code = open('py/pre/%s.py'% result_id,'w')
    f_code.write(code)
    f_decode.write('reference code for bleu calculation: \n')
    f_decode.write(ref_code_for_bleu + '\n')
    f_ref_code_for_bleu = open('py/ref_bleu/%s.py'% result_id,'w')
    f_ref_code_for_bleu.write(ref_code_for_bleu)
    f_decode.write('predicted code for bleu calculation: \n')
    f_decode.write(pred_code_for_bleu + '\n')
    f_pred_code_for_bleu= open('py/pre_bleu/%s.py'% result_id,'w')
    f_pred_code_for_bleu.write(pred_code_for_bleu)
    f_decode.write('pred_shorter_than_ref: %s\n' % shorter)
    f_decode.write('-' * 60 + '\n')

    # for Hiro's evaluation
    f_generated_code.write(pred_code_for_bleu.replace('\n', '#NEWLINE#') + '\n')
    f_ref_source.close()
    f_code.close()
    f_ref_code_for_bleu.close()
    f_pred_code_for_bleu.close()
    f.close()
    f_decode.close()
    f_bleu_eval_ref.close()
    f_bleu_eval_hyp.close()
    f_generated_code.close()

    return bleu, acc, error

