import re
import os
import pandas as pd
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu, SmoothingFunction

def tokenize_for_bleu_eval(code):
    code = code.replace('§',' ')
    code = re.sub(r'([^A-Za-z0-9_])', r' \1 ', code)
    code = re.sub(r'([a-z])([A-Z])', r'\1 \2', code)
    code = re.sub(r'\s+', ' ', code)
    code = code.replace('"', '`')
    code = code.replace('\'', '`')
    tokens = [t for t in code.split(' ') if t]

    return tokens
#计算生成代码x与参考代码y之间的bleu
def compute_bleu(pre_code,ref_code):
    refer_tokens_for_bleu = tokenize_for_bleu_eval(ref_code)
    pred_tokens_for_bleu = tokenize_for_bleu_eval(pre_code)
    sm = SmoothingFunction()
    ngram_weights = [0.25] * min(4, len(refer_tokens_for_bleu))
    bleu_score = sentence_bleu([refer_tokens_for_bleu], pred_tokens_for_bleu, weights=ngram_weights, smoothing_function=sm.method3)
    return bleu_score
def compute_bleu2(ref_list,pred_tokens_for_bleu):
    sm = SmoothingFunction()
    ngram_weights = [0.25] * 4
    bleu_score = sentence_bleu(ref_list, pred_tokens_for_bleu, weights=ngram_weights, smoothing_function=sm.method3)
    return bleu_score
#依照一系列reference计算生成代码x的BLEU(取平均)
def compute_bleus(pred,refers):
    sum = 0
    xx = 0
    for i in range(len(refers)):
        try:
            for fj in refers:
                sum += compute_bleu(pred,fj)
            #print('dd%s' % dd_bleu)
        except Exception as e:
            print(e)
            xx += 1
        print(xx)
        print('bleu:' + str(sum / (len(refers) - xx)))


