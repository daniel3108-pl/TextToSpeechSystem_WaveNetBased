import torch
import torch.functional as F
import torch.nn as nn
import torchtext as tt


class EncoderNetwork (nn.Module):
    def __init__(self, batch_size, hidden_dim, lstm_layers, input_size) -> None:
        super(EncoderNetwork, self).__init__()

        # Hyperparameters
        self.batch_size = batch_size
        self.hidden_dim = hidden_dim
        self.LSTM_layers = lstm_layers
        self.input_size = input_size

        self.dropout = nn.Dropout(0.5)
        self.embeding = nn.Embedding(self.input_size, self.hidden_dim, padding_idx=0)
        self.lstm = nn.LSTM(input_size=self.hidden_dim, hidden_size=self.hidden_dim, num_layers=self.LSTM_layers, batch_first=True)
        self.fc1 = nn.Linear(in_features=self.hidden_dim, out_features=self.hidden_dim*2)
        self.fc2 = nn.Linear(self.hidden_dim*2, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Hidden and cell state definion
        h = torch.zeros((self.LSTM_layers, x.size(0), self.hidden_dim))
        c = torch.zeros((self.LSTM_layers, x.size(0), self.hidden_dim))

        # Initialization fo hidden and cell states
        torch.nn.init.xavier_normal_(h)
        torch.nn.init.xavier_normal_(c)

        # Each sequence "x" is passed through an embedding layer
        out = self.embedding(x)
        # Feed LSTMs
        out, (hidden, cell) = self.lstm(out, (h,c))
        out = self.dropout(out)
        # The last hidden state is taken
        out = torch.relu_(self.fc1(out[:,-1,:]))
        out = self.dropout(out)
        out = torch.sigmoid(self.fc2(out))

        return out



