"""Moduł z pomocniczymi funkcjami nieskategaryzowanymi do innych modułów
"""

from __future__ import annotations

import librosa
import matplotlib.pyplot as plt

from .math_utils import to_mel_spect


def is_int(val: str) -> bool:
    try:
        int(val)
        return True
    except ValueError as er:
        return False


def is_float(val: str) -> bool:
    try:
        float(val)
        return True
    except ValueError as er:
        return False


def show_mel_spectrogram(waveform, sample_rate, n_fft=1024, win_length=None,
                         hop_length=512, n_mels=128, title="Mel spectrogram",
                         ylabel="Mel freq", xlabel="Frame"):

    melspec = to_mel_spect(waveform, sample_rate, n_fft, win_length, hop_length, n_mels)
    fig, ax = plt.subplots(1, 1, figsize=(13,8))
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    im = ax.imshow(librosa.power_to_db(melspec[0]), origin="lower", aspect="auto")
    fig.colorbar(im, ax=ax)
    plt.show()






