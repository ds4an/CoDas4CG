import shutil
import glob
from functools import reduce

from scripts.preprocess_utils import *
from lang.parse import *
import Constants
from config import parser

position_symbols = ["NAME_END",
                    "ATK_END",
                    "DEF_END",
                    "COST_END",
                    "DUR_END",
                    "TYPE_END",
                    "PLAYER_CLS_END",
                    "RACE_END",
                    "RARITY_END"]

names = ['Name', 'attack', 'defence', 'cost', 'duration', 'type', 'player class', 'race', 'rarity']


def extract_from_hs_line(line, end_symbol, start_pos=None):
    if start_pos is None:
        start_pos = 0

    end_pos = line.find(" " + end_symbol)
    result = line[start_pos:end_pos]
    new_pos = end_pos + len(end_symbol) + 2
    return result, new_pos


def tranform_description(vars, desc):
    vars_desc = map(lambda t: '{}: {}'.format(t[0], t[1]), zip(names, vars))
    vars_line = reduce(lambda v1, v2: '{}, {}'.format(v1, v2), vars_desc) + "."

    if desc == "NIL\n":
        desc = vars_line + "\n"
    else:
        desc = vars_line + " " + desc
    return re.sub(r"<[^>]*>", "", desc)


def split_input(filepath):
    logging.info('Splitting input ' + filepath)
    with open(filepath, 'r') as datafile, \
         open(filepath + '.description', 'w') as dfile:
            for line in tqdm(datafile.readlines()):
                vars = []
                position = 0
                for pos_sym in position_symbols:
                    var, position = extract_from_hs_line(line, pos_sym, position)
                    if var == "NIL":
                        var = "None"
                    vars.append(var)

                description = tranform_description(vars, line[position:])
                dfile.write(description)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)

    logging.info('=' * 80)
    logging.info('Pre-processing HearthStone dataset')
    logging.info('=' * 80)

    hs_source_dir = './data/card2code/third_party/hearthstone/'
    hs_dir = './preprocessed/hs/'

    if os.path.exists(hs_dir):
        shutil.rmtree(hs_dir)
    os.makedirs(hs_dir)

    train_dir = os.path.join(hs_dir, 'train')
    dev_dir = os.path.join(hs_dir, 'dev')
    test_dir = os.path.join(hs_dir, 'test')
    make_dirs([train_dir, dev_dir, test_dir])

    shutil.copy(os.path.join(hs_source_dir, 'dev_hs.in'), os.path.join(dev_dir, 'dev.in'))
    shutil.copy(os.path.join(hs_source_dir, 'dev_hs.out'), os.path.join(dev_dir, 'dev.out'))
    shutil.copy(os.path.join(hs_source_dir, 'train_hs.in'), os.path.join(train_dir, 'train.in'))
    shutil.copy(os.path.join(hs_source_dir, 'train_hs.out'), os.path.join(train_dir, 'train.out'))
    shutil.copy(os.path.join(hs_source_dir, 'test_hs.in'), os.path.join(test_dir, 'test.in'))
    shutil.copy(os.path.join(hs_source_dir, 'test_hs.out'), os.path.join(test_dir, 'test.out'))

    logging.info('Splitting dataset')
    split_input(os.path.join(dev_dir, 'dev.in'))
    split_input(os.path.join(train_dir, 'train.in'))
    split_input(os.path.join(test_dir, 'test.in'))

    logging.info('Tokenizing')
    tokenize_with_str_map(os.path.join(dev_dir, 'dev.in.description'),
                          os.path.join(dev_dir, 'dev.in.tokens'),
                          os.path.join(dev_dir, 'dev.in.strmap.bin'))
    tokenize_with_str_map(os.path.join(train_dir, 'train.in.description'),
                          os.path.join(train_dir, 'train.in.tokens'),
                          os.path.join(train_dir, 'train.in.strmap.bin'))
    tokenize_with_str_map(os.path.join(test_dir, 'test.in.description'),
                          os.path.join(test_dir, 'test.in.tokens'),
                          os.path.join(test_dir, 'test.in.strmap.bin'))

    logging.info('Building vocabulary')
    vocab = build_vocab_from_token_files(glob.glob(os.path.join(hs_dir, '*/*.tokens')), min_frequency=3)
    save_vocab(os.path.join(hs_dir, 'vocab.txt'), vocab)

    logging.info('Build vocab embeddings')
    vocab = Vocab(filename=os.path.join(hs_dir, 'vocab.txt'),
                  data=[Constants.UNK_WORD, Constants.EOS_WORD, Constants.PAD_WORD])
    emb_file = os.path.join(hs_dir, 'word_embeddings.pth')
    glove_file = os.path.join(data_dir, 'glove/glove.840B.300d')
    print(glove_file)
    # load glove embeddings and vocab
    glove_vocab, glove_emb = load_word_vectors(glove_file)
    emb = torch.Tensor(vocab.size(), glove_emb.size(1)).normal_(0.0, 0.1)
    # zero out the embeddings for padding and other special words if they are absent in vocab
    for idx, item in enumerate([Constants.UNK_WORD, Constants.EOS_WORD, Constants.PAD_WORD]):
        emb[idx].zero_()
    for word in vocab.labelToIdx.keys():
        if glove_vocab.getIndex(word):
            emb[vocab.getIndex(word)] = glove_emb[glove_vocab.getIndex(word)]
    torch.save(emb, emb_file)

    logging.info('Parsing descriptions trees')
    #parse(os.path.join(dev_dir, 'dev.in.tokens'))
    #parse(os.path.join(train_dir, 'train.in.tokens'))
    #parse(os.path.join(test_dir, 'test.in.tokens'))

    logging.info('Parsing output code')
    lb = 'В§' if system == 'w' else '§'
    parse_trees_dev = parse_code_trees(os.path.join(dev_dir, 'dev.out'),
                                       os.path.join(dev_dir, 'dev.in.strmap.bin'),
                                       os.path.join(dev_dir, 'dev.out.bin'),
                                       os.path.join(dev_dir, 'dev.out.raw.bin'), lb=lb)
    parse_trees_train = parse_code_trees(os.path.join(train_dir, 'train.out'),
                                         os.path.join(train_dir, 'train.in.strmap.bin'),
                                         os.path.join(train_dir, 'train.out.bin'),
                                         os.path.join(train_dir, 'train.out.raw.bin'), lb=lb)
    parse_trees_test = parse_code_trees(os.path.join(test_dir, 'test.out'),
                                        os.path.join(test_dir, 'test.in.strmap.bin'),
                                        os.path.join(test_dir, 'test.out.bin'),
                                        os.path.join(test_dir, 'test.out.raw.bin'), lb=lb)
    parse_trees = parse_trees_dev+parse_trees_train+parse_trees_test

    logging.info('Saving trees')
    write_trees(parse_trees_dev, os.path.join(dev_dir, 'dev.out.trees'))
    write_trees(parse_trees_train, os.path.join(train_dir, 'train.out.trees'))
    write_trees(parse_trees_test, os.path.join(test_dir, 'test.out.trees'))

    logging.info('Creating grammar')
    grammar = write_grammar(parse_trees, os.path.join(hs_dir, 'grammar.txt'))

    logging.info('Creating terminal vocabulary')
    write_terminal_tokens_vocab(grammar, parse_trees, os.path.join(hs_dir, 'terminal_vocab.txt'), min_freq=3)

    logging.info('Applying unary closures')
    do_unary_closures(parse_trees, 30)

    logging.info('Saving trees')
    write_trees(parse_trees_dev, os.path.join(dev_dir, 'dev.out.trees.uc'))
    write_trees(parse_trees_train, os.path.join(train_dir, 'train.out.trees.uc'))
    write_trees(parse_trees_test, os.path.join(test_dir, 'test.out.trees.uc'))

    logging.info('Creating grammar')
    grammar = write_grammar(parse_trees, os.path.join(hs_dir, 'grammar.txt.uc'))

