"""Moduł z funkcjami pomocniczymi związanymi z matematyką"""

from __future__ import annotations

import torchaudio


def to_mel_spect(waveform, sample_rate, n_fft=1024, win_length=None, hop_length=512, n_mels=128):
    """Przekształca tablicę próbek dźwięku do postaci Mel'owej

    :param waveform:
    :param sample_rate:
    :param n_fft:
    :param win_length:
    :param hop_length:
    :param n_mels:
    :return:
    """
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
    return mel_spectr(waveform)
