"""
Moduł odpowiedzialny za preprocessing tekstu oraz jego transformację do postaci czytelnej dla sieci neuronowcyh
"""

from typing import *

from utils.functional_utils import Monad
from utils.text_helpers import remove_symbols, remove_empty_chars

__punctuation = '!\'(),.:;? '
__special = '-'
__letters = 'abcdefghijklmnopqrstuvwxyz'

accepted_symbols = list(__letters) + list(__punctuation) + list(__special)
"""Akceptowane przez system symbole w wypowiedziach"""

class TextPreprocessor:
    """Klasa odpowiedzialna za preprocessing tekstu
    """
    def __init__(self):
        pass

    def clean(self, text: str) -> str:
        """Metoda czyszcząca podany tekst do postaci przyjmowanej przez OneHotVectorSequencer

        :type text: string
        :param text: teskt do czysczenia
        :return: wyczyszczony tekst
        """
        return Monad.some(text) \
                    .map(str.lower) \
                    .map(str.strip) \
                    .map(lambda t: remove_symbols(t, accepted_symbols)) \
                    .map(remove_empty_chars) \
                    .unbind()

    def to_c2i_i2c(self, text: str) -> Tuple[Dict, Dict]:
        """Transformuje tekst to postaci słownika znak indeks, indeks znak

        :param text: tekst do transformacji
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
    """Klasa odpowiedzialna za przekształcenie tekstu do postaci sekwencji wektorów "OneHot", każdy znak to tablica 0 i 1,
    1 - oznacza że znak w tablicy akceptowanych znaków na danej pozycji jest równy kodowanemu znakowi, 0 nie jest,
    """

    def __init__(self):
        """Konstruktor domyślny"""
        pass

    def sequence_text(self, text: str) -> List[List[int]]:
        """Metoda, która  koduje tekst do postaci sekwencji

        :param self: referencja do instancji obiektu OHVS
        :param text: fraza do zakodowania
        :return: Listę list będącą one hot wektorami
        """
        seq = [[1 if char == s else 0 for s in accepted_symbols] for char in text]
        return seq

    def desequence_text(self, sequence: List[List[int]]) -> str:
        """Metoda która dekoduje sekwencje wektorową na zwykły tekst

        :param self: referencja do instancji obiektu
        :param sequence: sekwencja wektorów one hot
        :return: odkodowany tekst
        """
        assert isinstance(sequence, list), "sequence has to be a list of int"
        return "".join([accepted_symbols[i] for char_arr in sequence for i, num in enumerate(char_arr) if num == 1])
