import torch
from torch.autograd import Variable as Var
import torch.nn as nn


def ifcond(cond, x_1, x_2):
    # ensure boolean
    cond = cond.byte().float()
    # check is it Tensor or Variable
    if not hasattr(cond, "backward"):
        cond = Var(cond, requires_grad=False)
    return (cond * x_1) + ((1-cond) * x_2)


def index_select_if_none(input, dim, index, ifnone):
    input_max = input.data.shape[dim]
    index_mask = ((index > 0) * (index < input_max)).eq(0)
    index.masked_fill_(index_mask, input_max)
    input = torch.cat([input, ifnone], dim=0)
    return input[index]


def from_list(ls, cuda):
    tensor = torch.Tensor(ls)
    if cuda:
        tensor = tensor.cuda()
    return tensor


def from_long_list(ls, cuda):
    tensor = torch.LongTensor(ls)
    if cuda:
        tensor = tensor.cuda()
    return tensor


def zeros(*shape, cuda=False):
    t = torch.FloatTensor(*shape).zero_()
    if cuda:
        t = t.cuda()
    return t


def zeros_var(*shape, cuda=False):
    t = torch.FloatTensor(*shape).zero_()
    if cuda:
        t = t.cuda()
    return Var(t, requires_grad=False)


def normal_var(*shape, cuda=False, scale=1.0):
    t = torch.FloatTensor(*shape).normal_(0.0, scale)
    if cuda:
        t = t.cuda()
    return Var(t, requires_grad=False)


def init_var(*shape, cuda=False, scale=1.0, training=True):
    if training:
        return normal_var(*shape, cuda=cuda, scale=scale)
    else:
        return zeros_var(*shape, cuda=cuda)


def zeros_like(tensor, cuda):
    if hasattr(tensor, "backward"):
        shape = tensor.data.shape
    else:
        shape = tensor.shape
    return zeros(*shape, cuda=cuda)


def add_padding_and_stack(tensors, cuda, dim=0, max_length=None):
    if max_length is None:
        max_length = max([t.data.shape[dim] for t in tensors])

    result = []
    for tensor in tensors:
        sh = list(tensor.data.shape)
        sh[dim] = max_length-sh[dim]
        assert sh[dim] >= 0

        if sh[dim] > 0:
            padding = Var(zeros(*sh, cuda=cuda))
            tensor = torch.cat([tensor, padding], dim=dim)
        result.append(tensor)

    return torch.stack(result)


def add_padding_and_cat(tensors, cuda, dim=1, cat_dim=0, max_length=None):
    if max_length is None:
        max_length = max([t.data.shape[dim] for t in tensors])

    result = []
    for tensor in tensors:
        sh = list(tensor.data.shape)
        sh[dim] = max_length-sh[dim]
        assert sh[dim] >= 0

        if sh[dim] > 0:
            padding = Var(zeros(*sh, cuda=cuda))
            tensor = torch.cat([tensor, padding], dim=dim)
        result.append(tensor)

    return torch.cat(result, dim=cat_dim)


def parameter_init_zero(*dims):
    return nn.Parameter(torch.FloatTensor(*dims).zero_())


def dropout_matrix(*dims, p=0.2, train=True, cuda=False):
    assert p <= 1.0 and p >= 0.0, "Invalid probability: {}".format(p)
    prob = 1-p
    # all 0.8, ok for evaluation
    d = Var(torch.FloatTensor(*dims).fill_(prob))
    if train:
        # all 1 or 0
        d = d.bernoulli()
    if cuda:
        d = d.cuda()
    return d


def device_map_location(cuda):
    if cuda:
        return lambda storage, loc: storage.cuda()
    else:
        return lambda storage, loc: storage


def reverse(tensor, dim=0):
    length = tensor.size()[dim]
    idx = Var(torch.arange(length-1, -1, -1).long())
    if tensor.is_cuda:
        idx = idx.cuda()

    return torch.index_select(tensor, dim, idx)




