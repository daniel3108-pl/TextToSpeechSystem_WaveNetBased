from typing import *
import yaml
import os
from utils import Monad


class TrainingConfigLoader:
    def __init__(self) -> None:
        pass

    def load_config(self, path: str) -> Dict[str, Union[str, float, int]]:
        if not os.path.isfile(path):
            raise FileNotFoundError("Config file of path: {}, does not exist".format(path))

        with open(path) as f:
            config_file = yaml.load(f, yaml.Loader)

        print(self.__hasProperFields(config_file))

        return config_file if self.__validate_config(config_file) else None

    def __validate_config(self, config: Dict[str, str]) -> bool:
        return self.__hasProperFields(config) and self.__hasProperModelValues(config) and self.__hasProperDatasetValues(config)

    def __hasProperFields(self, config: Dict[str, Union[str, float, int]]) -> bool:
        if not list(config.keys()) == ['model', 'dataset']:
            return False

        if not list(config.get('model').keys()) == ['epochs', 'batch-size', 'learning-rate', 'output-file']:
            return False

        if not list(config.get('dataset').keys()) == ['definition-file', 'audio-directory']:
            return False

        return True

    def __hasProperModelValues(self, config: Dict[str, Union[str, float, int]]):
        model_config = config["model"]
        try:
            eps = int(model_config["epochs"])
        except Exception as e:
            return False
        try:
            batch = int(model_config["batch-size"])
        except Exception as e:
            return False
        try:
            lr = float(model_config['learning-rate'])
        except Exception as e:
            return False

        if eps < 1 and batch < 1 and lr <= 0:
            return False

        with open(model_config["output-file"], "w") as f:
            f.write("")

        if not os.path.isfile(model_config["output-file"]):
            os.remove(model_config['output-file'])
            return False

        os.remove(model_config['output-file'])
        return True

    def __hasProperDatasetValues(self, config: Dict[str, Union[str, float, int]]) -> bool:
        return True # For debug only

        if not os.path.isfile(config['dataset']['definition-file']):
            return False
        if not os.path.isdir(config['dataset']['autio-directory']):
            return False
        return True


class GeneratorConfigLoader:
    def __init__(self):
        pass

    def load_config(self, path: str) -> Dict[str, Union[str, float, int]]:
        pass