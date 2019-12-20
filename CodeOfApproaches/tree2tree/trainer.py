import torch
from tqdm import tqdm
import logging
import astor
import os
import numpy as np
import math
import shutil
import pandas as pd

from lang.parse import decode_tree_to_python_ast
from utils.general import get_batches
from utils.eval import evaluate_decode_result
from utils.io import send_telegram


class Trainer(object):
    def __init__(self, model, config, optimizer):
        self.config = config
        self.model = model
        self.optimizer = optimizer

    def train_all(self, train_data, dev_data, test_data, results_dir):
        max_epoch = self.config.max_epoch
        patience_counter = 0
        history_valid_perf = []
        history_valid_bleu = []
        history_valid_acc = []
        history_errors = []
        history_loss = []
        best_model_file = None
        validation_bleu, validation_accuracy, validation_errors = 0.0, 0.0, 0.0
        for epoch in range(max_epoch):
            loss = self.train(train_data, epoch)
            history_loss.append(loss)
            logging.info('Epoch {} training finished, loss: {}.'.format(epoch+1, loss))

            epoch_dir = os.path.join(results_dir, str(epoch+1))
            if os.path.exists(epoch_dir):
                shutil.rmtree(epoch_dir)
            os.mkdir(epoch_dir)
            model_path = os.path.join(epoch_dir, 'model.pth')
            logging.info('Saving model at {}.'.format(model_path))
            torch.save(self.model, model_path)
            '''
            bleu, accuracy, errors = self.validate(dev_data, epoch, epoch_dir)
            logging.info('Epoch {} validation finished, bleu: {}, accuracy: {}, errors: {}.'.format(
                epoch + 1, bleu, accuracy, errors))

            history_valid_acc.append(accuracy)
            history_valid_bleu.append(bleu)
            history_errors.append(errors)
            val_perf = eval(self.config.valid_metric)

            if val_perf > 0.02:
                if len(history_valid_perf) == 0 or val_perf > np.array(history_valid_perf).max():
                    patience_counter = 0
                    logging.info('Found best model on epoch {}'.format(epoch+1))
                    best_model_file = model_path
                    validation_accuracy = accuracy
                    validation_bleu = bleu
                    validation_error = errors
                else:
                    patience_counter += 1
                    logging.info('Hitting patience_counter: {}'.format(patience_counter))
                    if patience_counter >= self.config.train_patience:
                        logging.info('Early Stop!')
                        break

            history_valid_perf.append(val_perf)
            # save performance metrics on every step
            hist_df = pd.DataFrame(list(zip(history_valid_bleu,
                                            history_valid_acc,
                                            history_errors,
                                            history_loss)),
                                   columns=['BLEU', 'Accuracy', 'Errors', 'Loss'])
            history_file = os.path.join(results_dir, 'hist.csv')
            hist_df.to_csv(history_file, index=False)

        # test set evaluation
        if best_model_file is not None:
            self.model = torch.load(best_model_file)
            dir = os.path.join(results_dir, 'final')
            if os.path.exists(dir):
                shutil.rmtree(dir)
            os.mkdir(dir)
            bleu, accuracy, errors = self.validate(test_data, -100, dir)
            logging.info('Test set evaluation finished, bleu: {}, accuracy: {}, errors: {}.'.format(
                bleu, accuracy, errors))

            model_path = os.path.join(dir, 'model.pth')
            logging.info('Saving model at {}.'.format(model_path))
            torch.save(self.model, model_path)

            report_result = {
                "Test BLEU": bleu,
                "Test accuracy": accuracy,
                "Test error": errors,
                "Validation BLEU": validation_bleu,
                "Validation accuracy": validation_accuracy,
                "Validation error": validation_error,
                "Last epoch": epoch,
                "Mean error": np.mean(history_errors)
            }
            print(report_result)
            self.report_bot(report_result)
            '''

    def train(self, dataset, epoch, st_batch=None):
        self.model.train()
        self.optimizer.zero_grad()
        total_loss = 0.0
        batch_size = self.config.batch_size
        indices = torch.randperm(len(dataset))
        if self.config.cuda:
            indices = indices.cuda()
        total_batches = math.floor(len(indices)/batch_size)+1
        batches = list(get_batches(indices, batch_size))

        if st_batch:
            batches = batches[st_batch:]

        for i, batch in tqdm(enumerate(batches), desc='Training epoch '+str(epoch+1)+'', total=total_batches):
            trees, queries, tgt_node_seq, tgt_par_rule_seq, tgt_par_t_seq, \
            tgt_action_seq, tgt_action_seq_type = dataset.get_batch(batch)
            #print(trees)
            loss = self.model.forward_train(trees, queries, tgt_node_seq, tgt_action_seq, tgt_par_rule_seq, tgt_par_t_seq, tgt_action_seq_type)
            assert loss > 0, "NLL can not be less than zero"

            total_loss += loss.data[0]
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()
            logging.debug('Batch {}, loss {}'.format(i+1, loss[0]))

        return total_loss/len(dataset)

    def validate(self, dataset, epoch, out_dir):
        self.model.eval()
        cum_bleu, cum_acc = 0.0, 0.0
        errors = 0
        for idx in tqdm(range(len(dataset)), desc='Testing epoch '+str(epoch+1)+''):
            data_entry = dataset[idx]
            cand_list = self.model(data_entry['query_tree'], data_entry['query'], data_entry['query_tokens'])
            candidats = []
            #print("aaaaaaa")
            code = ''
            #print(cand_list)
            for cid, cand in enumerate(cand_list[:self.config.beam_size]):
                try:
                    ast_tree = decode_tree_to_python_ast(cand.tree)
                    #print(ast_tree)
                    for c in ast_tree.children:
                        code += astor.to_source(c)
                    #print(code)
                    candidats.append((cid, cand, ast_tree, code))
                except:
                    logging.debug("Exception in converting tree to code:"
                                  "id: {}, beam pos: {}".format(idx, cid))
                    errors += 1
            if len(candidats) > 0:
                bleu, acc, error =  evaluate_decode_result(data_entry, idx, candidats[0], out_dir)
                cum_bleu += bleu
                cum_acc += acc
                # errors += 1
        
        cum_bleu /= len(dataset)
        cum_acc /= len(dataset)
        errors /= (len(dataset) * self.config.beam_size)

        return cum_bleu, cum_acc, errors

    def visualize(self, dataset, writer):
        self.model.train()
        self.optimizer.zero_grad()
        batch_size = 2
        indices = torch.randperm(len(dataset))
        batch = next(get_batches(indices, batch_size))

        trees, queries, tgt_node_seq, tgt_par_rule_seq, tgt_par_t_seq, \
        tgt_action_seq, tgt_action_seq_type = dataset.get_batch(batch)

        loss = self.model.forward_train(trees, queries, tgt_node_seq, tgt_action_seq, tgt_par_rule_seq, tgt_par_t_seq, tgt_action_seq_type)
        assert loss > 0, "NLL can not be less than zero"

        loss.backward()
        writer.add_graph(self.model, loss)

    def report_bot(self, report_dict):
        msg = "Finished experiment with config {}.\n\n".format(self.config)
        msg += "\n".join(["{}: {}.".format(k, v) for k, v in report_dict.items()])
        send_telegram(msg)
