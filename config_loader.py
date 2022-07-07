from typing import *
import yaml
import os
from utils import is_int, is_float
import logging


class TrainingConfigLoader:
    """Klasa ładująca plik konfiguracyjny yaml do specyfikowania parametrów uczenia
    """

    config_logger: logging.Logger = logging.getLogger("Training Config Loader")

    def __init__(self) -> None:
        pass

    def load_config(self, path: str) -> Dict[str, Union[str, float, int]]:
        """Metoda ładująca plik konfiguracyjny
        :param path: ścieżka do pliku konfiguracyjnego
        :return: Obiekt typu Dictionary z załadowanymi argumentami
        """
        if not os.path.isfile(path):
            self.config_logger.error("Config file of path: {}, does not exist".format(path))
            raise FileNotFoundError("Config file of path: {}, does not exist".format(path))

        with open(path) as f:
            config_file = yaml.load(f, yaml.Loader)

        return config_file if self.__validate_config(config_file) else None

    def __validate_config(self, config: Dict[str, str]) -> bool:
        """Metoda wywołująca walidację pliku konfiguracyjnego
        :param config: obiekt dictionary z załadowaną konfiguracją
        :return: True jeśli konfiguracja jest poprawna False jeśli nie
        """
        return self.__has_proper_fields(config) \
               and self.__has_proper_model_value(config) \
               and self.__has_proper_dataset_values(config)

    def __has_proper_fields(self, config: Dict[str, Union[str, float, int]]) -> bool:
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
                self.config_logger.error("Config for {} misses {} fields" \
                                         .format(m, {"epochs", "batch-size", "learning-rate"} - set(config['model'][m].keys())))
                return False

        if not list(config['dataset'].keys()) == ['root-dir', 'definition-file', 'audio-directory']:
            self.config_logger.error("Config for dataset misses {} fields" \
                                     .format({'definition-file', 'audio-directory', 'root-dir'} - set(config['dataset'].keys())))
            return False

        return True

    def __has_proper_model_value(self, config: Dict[str, Union[str, float, int]]):
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

    def __is_model_type_config_correct(self, model_config: Dict[str, Union[int, float]], model: str) -> bool:
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

    def __has_proper_dataset_values(self, config: Dict[str, Union[str, float, int]]) -> bool:
        return True  # For debug only

        if not os.path.isfile(config['dataset']['definition-file']):
            return False
        if not os.path.isdir(config['dataset']['root-dir']):
            return False
        if not os.path.isdir(config['dataset']['root-dir'] + config['dataset']['audio-directory']):
            return False
        return True


class GeneratorConfigLoader:
    def __init__(self):
        pass

    def load_config(self, path: str) -> Dict[str, Union[str, float, int]]:
        pass
