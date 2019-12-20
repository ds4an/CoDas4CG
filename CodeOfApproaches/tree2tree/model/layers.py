import torch.nn as nn
import torch.nn.init as init


class LogSoftmaxDense(nn.Linear):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.softmax = nn.Softmax(dim=-1)
        self.log_softmax = nn.LogSoftmax(dim=-1)

    def forward(self, input):
        o = super().forward(input)
        return self.softmax(o)

    def forward_train(self, input):
        o = super().forward(input)
        return self.log_softmax(o)
