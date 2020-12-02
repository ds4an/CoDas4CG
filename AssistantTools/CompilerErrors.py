import re
import csv
import os
import pandas as pd
def tokenize_for_bleu_eval(code):
    code = re.sub(r'([^A-Za-z0-9_])', r' \1 ', code)
    code = re.sub(r'([a-z])([A-Z])', r'\1 \2', code)
    code = re.sub(r'\s+', ' ', code)
    code = code.replace('"', '`')
    code = code.replace('\'', '`')
    tokens = [t for t in code.split(' ') if t]

    return tokens






content = open('gencode/tree2tree/tree2treeR.txt', 'r', encoding='utf-8').read()
#content = open('gencode/tranx/tranxE.txt', 'r', encoding='utf-8').read()

#统计静态编译检测错误个数
#sid_list = re.findall(r'\*\*\*\*\*\*\*\*\*\*\*\*\* Module ([\d]*)\n',content)
#检测动态编译检测错误个数
sid_list = re.findall(r'File "\.\/pre\/([\d]*)\.py\"',content)
# sid_list = re.findall(r'File "\.\/py\/([\d]*)\.py\"',content)
print(sid_list)
sid_list = list(set(sid_list))
xx=[]
for i in range(14865,15164):
    if str(i) not in sid_list:
        print(i)
print(len(sid_list))
# print(1-len(sid_list)/300)
print(1-(len(sid_list))/300)

