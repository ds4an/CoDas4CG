import os
import numpy as np
import logging
import sys
import torch
import torch.optim as optim
import random
import shutil
# from tensorboardX import SummaryWriter

from utils.general import init_logging
from model.x2x import Tree2TreeModel
from config import parser
from trainer import Trainer
from model.utils import device_map_location


if __name__ == '__main__':
    args = parser.parse_args()

    # arguments validation
    args.cuda = args.cuda and torch.cuda.is_available()

    # random seed
    np.random.seed(args.random_seed)
    torch.manual_seed(args.random_seed)
    random.seed(args.random_seed)
    if args.cuda:
        torch.cuda.manual_seed(args.random_seed)
        torch.backends.cudnn.benchmark = True

    # prepare dirs
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    # start logging
    init_logging(os.path.join(args.output_dir, 'parser.log'))
    logging.info('command line: %s', ' '.join(sys.argv))
    logging.info('current config: %s', args)
    logging.info('loading dataset [%s]', args.dataset)

    # load data
    load_dataset = None
    if args.dataset == 'hs':
        print('hsdataset!')
        from datasets.hs import load_dataset
    elif args.dataset == 'django':
        print('djdataset!')
        from datasets.django import load_dataset
    else:
        raise Exception('Dataset {} is not prepared yet'.format(args.dataset))
    print(args)
    train_data, dev_data, test_data = load_dataset(args)
    #print(len(train_data), len(dev_data), len(test_data))
    # configure more variables
    args.source_vocab_size = train_data.vocab.size()
    args.target_vocab_size = train_data.terminal_vocab.size()
    args.rule_num = len(train_data.grammar.rules)
    args.node_num = len(train_data.grammar.node_type_to_id)

    # load model
    if args.model:
        logging.info('Loading model: {}'.format(args.model))
        # device map location allows to load model trained on GPU on CPU env and vice versa
        model = torch.load(args.model, device_map_location(args.cuda))
    else:
        logging.info('Creating new model'.format(args.model))
        emb_file = os.path.join(args.data_dir, 'word_embeddings.pth')
        emb = torch.load(emb_file)
        model = Tree2TreeModel(args, emb, train_data.terminal_vocab, train_data.grammar)
        if args.cuda:
            model = model.cuda()

    # create learner
    optimizer = optim.Adam([p for p in model.parameters() if p.requires_grad], lr=args.lr)
    trainer = Trainer(model, args, optimizer)

    if args.mode == 'train':
        trainer.train_all(train_data, dev_data, test_data, args.output_dir)
    elif args.mode == 'validate':
        tmp_epoch_dir = os.path.join(args.output_dir, 'tmp')
        if os.path.exists(tmp_epoch_dir):
            shutil.rmtree(tmp_epoch_dir)
        os.mkdir(tmp_epoch_dir)
        #print(len(test_data))
        #print('--------------aaa-------')
        trainer.validate(test_data, 0, tmp_epoch_dir)
    elif args.mode == 'start_batch':
        trainer.train(train_data, 0, st_batch=59)
    else:
        raise Exception("Unknown mode!")
