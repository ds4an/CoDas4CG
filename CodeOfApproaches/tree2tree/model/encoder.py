import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init
from torch.autograd import Variable as Var

from model.utils import *


class LSTM(nn.Module):
    def __init__(self, in_dim, out_dim, p_dropout=0.0):
        super().__init__()

        self.input_dim = in_dim
        self.output_dim = out_dim
        self.dropout = p_dropout

        self.W_i = nn.Linear(in_dim, out_dim)
        init.xavier_uniform(self.W_i.weight)
        self.W_i.bias = nn.Parameter(torch.FloatTensor(out_dim).zero_())
        self.U_i = nn.Linear(out_dim, out_dim, bias=False)
        init.orthogonal(self.U_i.weight)

        self.W_f = nn.Linear(in_dim, out_dim)
        init.xavier_uniform(self.W_f.weight)
        self.W_f.bias = nn.Parameter(torch.FloatTensor(out_dim).fill_(1.0))
        self.U_f = nn.Linear(out_dim, out_dim)
        init.orthogonal(self.U_f.weight)

        self.W_c = nn.Linear(in_dim, out_dim)
        init.xavier_uniform(self.W_c.weight)
        self.W_c.bias = nn.Parameter(torch.FloatTensor(out_dim).fill_(0.0))
        self.U_c = nn.Linear(out_dim, out_dim)
        init.orthogonal(self.U_c.weight)

        self.W_o = nn.Linear(in_dim, out_dim)
        init.xavier_uniform(self.W_o.weight)
        self.W_o.bias = nn.Parameter(torch.FloatTensor(out_dim).fill_(0.0))
        self.U_o = nn.Linear(out_dim, out_dim)
        init.orthogonal(self.U_o.weight)

    def forward_node(self, xi, xf, xo, xc, h_prev, c_prev, dr_H):
        i = F.sigmoid(xi + self.U_i(h_prev * dr_H[0]))
        f = F.sigmoid(xi + self.U_f(h_prev * dr_H[1]))
        c = f * c_prev + i * F.tanh(xc + self.U_c(h_prev * dr_H[2]))
        o = F.sigmoid(xo + self.U_o(h_prev * dr_H[3]))
        h = o * F.tanh(c)
        return h, c

    def forward(self, X):
        batch_size = X.size()[0]
        length = X.size()[1]
        # (4, batch_size, input_dim)
        dr_X = dropout_matrix(4, batch_size, 1, self.input_dim, train=self.training, cuda=X.is_cuda, p=self.dropout)
        # (4, batch_size, output_dim)
        dr_H = dropout_matrix(4, batch_size, self.output_dim, train=self.training, cuda=X.is_cuda, p=self.dropout)

        Xi = self.W_i(X * dr_X[0])
        Xf = self.W_f(X * dr_X[1])
        Xc = self.W_c(X * dr_X[2])
        Xo = self.W_o(X * dr_X[3])

        h = init_var(batch_size, self.output_dim, scale=0.1, cuda=X.is_cuda, training=self.training)
        c = init_var(batch_size, self.output_dim, scale=0.1, cuda=X.is_cuda, training=self.training)
        h_hist = []
        c_hist = []
        for t in range(length):
            xi, xf, xo, xc = Xi[:, t, :].squeeze(1), \
                             Xf[:, t, :].squeeze(1), \
                             Xo[:, t, :].squeeze(1), \
                             Xc[:, t, :].squeeze(1)

            h, c = self.forward_node(xi, xf, xo, xc,
                                     h, c, dr_H)
            h_hist.append(h)
            c_hist.append(c)

        return torch.stack(h_hist, dim=1), torch.stack(c_hist, dim=1)


class BiLSTM(nn.Module):
    def __init__(self, in_dim, out_dim, p_dropout=0.0):
        super().__init__()

        self.input_dim = in_dim
        self.output_dim = out_dim
        self.dropout = p_dropout

        self.forward_lstm = LSTM(in_dim, int(out_dim/2), p_dropout)
        self.backward_lstm = LSTM(in_dim, int(out_dim/2), p_dropout)

    def forward(self, X):
        h_forward, c_forward = self.forward_lstm(X)
        h_backward, c_backward = self.backward_lstm(reverse(X, 1))

        h_hist = torch.cat([h_forward, reverse(h_backward, 1)], dim=-1)
        c_hist = torch.cat([c_forward, reverse(c_backward, 1)], dim=-1)

        return h_hist, c_hist


class ChildSumTreeLSTM(nn.Module):
    def __init__(self, in_dim, mem_dim, p_dropout=0.0):
        super().__init__()

        self.in_dim = in_dim
        self.mem_dim = mem_dim
        self.dropout = p_dropout

        # W_x
        self.ix = nn.Linear(self.in_dim, self.mem_dim)
        init.xavier_uniform(self.ix.weight)
        self.ix.bias = nn.Parameter(torch.FloatTensor(self.mem_dim).zero_())

        self.ox = nn.Linear(self.in_dim, self.mem_dim)
        init.xavier_uniform(self.ox.weight)
        self.ox.bias = nn.Parameter(torch.FloatTensor(self.mem_dim).zero_())

        self.ux = nn.Linear(self.in_dim, self.mem_dim)
        init.xavier_uniform(self.ux.weight)
        self.ux.bias = nn.Parameter(torch.FloatTensor(self.mem_dim).zero_())

        self.fx = nn.Linear(self.in_dim, self.mem_dim)
        init.xavier_uniform(self.fx.weight)
        self.fb = nn.Parameter(torch.FloatTensor(self.mem_dim).fill_(1.0))

        # W_h
        self.ih = nn.Linear(self.mem_dim, self.mem_dim, bias=False)
        init.orthogonal(self.ih.weight)

        self.oh = nn.Linear(self.mem_dim, self.mem_dim, bias=False)
        init.orthogonal(self.oh.weight)

        self.uh = nn.Linear(self.mem_dim, self.mem_dim, bias=False)
        init.orthogonal(self.uh.weight)

        self.fh = nn.Linear(self.mem_dim, self.mem_dim, bias=False)
        init.orthogonal(self.fh.weight)

    def node_forward(self, xi, xf, xo, xu, child_c, child_h, dr_H):
        # (1, mem_dim)
        child_h_sum = torch.sum(child_h, dim=0, keepdim=True)

        i = F.sigmoid(xi + self.ih(child_h_sum * dr_H[0]))
        o = F.sigmoid(xo + self.oh(child_h_sum * dr_H[1]))
        u = F.tanh(xu + self.uh(child_h_sum * dr_H[2]))

        f = F.sigmoid(
            self.fh(child_h * dr_H[3].unsqueeze(0)) +
            xf.repeat(len(child_h), 1) +
            self.fb
        )
        # (1, mem_dim)
        fc = torch.sum(f * child_c, dim=0, keepdim=True)

        c = u * i + fc
        h = torch.mul(o, F.tanh(c))
        return c, h

    def forward_inner(self, tree, Xi, Xf, Xu, Xo, dr_H):
        _ = [self.forward_inner(tree.children[idx], Xi, Xf, Xu, Xo, dr_H) for idx in range(tree.num_children)]

        if tree.num_children == 0:
            # (1, mem_dim)
            child_c = init_var(1, self.mem_dim, cuda=Xi.is_cuda, scale=0.1, training=self.training)
            child_h = init_var(1, self.mem_dim, cuda=Xi.is_cuda, scale=0.1, training=self.training)
        else:
            # (k_children, mem_dim)
            child_c, child_h = zip(*map(lambda x: x.state, tree.children))
            child_c, child_h = torch.cat(child_c, dim=0), torch.cat(child_h, dim=0)

        # (1, mem_dim)
        xi, xf, xo, xu = Xi[tree.idx, :], \
                         Xf[tree.idx, :], \
                         Xo[tree.idx, :], \
                         Xu[tree.idx, :]

        tree.state = self.node_forward(xi, xf, xo, xu, child_c, child_h, dr_H)
        return tree.state

    def forward(self, tree, X):
        dr_X = dropout_matrix(4, 1, self.in_dim, train=self.training, cuda=X.is_cuda, p=self.dropout)
        dr_H = dropout_matrix(4, self.mem_dim, train=self.training, cuda=X.is_cuda, p=self.dropout)

        Xi = self.ix(X * dr_X[0])
        Xf = self.fx(X * dr_X[1])
        Xu = self.ux(X * dr_X[2])
        Xo = self.ox(X * dr_X[3])

        self.forward_inner(tree, Xi, Xf, Xu, Xo, dr_H)
        return tree.state[1], \
               tree.state[0], \
               torch.stack([t.state[1] for t in tree.data()]).squeeze(1)


class EncoderLSTMWrapper(nn.Module):
    def __init__(self, config):
        super().__init__()

        self.config = config

        if self.config.encoder == 'recursive-lstm':
            self.encoder = ChildSumTreeLSTM(config.word_embed_dim, config.encoder_hidden_dim,
                                            config.encoder_dropout)
        elif self.config.encoder == 'bi-lstm':
            hidden_dim = int(config.encoder_hidden_dim/2)
            self.hidden_dim = hidden_dim
            # http://pytorch.org/docs/master/nn.html#torch.nn.LSTM
            self.encoder = nn.LSTM(config.word_embed_dim, hidden_dim, 1, batch_first=True,
                                   dropout=config.encoder_dropout, bidirectional=True)
            self.init_bilstm(hidden_dim)

        elif self.config.encoder == 'bi-lstm-dropout':
            assert config.encoder_dropout > 0.0, "Custom LSTM implementation designed specially to use with " \
                                         "dropout. Use bi-lstm instead."
            self.encoder = BiLSTM(config.word_embed_dim, config.encoder_hidden_dim, config.encoder_dropout)
        else:
            raise Exception("Unknown encoder type!")

    def init_bilstm(self, hidden_dim):
        init.xavier_uniform(self.encoder.weight_ih_l0)
        init.xavier_uniform(self.encoder.weight_ih_l0_reverse)
        init.orthogonal(self.encoder.weight_hh_l0)
        init.orthogonal(self.encoder.weight_hh_l0_reverse)

        bias = self.init_lstm_bias(self.encoder.bias_ih_l0, hidden_dim)
        self.encoder.bias_ih_l0 = nn.Parameter(bias.clone())
        self.encoder.bias_hh_l0 = nn.Parameter(bias.clone())
        self.encoder.bias_ih_l0_reverse = nn.Parameter(bias.clone())
        self.encoder.bias_hh_l0_reverse = nn.Parameter(bias.clone())

    def init_lstm_bias(self, bias, hidden_dim):
        bias = bias.data.fill_(0.0)
        # forget gate
        bias[hidden_dim:2 * hidden_dim] = 1.0
        return bias

    def forward(self, trees, inputs):
        if self.config.encoder == 'recursive-lstm':
            return self.forward_recursive(trees, inputs)
        elif self.config.encoder == 'bi-lstm':
            return self.forward_lstm(inputs)
        elif self.config.encoder == 'bi-lstm-dropout':
            return self.forward_lstm_dropout(inputs)

    def forward_lstm(self, inputs):
        # (2, batch_size, encoder_hidden_dim)
        h0 = init_var(2, inputs.size[0], self.hidden_dim,
                      cuda=inputs.is_cuda, scale=0.1, training=self.training)
        c0 = init_var(2, inputs.size[0], self.hidden_dim,
                      cuda=inputs.is_cuda, scale=0.1, training=self.training)
        ctx, hc = self.encoder(inputs, (h0, c0))
        assert ctx.data.shape[0] == inputs.data.shape[0]
        assert ctx.data.shape[2] == self.config.encoder_hidden_dim
        h, c = hc
        # (batch_size, encoder_hidden_dim)
        h = h.permute(1, 0, 2).contiguous().view(-1, self.config.encoder_hidden_dim)
        c = c.permute(1, 0, 2).contiguous().view(-1, self.config.encoder_hidden_dim)

        return h, c, ctx

    def forward_lstm_dropout(self, inputs):
        h_hist, c_hist = self.encoder(inputs)
        h, c = h_hist[:, -1, :].squeeze(1), c_hist[:, -1, :].squeeze(1)
        return h, c, h_hist

    def forward_recursive(self, trees, inputs):
        # (batch_size, encoder_hidden_dim)
        h = []
        c = []
        # (batch_size, query_length, encoder_hidden_dim)
        ctx = []
        # encoder can process only one tree at the time
        for tree, input in zip(trees, inputs):
            # (1, hidden_dim), (1, hidden_dim)
            # (1, seq_len, hidden_dim)
            h1, c1, ctx1 = self.encoder(tree, input)
            h.append(h1)
            c.append(c1)
            ctx.append(ctx1)

        # all ctx must be one length to be stacked
        ctx = add_padding_and_stack(ctx, inputs.is_cuda)
        h = torch.cat(h, dim=0)
        c = torch.cat(c, dim=0)

        return h, c, ctx

