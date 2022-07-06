from __future__ import  annotations

import matplotlib.pyplot as plt
import librosa
import torchaudio
from typing import *


T = TypeVar("T")
U = TypeVar("U")


class Monad(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value: object = value

    def flat_map(self, func: Callable[T, Monad[U]]) -> Monad[U]:
        return func(self.value)

    def map(self, func: Callable[T, U]) -> U:
        return func(self.value)

    @staticmethod
    def some(value: T):
        return Monad(value)

    def unbind(self) -> T:
        return self.value


def show_mel_spectrogram(waveform, sample_rate, n_fft=1024, win_length=None,
                         hop_length=512, n_mels=128, title="Mel spectrogram",
                         ylabel="Mel freq", xlabel="Frame"):

    mel_spectr = torchaudio.transforms.MelSpectrogram(
        sample_rate=sample_rate,
        n_fft=n_fft,
        win_length=win_length,
        hop_length=hop_length,
        center=True,
        pad_mode="reflect",
        power=2.0,
        norm='slaney',
        onesided=True,
        n_mels=n_mels,
        mel_scale="htk"
    )

    melspec = mel_spectr(waveform)
    fig, ax = plt.subplots(1, 1, figsize=(13,8))
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    im = ax.imshow(librosa.power_to_db(melspec[0]), origin="lower", aspect="auto")
    fig.colorbar(im, ax=ax)
    plt.show()




