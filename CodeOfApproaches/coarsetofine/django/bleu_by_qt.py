import re
import os
import pandas as pd
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu, SmoothingFunction

def tokenize_for_bleu_eval(code):
    code = re.sub(r'([^A-Za-z0-9_])', r' \1 ', code)
    code = re.sub(r'([a-z])([A-Z])', r'\1 \2', code)
    code = re.sub(r'\s+', ' ', code)
    code = code.replace('"', '`')
    code = code.replace('\'', '`')
    tokens = [t for t in code.split(' ') if t]

    return tokens

def compute_bleu(refer_tokens_for_bleu,pred_tokens_for_bleu):
    sm = SmoothingFunction()
    ngram_weights = [0.25] * min(4, len(refer_tokens_for_bleu))
    bleu_score = sentence_bleu([refer_tokens_for_bleu], pred_tokens_for_bleu, weights=ngram_weights, smoothing_function=sm.method3)

    return bleu_score
if __name__ == "__main__":
    sum = 0
    file1 = pd.read_csv('./one.csv')
    flist = [(a, b) for (a, b) in zip(file1['pid'], file1['sid'])]
    file2 = pd.read_excel('./eval.xlsx')
    flist2 = [(a, b) for (a, b) in zip(file2['pid'], file2['sid'])]
    for i in range(len(flist)):
        a_bleu = []
        try:
            for fj in flist2:
                # print(fi[0],fj[0])
                if str(flist[i][0])==str(fj[0]):
                    # print('!!!')
                    # print(fi[0],fi[1], fj[1])
                    # f_ref = open('./finaleval/py15/ref_bleu/%s.py' % (int(fj[1]-12425)), 'r')
                    # f_pre = open('./finaleval/py15/pre_bleu/%s.py' % (int(fi[1])-12425), 'r')
                    f_ref = open('./rebuttal/13py/ref_bleu/%s.py' % (int(fj[1])), 'r')
                    # f_pre = open('./rebuttal/30960py/pre_bleu/%s.py' % (i+14865), 'r')
                    f_pre = open('./rebuttal/13py/pre_bleu/%s.py' % (i), 'r')

                    ref_code = f_ref.read()
                    pre_code = f_pre.read()
                    f_ref.close()
                    f_pre.close()
                    # print(ref_code)
                    # print('--------------------')
                    # print(pre_code)
                    refer_tokens_for_bleu = tokenize_for_bleu_eval(ref_code)
                    pred_tokens_for_bleu = tokenize_for_bleu_eval(pre_code)
                    print(compute_bleu(refer_tokens_for_bleu,pred_tokens_for_bleu))
                    a_bleu.append(compute_bleu(refer_tokens_for_bleu,pred_tokens_for_bleu))
            max_bleu = max(a_bleu)

            print('max%s' % max_bleu)
            sum += max_bleu
        except Exception as e:
            print(e)
    print(len(flist),len(flist2))
    # print(sum/len(flist))
    print(sum/299)