from typing import *

import torch
import torch.nn as nn
import torch.nn.functional as F


class EncoderNetwork (nn.Module):
    def __init__(self, params: Dict) -> None:
        super(EncoderNetwork, self).__init__()

        self.convs = nn.ModuleList()
        for _ in range(3):
            self.convs.append(
                nn.Sequential(
                    nn.Conv1d(params['embed_dim'],
                              params['embed_dim'],
                              kernel_size=params['kernel_size'],
                              stride=1,
                              padding=int((params['kernel_size'] - 1) / 2),
                              dilation=1),
                    nn.BatchNorm1d(params['embed_dim'])
                )
            )

        self.lstm = nn.LSTM(params['embed_dim'], int(params['embed_dim'] / 2), 1, batch_first=True, bidirectional=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        for conv in self.convs:
            x = F.dropout(F.relu(conv(x)), 0.5, training=True)





