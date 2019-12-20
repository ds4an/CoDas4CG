import os
import platform
import torch
import astor
import nltk

from natural_lang.vocab import Vocab
from utils.io import *
from lang.unaryclosure import apply_unary_closures, get_top_unary_closures
from lang.parse import *


base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
lib_dir = os.path.join(base_dir, 'lib')
data_dir = os.path.join(base_dir, 'data')

system = 'w' if platform.system() == 'Windows' else 'nw'

delimiter = ';' if system == 'w' else ':'

classpath = delimiter.join([
        lib_dir,
        os.path.join(lib_dir, 'stanford-parser/stanford-parser.jar'),
        os.path.join(lib_dir, 'stanford-parser/stanford-parser-3.5.1-models.jar'),
        os.path.join(lib_dir, 'easyccg/easyccg.jar')])


def make_dirs(dirs):
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)


def build_vocab_from_token_files(filepaths, lower=False, min_frequency=1):
    freq_dict = {}
    logging.info('Building vocabulary from token files...')
    for filepath in tqdm(filepaths):
        with open(filepath) as f:
            for line in f:
                if lower:
                    line = line.lower()
                for item in line.split():
                    if item in freq_dict:
                        freq_dict[item] += 1
                    else:
                        freq_dict[item] = 1
    vocab = {k for k, v in freq_dict.items() if v >= min_frequency}
    logging.debug('Total items: {}, with min frequency: {}.'.format(len(freq_dict), len(vocab)))
    return vocab


def build_vocab_from_items(items, lower=False, min_frequency=1):
    freq_dict = {}
    logging.info('Building vocabulary from items...')
    for item in tqdm(items):
        if lower:
            item = item.lower()
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    vocab = {k for k, v in freq_dict.items() if v >= min_frequency}
    logging.debug('Total items: {}, with min frequency: {}.'.format(len(freq_dict), len(vocab)))
    return vocab


def save_vocab(destination, vocab):
    logging.info('Writing vocabulary: ' + destination)
    with open(destination, 'w', encoding='utf-8') as f:
        for w in tqdm(sorted(vocab)):
            f.write(w + '\n')


def tokenize(filein, fileout):
    logging.info('Tokenizing ' + filein)
    cmd = ('java -cp %s Tokenize -tokpath %s < %s'
           % (classpath, fileout, filein))
    os.system(cmd)


def tokenize_with_str_map(filein, fileout, filestrmap):
    logging.info('Tokenizing with strmap ' + filein)
    with open(filein, 'r') as f:
        t_n_str = map(tokenize_and_strmap_query, f.readlines())
        tokens, str_maps = tuple(zip(*t_n_str))
    with open(fileout, 'w') as f:
        f.writelines([' '.join(t) + '\n' for t in tokens])
    serialize_to_file(str_maps, filestrmap)



def dependency_parse(filepath):
    logging.info('Dependency parsing ' + filepath)
    dirpath = os.path.dirname(filepath)
    filepre = os.path.splitext(os.path.basename(filepath))[0]
    parentpath = os.path.join(dirpath, filepre + '.dependency_parents')
    relpath = os.path.join(dirpath, filepre + '.dependency_rels')
    cmd = ('java -cp %s DependencyParse -parentpath %s -relpath %s < %s'
        % (classpath, parentpath, relpath, filepath))
    os.system(cmd)


def constituency_parse(filepath):
    logging.info('Constituency parsing ' + filepath)
    dirpath = os.path.dirname(filepath)
    filepre = os.path.splitext(os.path.basename(filepath))[0]
    parentpath = os.path.join(dirpath, filepre + '.constituency_parents')
    catpath = os.path.join(dirpath, filepre + '.constituency_categories')
    cmd = ('java -cp {} ConstituencyParse -parentpath {} -catpath {} < {}'.format
        (classpath, parentpath, catpath, filepath))
    os.system(cmd)


def ccg_parse(filepath):
    logging.info('CCG parsing ' + filepath)
    dirpath = os.path.dirname(filepath)
    filepre = os.path.splitext(os.path.basename(filepath))[0]
    parentpath = os.path.join(dirpath, filepre + '.ccg_parents')
    catpath = os.path.join(dirpath, filepre + '.ccg_categories')
    cmd = ('java -Xmx40960M -cp {} CCGParse -parentpath {} -catpath {} -modelpath '
           'lib/easyccg/model < {}'.format(classpath, parentpath, catpath, filepath))
    os.system(cmd)


def parse(filepath):
    #dependency_parse(filepath)
    #constituency_parse(filepath)
    #ccg_parse(filepath)
    print('skip')


# loading GLOVE word vectors
# if .pth file is found, will load that
# else will load from .txt file & save
def load_word_vectors(path):
    if os.path.isfile(path+'.pth') and os.path.isfile(path+'.vocab'):
        logging.info('Glove file found, loading to memory...')
        vectors = torch.load(path+'.pth')
        vocab = Vocab(filename=path+'.vocab')
        return vocab, vectors
    # saved file not found, read from txt file
    # and create tensors for word vectors
    logging.info('Glove file not found, preparing, be patient...')
    count = sum(1 for line in open(path+'.txt'))
    with open(path+'.txt', 'r') as f:
        contents = f.readline().rstrip('\n').split(' ')
        dim = len(contents[1:])
    words = [None]*(count)
    vectors = torch.zeros(count,dim)
    with open(path+'.txt','r') as f:
        idx = 0
        for line in f:
            contents = line.rstrip('\n').split(' ')
            words[idx] = contents[0]
            vectors[idx] = torch.Tensor(list(map(float, contents[1:])))
            idx += 1
    with open(path+'.vocab', 'w') as f:
        for word in words:
            f.write(word+'\n')
    vocab = Vocab(filename=path+'.vocab')
    torch.save(vectors, path+'.pth')
    return vocab, vectors


def parse_code_trees(code_file, strmap_file, code_out_file, raw_code_out_file, lb='§'):
    logging.info('Parsing code trees from file {}'.format(code_file))
    strmaps = deserialize_from_file(strmap_file)

    parse_trees = []
    raw_codes = []
    codes = []
    for line, str_map in tqdm(zip(open(code_file).readlines(), strmaps)):
        line = line.strip().replace('    ', '\t')
        print(lb)
        if lb is not None:
            line = line.replace(lb, '\n')
        code = line

        raw_code = code
        raw_codes.append(raw_code)

        code = canonicalize_code(code)
        for str_literal, str_repr in str_map.items():
            code = code.replace(str_literal, '\'' + str_repr + '\'')

        codes.append(code)

        try:
            #print(code)
            p_tree = parse_raw(code)
            # sanity check
            #print(p_tree)
            node_type = p_tree.type
            node_label = p_tree.label
            pred_code = ''
            # remove root
            if node_type == 'root':
                for t in p_tree.children:
                    pred_ast = parse_tree_to_python_ast(t)
                    pred_code =pred_code + astor.to_source(pred_ast)
           # print(pred_code)        
           # pred_ast = parse_tree_to_python_ast(p_tree)
           # for pa in pred_ast:
            #    pred_code = astor.to_source(pred_ast)
              #  print(pred_code)
            print("------------------------------------------------")
            ref_ast = ast.parse(code)
            print(code)
            ref_code = astor.to_source(ref_ast)
            print(ref_code)

            #if pred_code != ref_code:
             #   raise RuntimeError('code mismatch!')

            parse_trees.append(p_tree)
        except RuntimeError as e:
            print(e)
            parse_trees.append(None)

    serialize_to_file(codes, code_out_file)
    serialize_to_file(raw_codes, raw_code_out_file)
    return parse_trees


def write_grammar(parse_trees, out_file):
    grammar = get_grammar(parse_trees)

    serialize_to_file(grammar, out_file + '.bin')
    with open(out_file, 'w') as f:
        for rule in tqdm(grammar):
            str = rule.__repr__()
            f.write(str + '\n')

    return grammar


def write_terminal_tokens_vocab(grammar, parse_trees, out_file, min_freq=2):
    terminal_token_seq = []

    for parse_tree in tqdm(parse_trees):
        if parse_tree is None: continue
        for node in parse_tree.get_leaves():
            if grammar.is_value_node(node):
                terminal_val = node.value
                terminal_str = str(terminal_val)

                terminal_tokens = get_terminal_tokens(terminal_str)

                for terminal_token in terminal_tokens:
                    terminal_token_seq.append(terminal_token)

    terminal_vocab = build_vocab_from_items(terminal_token_seq, False, min_freq)
    save_vocab(out_file, terminal_vocab)


def do_unary_closures(parse_trees, k):
    logging.info('Applying unary closures to parse trees...')
    unary_closures = get_top_unary_closures(parse_trees, k=k)
    for parse_tree in tqdm(parse_trees):
        if parse_tree is None: continue
        apply_unary_closures(parse_tree, unary_closures)


def write_trees(parse_trees, out_file):
    # save data
    with open(out_file, 'w') as f:
        for tree in tqdm(parse_trees):
            f.write(tree.__repr__() + '\n')
    serialize_to_file(parse_trees, out_file + '.bin')


QUOTED_STRING_RE = re.compile(r"(?P<quote>['\"])(?P<string>.*?)(?<!\\)(?P=quote)")
def tokenize_and_strmap_query(query):
    """
    replace strings in query to a special place holder
    """
    str_count = 0
    str_map = dict()

    matches = QUOTED_STRING_RE.findall(query)
    # de-duplicate
    cur_replaced_strs = set()
    for match in matches:
        # If one or more groups are present in the pattern,
        # it returns a list of groups
        quote = match[0]
        str_literal = quote + match[1] + quote

        if str_literal in cur_replaced_strs:
            continue

        # FIXME: substitute the ' % s ' with
        if str_literal in ['\'%s\'', '\"%s\"']:
            continue

        str_repr = '_STR_%d_' % str_count
        str_map[str_literal] = str_repr

        query = query.replace(str_literal, str_repr)

        str_count += 1
        cur_replaced_strs.add(str_literal)

    # tokenize
    query_tokens = nltk.word_tokenize(query)

    new_query_tokens = []
    # break up function calls like foo.bar.func
    for token in query_tokens:
        new_query_tokens.append(token)
        i = token.find('.')
        if 0 < i < len(token) - 1:
            new_tokens = ['('] + token.replace('.', ' ').split(' ') + [')']
            new_query_tokens.extend(new_tokens)

    return new_query_tokens, str_map
