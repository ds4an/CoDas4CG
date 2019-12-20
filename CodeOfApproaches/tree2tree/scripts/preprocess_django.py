import shutil
import glob
from functools import reduce

from scripts.preprocess_utils import *
from lang.parse import *
import Constants
from config import parser
import time


def copy_n_lines(in_f, out_file, n_lines):
    with open(out_file, 'w') as out_f:
        for _ in range(n_lines):
            out_f.write(in_f.readline().strip() + '\n')


def split_file(dataset_file, train_dir, dev_dir, test_dir, ext):
    with open(dataset_file, 'r') as in_f:
        train_file = os.path.join(train_dir, 'train.' + ext)
        copy_n_lines(in_f, train_file, n_lines=13582)

        dev_file = os.path.join(dev_dir, 'dev.' + ext)
        copy_n_lines(in_f, dev_file, n_lines=1269)

        test_file = os.path.join(test_dir, 'test.' + ext)
        copy_n_lines(in_f, test_file, n_lines=1805)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)

    logging.info('=' * 80)
    logging.info('Pre-processing Django dataset')
    logging.info('=' * 80)

    dj_source_dir = './data/en-django/'
    dj_dir = './preprocessed/django/'

    if os.path.exists(dj_dir):
        shutil.rmtree(dj_dir)
    os.makedirs(dj_dir)

    train_dir = os.path.join(dj_dir, 'train')
    dev_dir = os.path.join(dj_dir, 'dev')
    test_dir = os.path.join(dj_dir, 'test')
    make_dirs([train_dir, dev_dir, test_dir])

    shutil.copy(os.path.join(dj_source_dir, 'all.anno'), os.path.join(dj_dir, 'all.anno'))
    shutil.copy(os.path.join(dj_source_dir, 'all.code'), os.path.join(dj_dir, 'all.code'))

    logging.info('Splitting dataset')
    split_file(os.path.join(dj_dir, 'all.anno'), train_dir, dev_dir, test_dir, 'in')
    split_file(os.path.join(dj_dir, 'all.code'), train_dir, dev_dir, test_dir, 'out')

    logging.info('Tokenizing')
    tokenize_with_str_map(os.path.join(dev_dir, 'dev.in'),
                          os.path.join(dev_dir, 'dev.in.tokens'),
                          os.path.join(dev_dir, 'dev.in.strmap.bin'))
    tokenize_with_str_map(os.path.join(train_dir, 'train.in'),
                          os.path.join(train_dir, 'train.in.tokens'),
                          os.path.join(train_dir, 'train.in.strmap.bin'))
    tokenize_with_str_map(os.path.join(test_dir, 'test.in'),
                          os.path.join(test_dir, 'test.in.tokens'),
                          os.path.join(test_dir, 'test.in.strmap.bin'))

    logging.info('Building vocabulary')
    vocab = build_vocab_from_token_files(glob.glob(os.path.join(dj_dir, '*/*.tokens')), min_frequency=3)
    save_vocab(os.path.join(dj_dir, 'vocab.txt'), vocab)

    logging.info('Build vocab embeddings')
    vocab = Vocab(filename=os.path.join(dj_dir, 'vocab.txt'),
                  data=[Constants.UNK_WORD, Constants.EOS_WORD, Constants.PAD_WORD])
    emb_file = os.path.join(dj_dir, 'word_embeddings.pth')
    glove_file = os.path.join(data_dir, 'glove/glove.840B.300d')
    glove_vocab, glove_emb = load_word_vectors(glove_file)
    emb = torch.Tensor(vocab.size(), glove_emb.size(1)).normal_(0.0, 0.1)

    for idx, item in enumerate([Constants.UNK_WORD, Constants.EOS_WORD, Constants.PAD_WORD]):
        emb[idx].zero_()
    for word in vocab.labelToIdx.keys():
        if glove_vocab.getIndex(word):
            emb[vocab.getIndex(word)] = glove_emb[glove_vocab.getIndex(word)]
    torch.save(emb, emb_file)

    logging.info('Parsing descriptions trees')
    parse(os.path.join(dev_dir, 'dev.in.tokens'))
    time.sleep(10)
    parse(os.path.join(train_dir, 'train.in.tokens'))
    print('finish--------------------------')
    #time.sleep(10000)
    parse(os.path.join(test_dir, 'test.in.tokens'))

    logging.info('Parsing output code')
    parse_trees_dev = parse_code_trees(os.path.join(dev_dir, 'dev.out'),
                                       os.path.join(dev_dir, 'dev.in.strmap.bin'),
                                       os.path.join(dev_dir, 'dev.out.bin'),
                                       os.path.join(dev_dir, 'dev.out.raw.bin'))
    parse_trees_train = parse_code_trees(os.path.join(train_dir, 'train.out'),
                                         os.path.join(train_dir, 'train.in.strmap.bin'),
                                         os.path.join(train_dir, 'train.out.bin'),
                                         os.path.join(train_dir, 'train.out.raw.bin'))
    parse_trees_test = parse_code_trees(os.path.join(test_dir, 'test.out'),
                                        os.path.join(test_dir, 'test.in.strmap.bin'),
                                        os.path.join(test_dir, 'test.out.bin'),
                                        os.path.join(test_dir, 'test.out.raw.bin'))
    parse_trees = parse_trees_dev+parse_trees_train+parse_trees_test

    # without u c
    logging.info('Saving trees')
    write_trees(parse_trees_dev, os.path.join(dev_dir, 'dev.out.trees'))
    write_trees(parse_trees_train, os.path.join(train_dir, 'train.out.trees'))
    write_trees(parse_trees_test, os.path.join(test_dir, 'test.out.trees'))

    logging.info('Creating grammar')
    grammar = write_grammar(parse_trees, os.path.join(dj_dir, 'grammar.txt'))

    logging.info('Creating terminal vocabulary')
    write_terminal_tokens_vocab(grammar, parse_trees, os.path.join(dj_dir, 'terminal_vocab.txt'), min_freq=1)

    # with u c
    logging.info('Applying unary closures')
    do_unary_closures(parse_trees, 20)

    logging.info('Saving trees with unary closures')
    write_trees(parse_trees_dev, os.path.join(dev_dir, 'dev.out.trees.uc'))
    write_trees(parse_trees_train, os.path.join(train_dir, 'train.out.trees.uc'))
    write_trees(parse_trees_test, os.path.join(test_dir, 'test.out.trees.uc'))

    logging.info('Creating grammar')
    grammar = write_grammar(parse_trees, os.path.join(dj_dir, 'grammar.txt.uc'))
