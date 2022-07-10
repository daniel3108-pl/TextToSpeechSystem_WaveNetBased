from typing import *

from utils import Monad
from .text_helpers import remove_symbols, remove_empty_chars

__punctuation = '!\'(),.:;? '
__special = '-'
__letters = 'abcdefghijklmnopqrstuvwxyz'

accepted_symbols = list(__letters) + list(__punctuation) + list(__special)


class TextPreprocessor:

    def __init__(self):
        pass

    def clean(self, text: str) -> Tuple[Dict, Dict]:
        return Monad.some(text) \
                    .map(str.lower) \
                    .map(str.strip) \
                    .map(lambda t: remove_symbols(t, accepted_symbols)) \
                    .map(remove_empty_chars) \
                    .unbind()

    def to_c2i_i2c(self, text: str) -> Tuple[Dict, Dict]:
        """Transformuje tekst to postaci słownika znak indeks, indeks znak
        :param text: tekst do transformacji
        :type text: str
        :return: Krotkę słowników char 2 index, index 2 char
        """
        char2idx = dict()
        idx2char = dict()

        i = 0
        for char in text:
            if char not in char2idx.keys():
                char2idx[char] = i
                idx2char[i] = char
                i+=1

        return char2idx, idx2char


class OneHotVectorSequencer:

    def __init__(self):
            pass

    def sequence_text(self, text: str) -> List[int]:
        seq = [[1 if char == s else 0 for s in accepted_symbols] for char in text]
        return seq

    def desequence_text(self, sequence: List[List[int]]) -> str:
        assert isinstance(sequence, list), "sequence has to be a list of int"
        return "".join([accepted_symbols[i] for char_arr in sequence for i, num in enumerate(char_arr) if num == 1])
