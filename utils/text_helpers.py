"""Moduł funkcji pomocniczych do pracy na łańcuchach znaków"""

from typing import *


def remove_symbols(text: str, accepted_symbols: List[str]) -> str:
    """Usuwa nie chciane znaki z podanego tekstu

    :param text: tekst, w którym chcemy usunąć znaki
    :param accepted_symbols: lista akceptowanych symboli
    :return: tekst z usuniętymi znakami niepożądanymi
    """
    return "".join([char for char in text if char in accepted_symbols])


def remove_empty_chars(text: str) -> str:
    """Usuwa powielone znaki spacji z tekstu

    :param text: tekst do wyczyszczenia
    :return: tekst z usuniętymi powtarzającymi sie spacjami
    """
    text_arr = list(text)
    i, j = 0, 1
    while i < len(text_arr) and j < len(text_arr):
        if text_arr[i] == " " and text_arr[j] == " ":
            del text_arr[j]
            continue
        i += 1
        j += 1

    return "".join(text_arr)
