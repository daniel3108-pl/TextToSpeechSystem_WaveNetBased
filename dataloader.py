from __future__ import annotations

import os

import pandas as pd
import torch
import torchaudio
from torch.utils.data import Dataset


class SpeechSamplesDataset(Dataset):
    """Klasa ulatwiajaca ladowanie zestwau plikow audio
    """
    def __init__(self, csv_file, root_dir, csv_sep="\t", transform=None, cuda=False):
        """Metoda inicializujaca klase zestawu danych

        :param csv_file: sciezka do pliku csv opisujacy zestaw danych tekstowych
        :param root_dir: sciezka bazowa zestawu danych
        :param csv_sep: separator pliku csv, np. ","  "\t"  "|"
        :param transform:
        :return: None
        """
        self.audio_frame = pd.read_csv(root_dir + csv_file, sep=csv_sep)
        self.root_dir = root_dir
        self.transform = transform
        if torch.cuda.is_available():
            self.__cuda = cuda
        else:
            self.__cuda = False

    def __len__(self):
        """Zwraca dlugosc zestawu danych
        """
        return self.audio_frame.shape[0]

    def __getitem__(self, idx):
        """Zwraca element o podanym indexie

        :param idx: indeks parametru
        :return: Dict z sample rate, tablia waveform oraz transkrypcja mowy z pliku audio
        :rtype: Dict[float, np.array, str]
        """
        if torch.is_tensor(idx):
            idx = idx.tolist()

        audio_name = os.path.join(self.root_dir,
                                  self.audio_frame.iloc[idx, 0]) + ".wav"
        waveform, samplerate = torchaudio.load(audio_name)

        if self.__cuda:
            waveform = waveform.to("cuda")

        transcription = self.audio_frame.iloc[idx, 1].lower()
        sample = {"samplerate": samplerate, "waveform": waveform, "transcription": transcription, "filepath": audio_name}

        if (self.transform):
            sample = self.transform(sample)

        return sample

    def to(self, device: str):
        """Ustawia czy dane maja trzmane w pamieci ram czy w pamieci GPU

        :param device: "cuda" lub "cpu",
        """
        if device == "cpu":
            self.__cuda = False
            return

        if device == "cuda" and torch.cuda.is_available():
            self.__cuda = True
        else:
            raise Exception("Cuda is not available")

    def train_test_split(self, train_size=0.8, test_size=0.2):
        """Dzieli zestaw na dane testowe i treningowe

        :param train_size: procent ile danych z calosci ma przypadac na dane treningowe
        :param test_size: procent ile danych z calosci ma przypada na dane testowe
        :return: tupple of train and test subsets
        """
        if train_size + test_size > 1:
            raise Exception("split sizes cannot be more than 100% in sum")

        train_size = int(len(self) * train_size)
        test_size = len(self) - train_size
        return torch.utils.data.random_split(self, [train_size, test_size])
