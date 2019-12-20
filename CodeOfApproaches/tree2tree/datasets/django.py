import os
import torch
import logging

from datasets.dataset import Dataset, parents_prefix
import Constants
from utils.io import deserialize_from_file
from natural_lang.vocab import Vocab
from config import parser


def load_dataset(config, force_regenerate=False):
    dj_dir = './preprocessed/django'
    logging.info('='*80)
    logging.info('Loading datasets from folder ' + dj_dir)
    logging.info('='*80)
    train, test, dev = None, None, None
    prefix = config.syntax + '_'
    if config.unary_closures:
        prefix += 'uc_'

    train_dir = os.path.join(dj_dir, 'train')
    train_file = os.path.join(train_dir, prefix+'train.pth')
    if not force_regenerate and os.path.isfile(train_file):
        logging.info('Train dataset found, loading...')
        #print(train_file)
        train = torch.load(train_file)
        train.config = config

    test_dir = os.path.join(dj_dir, 'test')
    test_file = os.path.join(test_dir, prefix+'test.pth')
    if not force_regenerate and os.path.isfile(test_file):
        logging.info('Test dataset found, loading...')
        test = torch.load(test_file)
        test.config = config

    dev_dir = os.path.join(dj_dir, 'dev')
    dev_file = os.path.join(dev_dir, prefix+'dev.pth')
    if not force_regenerate and os.path.isfile(dev_file):
        logging.info('Dev dataset found, loading...')
        dev = torch.load(dev_file)
        dev.config = config

    if train is None or test is None or dev is None:
        terminal_vocab_file = os.path.join(dj_dir, 'terminal_vocab.txt')
        if config.unary_closures:
            grammar_file = os.path.join(dj_dir, 'grammar.txt.uc.bin')
        else:
            grammar_file = os.path.join(dj_dir, 'grammar.txt.bin')

        grammar = deserialize_from_file(grammar_file)
        terminal_vocab = Vocab(terminal_vocab_file, data=[Constants.UNK_WORD, Constants.EOS_WORD, Constants.PAD_WORD])
        vocab = Vocab(os.path.join(dj_dir, 'vocab.txt'), data=[Constants.UNK_WORD, Constants.EOS_WORD, Constants.PAD_WORD])

        if test is None:
            logging.info('Test dataset not found, generating...')
            test = Dataset(test_dir, 'test', grammar, vocab, terminal_vocab,
                            config.syntax, config.max_example_action_num, config.unary_closures)
            torch.save(test, test_file)

        if dev is None:
            logging.info('Dev dataset not found, generating...')
            dev = Dataset(dev_dir, 'dev', grammar, vocab, terminal_vocab,
                            config.syntax, config.max_example_action_num, config.unary_closures)
            torch.save(dev, dev_file)

        if train is None:
            logging.info('Train dataset not found, generating...')
            train = Dataset(train_dir, 'train', grammar, vocab, terminal_vocab,
                            config.syntax, config.max_example_action_num, config.unary_closures)
            torch.save(train, train_file)
    
    train.prepare_torch(config.cuda)
    dev.prepare_torch(config.cuda)
    test.prepare_torch(config.cuda)
    return train, dev, test


if __name__ == '__main__':
    config = parser.parse_args()
    config.syntax = 'dependency'
    config.unary_closures = False
    load_dataset(config, force_regenerate=True)
    config.unary_closures = True
    load_dataset(config, force_regenerate=True)
