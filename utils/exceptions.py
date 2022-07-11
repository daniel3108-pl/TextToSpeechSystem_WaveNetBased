"""Moduł przechowujący klasy wyjątków"""


class ConfigLoadingUnsuccessful(Exception):
    """Klasa wyjątku gdy plik konfiguracyjny nie został poprawnie odczytany
    """
    pass

class ZipFileIsNotOpened(Exception):
    pass