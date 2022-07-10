import torch.functional as F
import torch.nn as nn


class DecoderPrenet(nn.Module):
    def __init__(self, input_dim):
        super(DecoderPrenet, self).__init__()

    def forward(self, x):
        x = F.dropout(F.relu(), p=0.5, training=True)


class DecoderNetwork(nn.Module):
    def __init__(self, embeded_dim, hidden_dim, lstm_layers, out_dim, dropout):
        super(DecoderNetwork, self).__init__()

        self.out_dim = out_dim
        self.embeded_dim = embeded_dim
        self.hidden_dim = hidden_dim
        self.lstm_layers = lstm_layers
        self.dropout = dropout

        self.embedding = nn.Embedding(self.out_dim, self.embeded_dim)
        self.lstm = nn.LSTM(self.embeded_dim,
                            self.hidden_dim,
                            num_layers=self.lstm_layers,
                            dropout=self.dropout)
        self.linear = nn.Linear(hidden_dim, out_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, hid, cell):
        x = x.unsqueeze(0)
        embedded = self.dropout(self.embedding(x))
        out, (hid, cell) = self.lstm(embedded, (hid, cell))
        prediction = self.linear(out.squeeze(0))
        return prediction, hid, cell


