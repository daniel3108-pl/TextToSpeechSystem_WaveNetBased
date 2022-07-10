from utils import Monad


LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z',' ']


class TextPreprocessor:
    def __init__(self):
        pass

    # Ta monada to tylko zeby ladniej kod wygladal tak naprawde
    def transform(self, text: str) -> str:
        return Monad.some(text) \
                    .map(str.lower) \
                    .map(str.strip) \
                    .map(self.__remove_symbols) \
                    .map(self.__remove_empty_chars) \
                    .unbind()

    def __remove_symbols(self, text) -> str:
        return "".join([char for char in text if char in LETTERS])

    def __remove_empty_chars(self, text) -> str:
        text_arr = list(text)
        i, j = 0, 1
        while i < len(text_arr) and j < len(text_arr): # fajny O(n) algos na usuwanie powtarzajacych sie spacji
            if text_arr[i] == " " and text_arr[j] == " ":
                del text_arr[j]
                continue
            i += 1
            j += 1

        return "".join(text_arr)

