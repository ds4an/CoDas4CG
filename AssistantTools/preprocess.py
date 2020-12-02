# coding=utf-8

from __future__ import print_function

import itertools
import re
import pickle
import ast
import inspect
import astor
import nltk
import sys
import codecs

import numpy as np

QUOTED_TOKEN_RE = re.compile(r"(?P<quote>''|[`'\"])(?P<string>.*?)(?P=quote)")


def compare_ast(node1, node2):
    if not isinstance(node1, str):
        if type(node1) is not type(node2):
            return False
    if isinstance(node1, ast.AST):
        for k, v in list(vars(node1).items()):
            if k in ('lineno', 'col_offset', 'ctx'):
                continue
            if not compare_ast(v, getattr(node2, k)):
                return False
        return True
    elif isinstance(node1, list):
        return all(itertools.starmap(compare_ast, zip(node1, node2)))
    else:
        return node1 == node2


def tokenize_intent(intent):
    lower_intent = intent.lower()
    tokens = nltk.word_tokenize(lower_intent)

    return tokens


def infer_slot_type(quote, value):
    if quote == '`' and value.isidentifier():
        return 'var'
    return 'str'


def canonicalize_intent(intent):
    # handle the following special case: quote is `''`
    marked_token_matches = QUOTED_TOKEN_RE.findall(intent)

    slot_map = dict()
    var_id = 0
    str_id = 0
    for match in marked_token_matches:
        quote = match[0]
        value = match[1]
        quoted_value = quote + value + quote

        # try:
        #     # if it's a number, then keep it and leave it to the copy mechanism
        #     float(value)
        #     intent = intent.replace(quoted_value, value)
        #     continue
        # except:
        #     pass

        slot_type = infer_slot_type(quote, value)

        if slot_type == 'var':
            slot_name = 'var_%d' % var_id
            var_id += 1
            slot_type = 'var'
        else:
            slot_name = 'str_%d' % str_id
            str_id += 1
            slot_type = 'str'

        # slot_id = len(slot_map)
        # slot_name = 'slot_%d' % slot_id
        # # make sure slot_name is also unicode
        # slot_name = unicode(slot_name)

        intent = intent.replace(quoted_value, slot_name)
        slot_map[slot_name] = {'value': value.strip().encode().decode('unicode_escape', 'ignore'),
                               'quote': quote,
                               'type': slot_type}

    return intent, slot_map


def replace_identifiers_in_ast(py_ast, identifier2slot):
    for node in ast.walk(py_ast):
        for k, v in list(vars(node).items()):
            if k in ('lineno', 'col_offset', 'ctx'):
                continue
            # Python 3
            # if isinstance(v, str) or isinstance(v, unicode):
            if isinstance(v, str):
                if v in identifier2slot:
                    slot_name = identifier2slot[v]
                    # Python 3
                    # if isinstance(slot_name, unicode):
                    #     try: slot_name = slot_name.encode('ascii')
                    #     except: pass

                    setattr(node, k, slot_name)


def is_enumerable_str(identifier_value):
    """
    Test if the quoted identifier value is a list
    """

    return len(identifier_value) > 2 and identifier_value[0] in ('{', '(', '[') and identifier_value[-1] in ('}', ']', ')')


def canonicalize_code(code, slot_map):
    string2slot = {x['value']: slot_name for slot_name, x in list(slot_map.items())}

    py_ast = ast.parse(code)
    replace_identifiers_in_ast(py_ast, string2slot)
    canonical_code = astor.to_source(py_ast).strip()

    # the following code handles the special case that
    # a list/dict/set mentioned in the intent, like
    # Intent: zip two lists `[1, 2]` and `[3, 4]` into a list of two tuples containing elements at the same index in each list
    # Code: zip([1, 2], [3, 4])

    entries_that_are_lists = [slot_name for slot_name, val in slot_map.items() if is_enumerable_str(val['value'])]
    if entries_that_are_lists:
        for slot_name in entries_that_are_lists:
            list_repr = slot_map[slot_name]['value']
            #if list_repr[0] == '[' and list_repr[-1] == ']':
            first_token = list_repr[0]  # e.g. `[`
            last_token = list_repr[-1]  # e.g., `]`
            fake_list = first_token + slot_name + last_token
            slot_map[fake_list] = slot_map[slot_name]
            # else:
            #     fake_list = slot_name

            canonical_code = canonical_code.replace(list_repr, fake_list)

    return canonical_code


def decanonicalize_code(code, slot_map):
    for slot_name, slot_val in slot_map.items():
        if is_enumerable_str(slot_name):
            code = code.replace(slot_name, slot_val['value'])

    slot2string = {x[0]: x[1]['value'] for x in list(slot_map.items())}
    py_ast = ast.parse(code)
    replace_identifiers_in_ast(py_ast, slot2string)
    raw_code = astor.to_source(py_ast).strip()
    # for slot_name, slot_info in slot_map.items():
    #     raw_code = raw_code.replace(slot_name, slot_info['value'])

    return raw_code

def codeReplaceText(requirments,implements):
    f = codecs.open("new.anno",'w','utf-8')
    count1=0
    count2=0
    for idx, (src_query, tgt_code) in enumerate(
            zip(codecs.open(requirments, 'r', 'utf-8'), codecs.open(implements, 'r', 'utf-8'))):
        args_list=[]
        src_query = src_query.strip()
        text = re.sub(r"can\'t", "can not", src_query)
        text = re.sub(r"cannot", "can not ", text)
        text = re.sub(r"\'ve ", " have ", text)
        text = re.sub(r"n\'t", " not ", text)
        text = re.sub(r"i\'m", "i am ", text)
        text = re.sub(r"what\'s", "what is ", text)
        text = re.sub(r"What\'s","What is",text)
        text = re.sub(r"\'re", " are ", text)
        text = re.sub(r"\'d", " would ", text)
        text = re.sub(r"\'s","",text)
        src_query = re.sub(r"\'ll", " will ", text)
        if idx < 14865:
            tgt_code = tgt_code.replace('!#$', '\n').strip()
            root = ast.parse(tgt_code)
            for node in ast.walk(root):
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                    #nodeId = node.id
                    args_list.append(node.id)
                    #args_list.append(nodeId.lower())
            args_list2 =list(set(args_list))
            if 'a' in args_list2:
                args_list2.remove('a')
            #num1=len(args_list2)
            #num2=0
            for word in args_list2:
                if word in src_query:
                    #print(word)
                    pattern = re.compile(r'\b(%s)\b'%word, re.I)
                    src_query = pattern.sub('`'+word+'`',src_query,count=1)
            '''num2=src_query.count('`')/2
            count1+=num1
            count2+=num2
            print(str(num1)+'  '+str(num2))'''
        src_query = src_query.replace('``','`')
        f.write(src_query)
        f.write('\n')
    f.close()
from nltk.corpus import stopwords,wordnet

from nltk.stem import WordNetLemmatizer
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None
wnl = WordNetLemmatizer()
#stop = set(stopwords.words('english'))
stop = ['a','an','the','is','are','this','that']
def finalProcess(implements):
    f = codecs.open("all_1.anno",'w','utf-8')
    for idx, (src_query, tgt_code) in enumerate(
            zip(codecs.open("newall21.anno", 'r', 'utf-8'), codecs.open(implements, 'r', 'utf-8'))):
        src_query = src_query.strip()
        text = src_query.lower()
        text = re.sub(r" e mail ", " email ", text)
        text = re.sub(r" e \- mail ", " email ", text)
        text = re.sub(r" e\-mail ", " email ", text)
        text = text.replace('_1s','_1').replace('_0s','_0').replace('str_',' str_')\
            .replace('var_',' var_').strip()
        token_s = nltk.word_tokenize(text)
        tagged_sent = nltk.pos_tag(token_s)
        tokens = []
        for tag in tagged_sent:
            wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
            tokens.append(wnl.lemmatize(tag[0], pos = wordnet_pos))
        words = []
        for token in tokens:
            i = token.find('.')
            if 0 < i < len(token) - 1:
                new_tokens = ['['] + token.replace('.', ' . ').split(' ') + [']']
                words.extend(new_tokens)
            if token not in stop:
                words.append(token)
        result = ' '.join(words)
        result = result.replace(' .','.').replace(' ?','?').replace(' !','!').replace(' ,',',').replace('`','')
        f.write(result)
        f.write('\n')
    f.close()
#同时处理需求和代码
def PreProcessALL(requirements, implements):
    codeReplaceText(requirements, implements)
    print('replace finished')
    f = codecs.open("newall21.anno",'w','utf-8')
    f1 = codecs.open("newall21.code",'w','utf-8')
    f2 = codecs.open("str_map",'w','utf-8')
    for idx, (src_query, tgt_code) in enumerate(
            zip(codecs.open("new.anno", 'r', 'utf-8'), codecs.open(implements, 'r', 'utf-8'))):
        # for idx, (src_query, tgt_code) in enumerate(zip(open(annot_file), open(code_file))):
        src_query = src_query.strip()

        tgt_code = tgt_code.replace('\n', 'nnnnnnnn')
        tgt_code = tgt_code.replace('!#$', '\n').strip()
        canonical_intent, slot_map = canonicalize_intent(src_query)
        canonical_snippet = canonicalize_code(tgt_code, slot_map)
        canonical_snippet_final = canonical_snippet.replace('\n','!#$').strip()
        canonical_snippet_final = canonical_snippet_final.replace('nnnnnnnn','\n').strip()
        f2.write(str(slot_map))
        f2.write('\n')
        f.write(canonical_intent)
        f.write('\n')
        f1.write(canonical_snippet_final)
        f1.write('\n')

    f.close()
    f1.close()
    f2.close()
    print('var and str finished.')
    finalProcess("newall21.code")
    print('final done!')
#处理文本
def PreProcessReq(requirements, implements):
    codeReplaceText(requirements, implements)
    print('replace finished')
    f = codecs.open("newall21.anno",'w','utf-8')
    for idx, (src_query, tgt_code) in enumerate(
            zip(codecs.open("new.anno", 'r', 'utf-8'), codecs.open(implements, 'r', 'utf-8'))):
        # for idx, (src_query, tgt_code) in enumerate(zip(open(annot_file), open(code_file))):
        src_query = src_query.strip()

        tgt_code = tgt_code.replace('\n', 'nnnnnnnn')
        tgt_code = tgt_code.replace('!#$', '\n').strip()
        canonical_intent, slot_map = canonicalize_intent(src_query)
        canonical_snippet = canonicalize_code(tgt_code, slot_map)
        canonical_snippet_final = canonical_snippet.replace('\n','!#$').strip()
        canonical_snippet_final = canonical_snippet_final.replace('nnnnnnnn','\n').strip()
        f.write(canonical_intent)
        f.write('\n')
    f.close()
    print('var and str finished.')
    finalProcess(implements)
    print('final done!')
#处理代码
def PreProcessImp(requirements, implements):
    codeReplaceText(requirements, implements)
    print('replace finished')
    f1 = codecs.open("newall21.code",'w','utf-8')
    for idx, (src_query, tgt_code) in enumerate(
            zip(codecs.open("new.anno", 'r', 'utf-8'), codecs.open(implements, 'r', 'utf-8'))):
        src_query = src_query.strip()
        tgt_code = tgt_code.replace('\n', 'nnnnnnnn')
        tgt_code = tgt_code.replace('!#$', '\n').strip()
        canonical_intent, slot_map = canonicalize_intent(src_query)
        canonical_snippet = canonicalize_code(tgt_code, slot_map)
        canonical_snippet_final = canonical_snippet.replace('\n','!#$').strip()
        canonical_snippet_final = canonical_snippet_final.replace('nnnnnnnn','\n').strip()

        f1.write(canonical_snippet_final)
        f1.write('\n')
    f1.close()
    print('finished.')