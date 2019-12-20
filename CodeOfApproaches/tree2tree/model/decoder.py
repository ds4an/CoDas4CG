import torch
import torch.nn as nn
import torch.nn.init as init
import torch.nn.functional as F

from model.utils import *
from lang.grammar import Grammar
from lang.astnode import DecodeTree


class CondAttLSTM(nn.Module):
    def __init__(self, input_dim,
                 output_dim,
                 context_dim,
                 att_hidden_dim,
                 config):

        super(CondAttLSTM, self).__init__()

        self.output_dim = output_dim
        self.context_dim = context_dim
        self.input_dim = input_dim

        # one W for all x
        self.W_ix = nn.Linear(input_dim, output_dim)
        init.xavier_uniform(self.W_ix.weight)
        self.W_ix.bias = nn.Parameter(torch.FloatTensor(output_dim).zero_())

        # input gate
        self.W_i = nn.Linear(output_dim + context_dim + output_dim + output_dim, output_dim, bias=False)
        init.orthogonal(self.W_i.weight)

        # forget gate
        self.W_fx = nn.Linear(input_dim, output_dim)
        init.xavier_uniform(self.W_fx.weight)
        self.W_fx.bias = nn.Parameter(torch.FloatTensor(output_dim).fill_(1.0))

        self.W_f = nn.Linear(output_dim + context_dim + output_dim + output_dim, output_dim, bias=False)
        init.orthogonal(self.W_f.weight)

        # memory cell new value
        self.W_cx = nn.Linear(input_dim, output_dim)
        init.xavier_uniform(self.W_cx.weight)
        self.W_cx.bias = nn.Parameter(torch.FloatTensor(output_dim).zero_())

        self.W_c = nn.Linear(output_dim + context_dim + output_dim + output_dim, output_dim, bias=False)
        init.orthogonal(self.W_c.weight)

        # output gate
        self.W_ox = nn.Linear(input_dim, output_dim)
        init.xavier_uniform(self.W_ox.weight)
        self.W_ox.bias = nn.Parameter(torch.FloatTensor(output_dim).zero_())

        self.W_o = nn.Linear(output_dim + context_dim + output_dim + output_dim, output_dim, bias=False)
        init.orthogonal(self.W_o.weight)

        # attention layer
        self.att_ctx = nn.Linear(context_dim, att_hidden_dim)
        init.xavier_uniform(self.att_ctx.weight)
        self.att_ctx.bias = nn.Parameter(torch.FloatTensor(att_hidden_dim).zero_())
        self.att_h = nn.Linear(output_dim, att_hidden_dim, bias=False)
        init.xavier_uniform(self.att_h.weight)
        self.att = nn.Linear(att_hidden_dim, 1)
        init.xavier_uniform(self.att.weight)
        self.att.bias = nn.Parameter(torch.FloatTensor(1).zero_())

        # attention over history
        self.h_att_hist = nn.Linear(output_dim, att_hidden_dim)
        init.xavier_uniform(self.h_att_hist.weight)
        self.h_att_hist.bias = nn.Parameter(torch.FloatTensor(att_hidden_dim).zero_())
        self.h_att_h = nn.Linear(output_dim, att_hidden_dim, bias=False)
        init.xavier_uniform(self.h_att_h.weight)
        self.h_att = nn.Linear(att_hidden_dim, 1)
        init.xavier_uniform(self.h_att.weight)
        self.h_att.bias = nn.Parameter(torch.FloatTensor(1).zero_())

        self.softmax = nn.Softmax(dim=-1);

        self.parent_hidden_state_feed = config.parent_hidden_state_feed
        self.dropout = config.decoder_dropout
        self.config = config

    def before_eval(self):
        self.W_ifco_x = nn.Linear(self.input_dim, 4*self.output_dim)
        self.W_ifco_x.weight = nn.Parameter(torch.cat([
            self.W_ix.weight.clone(),
            self.W_fx.weight.clone(),
            self.W_cx.weight.clone(),
            self.W_ox.weight.clone()
        ], dim=0).data)
        self.W_ifco_x.bias = nn.Parameter(torch.cat([
            self.W_ix.bias.clone(),
            self.W_fx.bias.clone(),
            self.W_cx.bias.clone(),
            self.W_ox.bias.clone()
        ]).data)

    def after_eval(self):
        del self.W_ifco_x

    # one time step at the time
    def forward(self, t, x, context, hist_h, h, c, parent_h):
        # dropout normalization
        x *= 1.0-self.dropout
        dr_H = dropout_matrix(4, p=self.dropout, train=False, cuda=h.is_cuda)
        # (batch_size, 4*output_dim)
        #x_ifoc = self.W_ifco_x(x)
        xi, xf, xo, xc = self.W_ix(x), self.W_fx(x), self.W_ox(x), self.W_cx(x) #torch.split(x_ifoc, self.output_dim, dim=-1)

        return self.forward_node(t,
                                 xi, xf, xo, xc,
                                 context, hist_h,
                                 h, c, parent_h,
                                 dr_H)

    def forward_node(self, t,
                     xi, xf, xo, xc,
                     context, hist_h,
                     h, c, par_h,
                     dr_H):
        # (batch_size, context_size, att_layer1_dim)
        context_att_trans = self.att_ctx(context)

        # (batch_size, att_layer1_dim)
        h_att_trans = self.att_h(h)

        # (batch_size, context_size, att_layer1_dim)
        att_hidden = F.tanh(context_att_trans + h_att_trans[:, None])

        # (batch_size, context_size)
        att_raw = self.att(att_hidden).squeeze(2)

        # (batch_size, context_size)
        ctx_att = self.softmax(att_raw)
        assert ctx_att[0].sum()[0]

        # (batch_size, context_dim)
        ctx_vec = (context * ctx_att.unsqueeze(2)).sum(dim=1)

        def _attention_over_history():
            # hist_h - (batch_size, seq_len, output_dim)
            # (batch_size, seq_len, att_hidden_dim)
            hist_h_att_trans = self.h_att_hist(hist_h)

            # h - (batch_size, output_dim)
            # (batch_size, att_hidden_dim)
            h_hatt_trans = self.h_att_h(h)

            # (batch_size, seq_len, att_hidden_dim)
            hatt_hidden = F.tanh(hist_h_att_trans + h_hatt_trans[:, None])

            # (batch_size, seq_len)
            hatt_raw = self.h_att(hatt_hidden).squeeze(2)

            # (batch_size, seq_len)
            h_att_weights = self.softmax(hatt_raw)

            # (batch_size, output_dim)
            _h_ctx_vec = torch.sum(hist_h * h_att_weights.unsqueeze(2), dim=1)

            return _h_ctx_vec

        if t and self.config.tree_attention:
            h_ctx_vec = _attention_over_history()
        else:
            h_ctx_vec = Var(zeros_like(h, h.is_cuda))

        if not self.config.parent_hidden_state_feed:
            par_h *= 0.

        # (batch_size, output_dim + context_dim + output_dim + output_dim)
        h_comb_i = torch.cat([h*dr_H[0], ctx_vec, par_h, h_ctx_vec], dim=-1)
        h_comb_f = torch.cat([h*dr_H[1], ctx_vec, par_h, h_ctx_vec], dim=-1)
        h_comb_c = torch.cat([h*dr_H[2], ctx_vec, par_h, h_ctx_vec], dim=-1)
        h_comb_o = torch.cat([h*dr_H[3], ctx_vec, par_h, h_ctx_vec], dim=-1)

        # (batch_size, output_dim)
        i = F.sigmoid(xi + self.W_i(h_comb_i))
        f = F.sigmoid(xf + self.W_f(h_comb_f))
        c = f * c + i * F.tanh(xc + self.W_c(h_comb_c))
        o = F.sigmoid(xo + self.W_o(h_comb_o))

        h = o * F.tanh(c)

        return h, c, ctx_vec

    # all inputs at the time (teacher forcing)
    def forward_train(self, X, context, h, c, parent_t):
        length = X.shape[1]
        # (4, batch_size, input_dim)
        dr_X = dropout_matrix(4, X.shape[0], 1, X.shape[2], p=self.dropout, cuda=h.is_cuda)
        dr_H = dropout_matrix(4, X.shape[0], self.output_dim, p=self.dropout, cuda=h.is_cuda)
        # calculate all X dense transformation at once
        # (batch_size, max_sequence_length, output_dim)
        Xi, Xf, Xo, Xc = self.W_ix(X*dr_X[0]), self.W_fx(X*dr_X[1]), self.W_ox(X*dr_X[2]), self.W_cx(X*dr_X[3])
        # (batch_size, max_sequence_length, decoder_hidden_dim)
        output_h = None
        # (batch_size, max_sequence_length, encoder_hidden_dim)
        output_ctx = []

        for t in range(length):
            # extract parent node from history
            if t and self.parent_hidden_state_feed:
                # gather require index to have the same size as input
                # except the gathering dimension
                # (batch_size, 1, hidden_dim)
                index = Var(parent_t[:, t][:, None, None].
                            expand(-1, -1, self.output_dim), requires_grad=False)
                # (batch_size, hidden_dim)
                par_h = torch.gather(output_h, 1, index).squeeze(1)
            else:
                par_h = Var(zeros_like(h, h.is_cuda))

            xi, xf, xo, xc = Xi[:, t, :].squeeze(1), \
                             Xf[:, t, :].squeeze(1), \
                             Xo[:, t, :].squeeze(1), \
                             Xc[:, t, :].squeeze(1)

            h, c, ctx_vec = self.forward_node(t,
                                              xi, xf, xo, xc,
                                              context, output_h,
                                              h, c, par_h,
                                              dr_H)
            if output_h is None:
                output_h = h[:, None]
            else:
                output_h = torch.cat([output_h, h[:, None]], dim=1)
            output_ctx.append(ctx_vec[:, None])

        return output_h, torch.cat(output_ctx, dim=1)


class PointerNet(nn.Module):
    def __init__(self, config):
        super(PointerNet, self).__init__()

        self.dense1_input = nn.Linear(config.encoder_hidden_dim, config.ptrnet_hidden_dim)
        init.xavier_uniform(self.dense1_input.weight)
        self.dense1_input.bias = parameter_init_zero(config.ptrnet_hidden_dim)

        self.dense1_h = nn.Linear(config.decoder_hidden_dim + config.encoder_hidden_dim, config.ptrnet_hidden_dim)
        init.xavier_uniform(self.dense1_h.weight)
        self.dense1_h.bias = parameter_init_zero(config.ptrnet_hidden_dim)

        self.dense2 = nn.Linear(config.ptrnet_hidden_dim, 1)
        init.xavier_uniform(self.dense2.weight)
        self.dense2.bias = parameter_init_zero(1)

        self.log_softmax = nn.LogSoftmax(dim=-1)
        self.softmax = nn.Softmax(dim=-1);

    def forward_scores(self, ctx, decoder_states):
        # (batch_size, query_length, ptrnet_hidden_dim)
        ctx_trans = self.dense1_input(ctx)

        # (batch_size, max_decode_step, ptrnet_hidden_dim)
        decoder_trans = self.dense1_h(decoder_states)

        # (batch_size, 1, query_length, ptrnet_hidden_dim)
        ctx_trans = ctx_trans.unsqueeze(1)

        # (batch_size, max_decode_step, 1, ptrnet_hidden_dim)
        decoder_trans = decoder_trans.unsqueeze(2)

        # (batch_size, max_decode_step, query_length, ptr_net_hidden_dim)
        dense1_trans = F.tanh(ctx_trans + decoder_trans)

        # (batch_size,  max_decode_step, query_length, 1)
        scores = self.dense2(dense1_trans)

        # (batch_size,  max_decode_step, query_length)
        return scores.squeeze(3)

    def forward(self, ctx, decoder_states):
        # (batch_size,  max_decode_step, query_length)
        scores = self.forward_scores(ctx, decoder_states)

        # (batch_size,  max_decode_step, query_length)
        scores = self.softmax(scores)

        # (batch_size,  max_decode_step, query_length)
        return scores

    def forward_train(self, ctx, decoder_states):
        # (batch_size,  max_decode_step, query_length)
        scores = self.forward_scores(ctx, decoder_states)

        # (batch_size,  max_decode_step, query_length)
        scores = self.log_softmax(scores)

        # (batch_size,  max_decode_step, query_length)
        return scores

