import sys
from torch.nn import Parameter
import numpy as np

import Constants
from model.encoder import EncoderLSTMWrapper
from model.decoder import *
from model.layers import *
from model.utils import *
from lang.hyp import Hyp

sys.setrecursionlimit(50000)


class Tree2TreeModel(nn.Module):
    def __init__(self, config, word_embeds, terminal_vocab, grammar):
        super().__init__()

        self.config = config
        self.thought = self.config.thought_vector

        self.terminal_vocab = terminal_vocab
        self.grammar = grammar

        self.word_embedding = nn.Embedding(word_embeds.shape[0], config.word_embed_dim, padding_idx=Constants.PAD)
        if config.pretrained_embeds:
            self.word_embedding.weight.data.copy_(word_embeds)
        else:
            init.normal(self.word_embedding.weight, 0.0, 0.2)
        if config.freeze_embeds:
            self.word_embedding.weight.requires_grad = False

        self.encoder = EncoderLSTMWrapper(config)

        self.decoder = CondAttLSTM(config.rule_embed_dim + config.node_embed_dim + config.rule_embed_dim,
                                   config.decoder_hidden_dim,
                                   config.encoder_hidden_dim,
                                   config.attention_hidden_dim,
                                   config)

        self.src_ptr_net = PointerNet(config)

        self.terminal_gen_softmax = LogSoftmaxDense(config.decoder_hidden_dim, 2)
        init.xavier_uniform(self.terminal_gen_softmax.weight)
        self.terminal_gen_softmax.bias = parameter_init_zero(2)

        self.rule_gen_softmax = LogSoftmaxDense(config.rule_embed_dim, config.rule_num)
        init.normal(self.rule_gen_softmax.weight, 0, 0.1)
        self.rule_gen_softmax.bias = parameter_init_zero(config.rule_num)

        self.vocab_gen_softmax = LogSoftmaxDense(config.rule_embed_dim, config.target_vocab_size)
        init.normal(self.vocab_gen_softmax.weight, 0, 0.1)
        self.vocab_gen_softmax.bias = parameter_init_zero(config.target_vocab_size)
        #print(config.node_num) 
        #print(config.node_embed_dim)
        self.node_embedding = Parameter(torch.FloatTensor(config.node_num, config.node_embed_dim))
        init.normal(self.node_embedding, 0, 0.1)

        # decoder_hidden_dim -> action embed
        self.decoder_hidden_state_W_rule = nn.Linear(config.decoder_hidden_dim, config.rule_embed_dim)
        init.xavier_uniform(self.decoder_hidden_state_W_rule.weight)
        self.decoder_hidden_state_W_rule.bias = parameter_init_zero(config.rule_embed_dim)
        # decoder_hidden_dim -> action embed
        self.decoder_hidden_state_W_token = nn.Linear(config.decoder_hidden_dim + config.encoder_hidden_dim,
                                                      config.rule_embed_dim)
        init.xavier_uniform(self.decoder_hidden_state_W_token.weight)
        self.decoder_hidden_state_W_token.bias = parameter_init_zero(config.rule_embed_dim)

        self.log_softmax = nn.LogSoftmax(dim=-1)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, tree, query_tokens, query_raw):
        vocab_embedding = self.vocab_gen_softmax.weight
        rule_embedding = self.rule_gen_softmax.weight
        #print('f1-----------------')
        # forward encoding accepts batches, whether forward of all model takes one example at time
        h, c, ctx = self.forward_encode([tree], query_tokens[None])
        # (decoder_hidden_dim)
        h = h.squeeze(0)
        c = c.squeeze(0)
        h = h if self.thought else init_var(self.config.decoder_hidden_dim,
                                            cuda=h.is_cuda, scale=0.1, training=self.training)
        c = c if self.thought else init_var(self.config.decoder_hidden_dim,
                                            cuda=c.is_cuda, scale=0.1, training=self.training)

        completed_hyps = []
        completed_hyp_num = 0
        live_hyp_num = 1

        root_hyp = Hyp(self.grammar)
        root_hyp.state = h
        root_hyp.cell = c
        root_hyp.action_embed = Var(zeros(self.config.rule_embed_dim, cuda=h.is_cuda), requires_grad=False)
        root_hyp.node_id = self.grammar.get_node_type_id(root_hyp.tree.type)
        root_hyp.parent_rule_id = -1

        hyp_samples = [root_hyp]

        # source word id in the terminal vocab
        src_token_id = self.terminal_vocab.convertToIdx(query_raw, Constants.UNK_WORD)
        unk_pos_list = [x for x, t in enumerate(src_token_id) if t == Constants.UNK]

        # sometimes a word may appear multi-times in the source, in this case,
        # we just copy its first appearing position. Therefore we mask the words
        # appearing second and onwards to -1
        token_set = set()
        for i, tid in enumerate(src_token_id):
            if tid in token_set:
                src_token_id[i] = -1
            else:
                token_set.add(tid)

        for t in range(self.config.decode_max_time_step):
            hyp_num = len(hyp_samples)
            # (hyp_num, decoder_hidden_dim)
            h = torch.stack([hyp.state for hyp in hyp_samples])
            c = torch.stack([hyp.cell for hyp in hyp_samples])

            # (hyp_num, max_time_step, decoder_hidden_dim)
            hist_h = Var(zeros(hyp_num, self.config.decode_max_time_step, self.config.decoder_hidden_dim, cuda=h.is_cuda), requires_grad=False)

            if t > 0:
                for i, hyp in enumerate(hyp_samples):
                    hist_h[i, :len(hyp.hist_h), :] = torch.stack(hyp.hist_h)
                    # for j, h in enumerate(hyp.hist_h):
                    #    hist_h[i, j] = h

            # (hyp_num, decoder_hidden_dim)
            prev_action_embed = torch.stack([hyp.action_embed for hyp in hyp_samples])
            # (hyp_num)
            node_id = from_long_list([hyp.node_id for hyp in hyp_samples], h.is_cuda)
            parent_rule_id = from_long_list([hyp.parent_rule_id for hyp in hyp_samples], h.is_cuda)
            parent_t = from_long_list([hyp.get_action_parent_t() for hyp in hyp_samples], h.is_cuda)

            # (hyp_num, 1, decoder_hidden_dim)
            index = Var(parent_t.unsqueeze(1).unsqueeze(2).expand(-1, -1, self.config.decoder_hidden_dim), requires_grad=False)
            # (hyp_num, decoder_hidden_dim)
            parent_h = torch.gather(hist_h, 1, index).squeeze(1)
            # (live_hyp_num, query_length, decoder_hidden_dim)
            ctx_tiled = ctx.repeat(live_hyp_num, 1, 1)

            h, c, \
            rule_prob, gen_action_prob, vocab_prob, copy_prob = \
                self.forward_decoder_step(t,
                                          h, c, hist_h,
                                          prev_action_embed,
                                          node_id, parent_rule_id,
                                          parent_h,
                                          ctx_tiled)

            new_hyp_samples = []

            # move probabilities to cpu and numpy
            if self.config.cuda:
                rule_prob = rule_prob.cpu()
                gen_action_prob = gen_action_prob.cpu()
                vocab_prob = vocab_prob.cpu()
                copy_prob = copy_prob.cpu()

            rule_prob = rule_prob.data.numpy()
            gen_action_prob = gen_action_prob.data.numpy()
            vocab_prob = vocab_prob.data.numpy()
            copy_prob = copy_prob.data.numpy()

            # iterating over items in the beam
            word_prob = gen_action_prob[:, 0:1] * vocab_prob
            word_prob[:, Constants.UNK] = 0

            hyp_scores = np.array([hyp.score for hyp in hyp_samples])

            # word_prob[:, src_token_id] += gen_action_prob[:, 1:2] * copy_prob[:, :len(src_token_id)]
            # word_prob[:, unk] = 0

            rule_apply_cand_hyp_ids = []
            rule_apply_cand_scores = []
            rule_apply_cand_rules = []
            rule_apply_cand_rule_ids = []

            hyp_frontier_nts = []
            word_gen_hyp_ids = []
            cand_copy_probs = []
            unk_words = []

            for k in range(live_hyp_num):
                hyp = hyp_samples[k]

                # if k == 0:
                #     print 'Top Hyp: %s' % hyp.tree.__repr__()

                frontier_nt = hyp.frontier_nt()
                hyp_frontier_nts.append(frontier_nt)

                assert hyp, 'none hyp!'

                # if it's not a leaf
                if not self.grammar.is_value_node(frontier_nt):
                    # iterate over all the possible rules
                    rules = self.grammar[frontier_nt.as_type_node] if self.config.head_nt_constraint else self.grammar
                    assert len(rules) > 0, 'fail to expand nt node %s' % frontier_nt
                    for rule in rules:
                        rule_id = self.grammar.rule_to_id[rule]

                        cur_rule_score = np.log(rule_prob[k, rule_id] + 1.e-7)
                        new_hyp_score = hyp.score + cur_rule_score

                        rule_apply_cand_hyp_ids.append(k)
                        rule_apply_cand_scores.append(new_hyp_score)
                        rule_apply_cand_rules.append(rule)
                        rule_apply_cand_rule_ids.append(rule_id)

                else:  # it's a leaf that holds values
                    cand_copy_prob = 0.0
                    for i, tid in enumerate(src_token_id):
                        try:
                            if tid != -1: 
                                word_prob[k, tid] += gen_action_prob[k, 1] * copy_prob[k, i]
                                cand_copy_prob = gen_action_prob[k, 1]
                        except Exception as e:
                            print(e,k,tid)
                    # and unk copy probability
                    if len(unk_pos_list) > 0:
                        unk_pos = copy_prob[k, unk_pos_list].argmax()
                        unk_pos = unk_pos_list[unk_pos]

                        unk_copy_score = gen_action_prob[k, 1] * copy_prob[k, unk_pos]
                        word_prob[k, Constants.UNK] = unk_copy_score

                        unk_word = query_raw[unk_pos]
                        unk_words.append(unk_word)

                        cand_copy_prob = gen_action_prob[k, 1]

                    word_gen_hyp_ids.append(k)
                    cand_copy_probs.append(cand_copy_prob)

            # prune the hyp space
            if completed_hyp_num >= self.config.beam_size:
                break

            word_prob = np.log(word_prob + 1.e-7)

            word_gen_hyp_num = len(word_gen_hyp_ids)
            rule_apply_cand_num = len(rule_apply_cand_scores)

            if word_gen_hyp_num > 0:
                word_gen_cand_scores = hyp_scores[word_gen_hyp_ids, None] + word_prob[word_gen_hyp_ids, :]
                word_gen_cand_scores_flat = word_gen_cand_scores.flatten()

                cand_scores = np.concatenate([rule_apply_cand_scores, word_gen_cand_scores_flat])
            else:
                cand_scores = np.array(rule_apply_cand_scores)

            top_cand_ids = (-cand_scores).argsort()[:self.config.beam_size - completed_hyp_num]

            # expand_cand_num = 0
           # print('tpi-----------')
           # print(top_cand_ids)
            for cand_id in top_cand_ids:
                # cand is rule application
                new_hyp = None
                if cand_id < rule_apply_cand_num:
                    hyp_id = rule_apply_cand_hyp_ids[cand_id]
                    hyp = hyp_samples[hyp_id]
                    rule_id = rule_apply_cand_rule_ids[cand_id]
                    rule = rule_apply_cand_rules[cand_id]
                    new_hyp_score = rule_apply_cand_scores[cand_id]

                    new_hyp = Hyp(hyp)
                    new_hyp.apply_rule(rule)

                    new_hyp.score = new_hyp_score
                    new_hyp.state = h[hyp_id].clone()
                    new_hyp.hist_h.append(new_hyp.state.clone())
                    new_hyp.cell = c[hyp_id].clone()
                    new_hyp.action_embed = rule_embedding[rule_id]
                else:
                    tid = (cand_id - rule_apply_cand_num) % word_prob.shape[1]
                    word_gen_hyp_id = int((cand_id - rule_apply_cand_num) / word_prob.shape[1])
                    hyp_id = word_gen_hyp_ids[word_gen_hyp_id]

                    if tid == Constants.UNK:
                        token = unk_words[word_gen_hyp_id]
                    else:
                        token = self.terminal_vocab.getLabel(tid)

                    frontier_nt = hyp_frontier_nts[hyp_id]
                    # if frontier_nt.type == int and (not (is_numeric(token) or token == '<eos>')):
                    #     continue

                    hyp = hyp_samples[hyp_id]
                    new_hyp_score = word_gen_cand_scores[word_gen_hyp_id, tid]

                    new_hyp = Hyp(hyp)
                    new_hyp.append_token(token)

                    # if log:
                    #     cand_copy_prob = cand_copy_probs[word_gen_hyp_id]
                    #     if cand_copy_prob > 0.5:
                    #         new_hyp.log += ' || ' + str(new_hyp.frontier_nt()) + '{copy[%s][p=%f]}' % (
                    #             token, cand_copy_prob)

                    new_hyp.score = new_hyp_score
                    new_hyp.state = h[hyp_id].clone()
                    new_hyp.hist_h.append(new_hyp.state.clone())
                    new_hyp.cell = c[hyp_id].clone()
                    new_hyp.action_embed = vocab_embedding[int(tid)].clone()
                    new_hyp.node_id = self.grammar.get_node_type_id(frontier_nt)

                # get the new frontier nt after rule application
                new_frontier_nt = new_hyp.frontier_nt()

                # if new_frontier_nt is None, then we have a new completed hyp!
                if new_frontier_nt is None:
                    #print('aa')
                    # if t <= 1:
                    #     continue
                    new_hyp.n_timestep = t + 1
                    completed_hyps.append(new_hyp)
                    completed_hyp_num += 1
                else:
                    #print('bb')
                    new_hyp.node_id = self.grammar.get_node_type_id(new_frontier_nt.type)
                    # new_hyp.parent_rule_id = grammar.rule_to_id[
                    #     new_frontier_nt.parent.to_rule(include_value=False)]
                    new_hyp.parent_rule_id = self.grammar.rule_to_id[new_frontier_nt.parent.applied_rule]

                    new_hyp_samples.append(new_hyp)

                    # expand_cand_num += 1
                    # if expand_cand_num >= beam_size - completed_hyp_num:
                    #     break

                    # cand is word generation

            live_hyp_num = min(len(new_hyp_samples), self.config.beam_size - completed_hyp_num)
            if live_hyp_num < 1:
                #print('这就break了？')
                break

            hyp_samples = new_hyp_samples[:live_hyp_num]
            hyp_samples = sorted(new_hyp_samples, key=lambda x: x.score, reverse=True)[:live_hyp_num]

        completed_hyps = sorted(completed_hyps, key=lambda x: x.score, reverse=True)
        #print(len(completed_hyps))
        return completed_hyps
        #return hyp_samples

    def forward_encode(self, trees, queries):
        queries = Var(queries, requires_grad=False)
        # (batch_size, query_length, word_embed_dim)
        query_embeds = self.word_embedding(queries)
        return self.encoder(trees, query_embeds)

    def forward_decoder_step(self, t,
                             h, c, hist_h,
                             prev_action_embed,
                             node_id, par_rule_id,
                             parent_h,
                             ctx):
        # (batch_size, node_embed_dim)
        node_embed = self.node_embedding[node_id]

        # (batch_size, decoder_hidden_dim)
        empty_state = Var(zeros(par_rule_id.shape[0], self.config.rule_embed_dim, cuda=h.is_cuda), requires_grad=False)
        par_rule_embed = index_select_if_none(self.rule_gen_softmax.weight,
                                              0, par_rule_id, empty_state)

        if not self.config.frontier_node_type_feed:
            node_embed *= 0.

        if not self.config.parent_action_feed:
            par_rule_embed *= 0.

        decoder_input = torch.cat([prev_action_embed, node_embed, par_rule_embed], dim=-1)

        h, c, ctx_vec = self.decoder(t,
                                     decoder_input,
                                     ctx, hist_h,
                                     h, c, parent_h)

        # (batch_size, decoder_hidden_state + encoder_hidden_dim)
        decoder_concat = torch.cat([h, ctx_vec], dim=-1)

        # (batch_size, rule_embed_dim)
        decoder_hidden_state_trans_rule = self.decoder_hidden_state_W_rule(h)
        decoder_hidden_state_trans_token = self.decoder_hidden_state_W_token(decoder_concat)
        decoder_hidden_state_trans_rule = F.tanh(decoder_hidden_state_trans_rule)
        decoder_hidden_state_trans_token = F.tanh(decoder_hidden_state_trans_token)

        # (batch_size, rule_num)
        rule_prob = self.rule_gen_softmax(decoder_hidden_state_trans_rule)

        # (batch_size, 2)
        gen_action_prob = self.terminal_gen_softmax(h)

        # (batch_size, target_vocab_size)
        vocab_prob = self.vocab_gen_softmax(decoder_hidden_state_trans_token)

        # (batch_size, query_length)
        copy_prob = self.src_ptr_net(ctx, decoder_concat.unsqueeze(1)).squeeze(1)

        return h, c, \
               rule_prob, gen_action_prob, vocab_prob, copy_prob

    def forward_train(self, trees, queries,
                      tgt_node_seq, tgt_action_seq, tgt_par_rule_seq, tgt_par_t_seq, tgt_action_seq_type):

        # (batch_size, encoder_hidden_dim), (batch_size, encoder_hidden_dim)
        # (batch_size, query_length, encoder_hidden_dim)
        h, c, ctx = self.forward_encode(trees, queries)

        # prepare output for teacher forced decoding
        # (batch_size, max_example_action_num, node_embed_dim)
       
        tgt_node_embed = self.node_embedding[tgt_node_seq]

        rule_embedding_W = self.rule_gen_softmax.weight
        vocab_embedding_W = self.vocab_gen_softmax.weight

        # (batch_size, max_example_action_num, rule_embed_dim)
        tgt_action_seq_embed = ifcond((tgt_action_seq[:, :, 0] > 0).unsqueeze(2),
                                      rule_embedding_W[tgt_action_seq[:, :, 0]],
                                      vocab_embedding_W[tgt_action_seq[:, :, 1]])

        # parent rule application embeddings
        # (batch_size, max_example_action_num, rule_embed_dim)
        tgt_par_rule_embed = Var(
            zeros(tgt_par_rule_seq.shape[0], tgt_par_rule_seq.shape[1], self.config.rule_embed_dim, cuda=h.is_cuda))
        tgt_par_rule_embed[:, 1:, :] = rule_embedding_W[tgt_par_rule_seq[:, 1:]]

        # (batch_size, max_example_action_num, rule_embed_dim)
        tgt_action_seq_embed_tm1 = Var(zeros_like(tgt_action_seq_embed, h.is_cuda))
        tgt_action_seq_embed_tm1[:, 1:, :] = tgt_action_seq_embed[:, :-1, :]

        h = h if self.thought else init_var(h.size()[0], self.config.decoder_hidden_dim,
                                            cuda=h.is_cuda, scale=0.1, training=self.training)
        c = c if self.thought else init_var(c.size()[0], self.config.decoder_hidden_dim,
                                            cuda=c.is_cuda, scale=0.1, training=self.training)

        # (batch_size, max_example_action_num, rule_embed_dim + node_embed_dim + rule_embed_dim)
        decoder_input = torch.cat([tgt_action_seq_embed_tm1, tgt_node_embed, tgt_par_rule_embed], dim=-1)

        # (batch_size, max_example_action_num, decoder_hidden_dim),
        # (batch_size, max_example_action_num, encoder_hidden_dim)
        decoder_hidden_states, ctx_vectors = self.decoder.forward_train(decoder_input,
                                                                        ctx, h, c, tgt_par_t_seq)

        # (batch_size, max_example_action_num, decoder_hidden_state + encoder_hidden_dim)
        decoder_concat = torch.cat([decoder_hidden_states, ctx_vectors], dim=-1)

        # (batch_size, max_example_action_num, rule_embed_dim)
        decoder_hidden_state_trans_rule = self.decoder_hidden_state_W_rule(decoder_hidden_states)
        decoder_hidden_state_trans_token = self.decoder_hidden_state_W_token(decoder_concat)

        decoder_hidden_state_trans_rule = F.tanh(decoder_hidden_state_trans_rule)
        decoder_hidden_state_trans_token = F.tanh(decoder_hidden_state_trans_token)

        # (batch_size, max_example_action_num, rule_num)
        rule_predict = self.rule_gen_softmax.forward_train(decoder_hidden_state_trans_rule)

        # (batch_size, max_example_action_num, 2)
        terminal_gen_action_prob = self.terminal_gen_softmax.forward_train(decoder_hidden_states)

        # (batch_size, max_example_action_num, target_vocab_size)
        vocab_predict = self.vocab_gen_softmax.forward_train(decoder_hidden_state_trans_token)

        # (batch_size, max_example_action_num, query_length)
        copy_prob = self.src_ptr_net.forward_train(ctx, decoder_concat)

        # (batch_size, max_example_action_num)
        rule_tgt_prob = rule_predict.gather(2, Var(tgt_action_seq[:, :, 0].unsqueeze(2), requires_grad=False)).squeeze(2)

        # (batch_size, max_example_action_num)
        vocab_tgt_prob = vocab_predict.gather(2, Var(tgt_action_seq[:, :, 1].unsqueeze(2), requires_grad=False)).squeeze(2)

        # (batch_size, max_example_action_num)
        copy_tgt_prob = copy_prob.gather(2, Var(tgt_action_seq[:, :, 2].unsqueeze(2), requires_grad=False)).squeeze(2)

        # (batch_size, max_example_action_num)
        tgt_action_seq_type = Var(tgt_action_seq_type.float(), requires_grad=False)

        tgt_prob = tgt_action_seq_type[:, :, 0] * rule_tgt_prob + \
                   tgt_action_seq_type[:, :, 1] * (terminal_gen_action_prob[:, :, 0] + vocab_tgt_prob) + \
                   tgt_action_seq_type[:, :, 2] * (terminal_gen_action_prob[:, :, 1] + copy_tgt_prob)

        # nll loss
        loss = torch.neg(torch.sum(tgt_prob))
        return loss
