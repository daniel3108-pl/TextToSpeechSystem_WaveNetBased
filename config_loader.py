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

        return config_file if self.__validate_config(config_file) else None

    def __validate_config(self, config: Dict[str, str]) -> bool:
        return self.__has_proper_fields(config) \
               and self.__has_proper_model_value(config) \
               and self.__has_proper_dataset_values(config)

    def __has_proper_fields(self, config: Dict[str, Union[str, float, int]]) -> bool:
        if not list(config.keys()) == ['model', 'dataset']:
            return False
        if not list(config.get('model').keys()) == ['encoder', 'decoder', 'wavenet', 'output-file']:
            return False

        for m in ['encoder', 'decoder', 'wavenet']:
            if config['model'][m].get("epochs") is None \
                    or config['model'][m].get("batch-size") is None \
                    or config['model'][m].get("learning-rate") is None:
                return False

        if not list(config.get('dataset').keys()) == ['definition-file', 'audio-directory']:
            return False

        return True

    def __has_proper_model_value(self, config: Dict[str, Union[str, float, int]]):
        model_config = config["model"]
        for model in ['encoder', 'decoder', 'wavenet']:
            try:
                eps = int(model_config[model]["epochs"])
            except Exception as e:
                return False
            try:
                batch = int(model_config[model]["batch-size"])
            except Exception as e:
                return False
            try:
                lr = float(model_config[model]['learning-rate'])
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

    def __has_proper_dataset_values(self, config: Dict[str, Union[str, float, int]]) -> bool:
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