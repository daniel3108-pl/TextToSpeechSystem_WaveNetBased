import torch
import torch.functional as F
import torch.nn as nn
import torchtext as tt


class DecoderNetwork (nn.Module):
    def __init__(self) -> None:
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        pass



