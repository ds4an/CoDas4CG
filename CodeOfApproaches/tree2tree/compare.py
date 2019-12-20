import os
import argparse
import torch

from utils.io import deserialize_from_file
from natural_lang.vocab import Vocab
import Constants
from datasets.dataset import Dataset


def load_test_dataset(data_dir, syntax, max_example_actions_num):
    # all with unary closures
    terminal_vocab_file = os.path.join(data_dir, 'terminal_vocab.txt')
    grammar_file = os.path.join(data_dir, 'grammar.txt.uc.bin')

    grammar = deserialize_from_file(grammar_file)
    terminal_vocab = Vocab(terminal_vocab_file, data=[Constants.UNK_WORD, Constants.EOS_WORD, Constants.PAD_WORD])
    vocab = Vocab(os.path.join(data_dir, 'vocab.txt'), data=[Constants.UNK_WORD, Constants.EOS_WORD, Constants.PAD_WORD])

    prefix = 'uc_' + syntax + '_'
    test_dir = os.path.join(data_dir, 'test')
    test = Dataset(test_dir, 'test', grammar, vocab, terminal_vocab, syntax, max_example_actions_num, True)
    torch.save(test, test_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-models_dir')
    parser.add_argument('-data_dir')

    args = parser.parse_args()

    ccg_model_file = os.path.join(args.models_dir, 'ccg_model.pth')
    if os.path.exists(ccg_model_file):
        ccg_model = torch.load(ccg_model_file)

    dependency_model_file = os.path.join(args.models_dir, 'dependency_model.pth')
    if os.path.exists(dependency_model_file):
        dependency_model = torch.load(dependency_model_file)

    pcfg_model_file = os.path.join(args.models_dir, 'pcfg_model.pth')
    if os.path.exists(dependency_model_file):
        pcfg_model = torch.load(dependency_model_file)

    bilstm_model_file = os.path.join(args.models_dir, 'bilstm_model.pth')