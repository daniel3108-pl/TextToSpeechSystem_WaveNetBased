"""
Moduł odpowiedzialny za klasy ładujące pliki konfiguracyjne
"""

import logging
import os
from typing import *

import yaml

from .logger import Logger
from .other_utils import is_int, is_float
from .zip_file_handler import ZipFileHandler


class TrainingConfigLoader:
    """Klasa ładująca plik konfiguracyjny yaml do specyfikowania parametrów uczenia
    """

    config_logger: logging.Logger = Logger.get_logger("Training Config Loader")
    """Pole z loggerem"""

    def __init__(self) -> None:
        pass

    def load_config(self, path: str) -> Optional[Dict]:
        """Metoda ładująca plik konfiguracyjny
        :param path: ścieżka do pliku konfiguracyjnego
        :return: Obiekt typu Dictionary z załadowanymi argumentami
        """
        if not os.path.isfile(path):
            self.config_logger.error("|Config file of path: {}, does not exist".format(path))
            raise FileNotFoundError("Config file of path: {}, does not exist".format(path))

        with open(path) as f:
            config_file = yaml.load(f, yaml.Loader)

        return config_file if self.__validate_config(config_file) else None

    def __validate_config(self, config: Dict) -> bool:
        """Metoda wywołująca walidację pliku konfiguracyjnego
        :param config: obiekt dictionary z załadowaną konfiguracją
        :return: True jeśli konfiguracja jest poprawna False jeśli nie
        """
        return self.__has_proper_fields(config) \
               and self.__has_proper_model_value(config) \
               and self.__has_proper_dataset_values(config)

    def __has_proper_fields(self, config: Dict) -> bool:
        """Metoda sptawdzająca czy plik konfiguracyjny ma odpowiednie pola

        :param config: słownik z definiciją konfiguracji
        :return: True lub False w zależności od wyniku
        """
        if not list(config.keys()) == ['model', 'dataset']:
            logging.error("Config misses model or dataset categories")
            return False

        if not list(config['model'].keys()) == ['encoder', 'decoder', 'wavenet', 'output-file']:
            self.config_logger.error("Model category misses {} subcategories" \
                          .format({'encoder', 'decoder', 'wavenet', 'output-file'} - set(config['model'].keys())))
            return False

        for m in ['encoder', 'decoder', 'wavenet']:
            if config['model'][m]["epochs"] is None \
                    or config['model'][m]["batch-size"] is None \
                    or config['model'][m]["learning-rate"] is None:
                self.config_logger.error("|Config for {} misses {} fields" \
                                         .format(m, {"epochs", "batch-size", "learning-rate"} - set(config['model'][m].keys())))
                return False

        if not list(config['dataset'].keys()) == ['root-dir', 'definition-file', 'audio-directory']:
            self.config_logger.error("|Config for dataset misses {} fields" \
                                     .format({'definition-file', 'audio-directory', 'root-dir'} - set(config['dataset'].keys())))
            return False

        return True

    def __has_proper_model_value(self, config: Dict) -> bool:
        """Sprawdza czy konfiguracja modelu ma odpowiednie formaty wartości

        :param config: słownik z definicją konfiguracji
        :return: True lub False w zależności od wyniku
        """
        model_config = config["model"]

        for model in ['encoder', 'decoder', 'wavenet']:
            if not self.__is_model_type_config_correct(model_config, model):
                return False

        with open(model_config["output-file"], "w") as f:
            f.write("")

        if not os.path.isfile(model_config["output-file"]):
            os.remove(model_config['output-file'])
            return False

        os.remove(model_config['output-file'])
        return True

    def __is_model_type_config_correct(self, model_config: Dict, model: str) -> bool:
        """Sprawdza poprawność wartości dla danego typu modelu w pliku konfiguracyjnym

        :param model_config: słownik z konfiguracją konkretnego modelu
        :param model: nazwa modelu do sprawdzenia
        :return: True lub False w zależności od wyniku
        """
        model_config_for_type = model_config[model]

        if not is_int(model_config_for_type["epochs"]) or \
                not is_int(model_config_for_type["batch-size"]) or \
                not is_float(model_config_for_type['learning-rate']):
            return False

        eps = int(model_config_for_type["epochs"])
        batch = int(model_config_for_type["batch-size"])
        lr = float(model_config_for_type["learning-rate"])

        if eps < 1 and batch < 1 and lr <= 0:
            return False

        return True

    def __has_proper_dataset_values(self, config: Dict) -> bool:
        """Sprawdza czy sa poprawne wartości w konfiguracji zestawu danych

        :param config: Słownik z konfiguracją
        :return: True lub False w zależności od wyniku funkcji
        """
        if not config['dataset']['root-dir'].endswith(".zip") and not os.path.isdir(config['dataset']['root-dir']):
            return False
        elif config['dataset']['root-dir'].endswith(".zip") and os.path.isfile(config['dataset']['root-dir']):
            self.config_logger.info("|Dataset in zip archive was detected. Started handling zip file.")
            return self.__handle_rootdir_beingzip(config['dataset']['root-dir'],
                                           config['dataset']['definition-file'],
                                           config['dataset']['audio-directory'])

        if not os.path.isdir(config['dataset']['root-dir'] + config['dataset']['audio-directory']):
            return False
        if not os.path.isfile(config['dataset']['root-dir'] + config['dataset']['definition-file']):
            return False
        return True

    def __handle_rootdir_beingzip(self, rootdir: str, deffile: str, wav_dir: str) -> bool:
        zip_hanlder = ZipFileHandler(rootdir)
        zip_hanlder.load_zip()

        filenames = zip_hanlder.get_filenames()
        if not deffile in filenames:
            zip_hanlder.close()
            self.config_logger.error("|Metadata file {} was not found".format(deffile))
            return False

        if not wav_dir in filenames:
            zip_hanlder.close()
            self.config_logger.error("|No wav files dir {}".format(wav_dir))
            return False

        zip_hanlder.close()
        return True




class GeneratorConfigLoader:
    """Klasa odpowiadająca za ładowanie i walidację pliku konfiguracyjnego dla generowania audio

    """
    def __init__(self):
        pass

    def load_config(self, path: str) -> Optional[Dict]:
        """Metoda ładująca i walidująca plik konfiguracyjny

        :param path: Ścieżka do pliku konfiguracyjnego
        :return: Słownik z definicją konfiguracji lub None
        """
        pass
