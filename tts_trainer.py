from typing import *

from torch.utils.data import DataLoader

import default_config
from config_loader import TrainingConfigLoader
from dataloader import SpeechSamplesDataset
from encoder.text_preprocessor import TextPreprocessor
from exceptions import ConfigLoadingUnsuccessful


class TtsTrainer:
    """Klasa, która odpowieada za proces trenowania modelu, wywoływanie odpowiednich akcji
        by ten model wytrenować
    """
    def __init__(self, config_path: Optional[str]) -> None:
        """Konstruktor klasy, który ładuje plik konfiguracyjny

        :param config_path: ściezka do pliku konfiguracyjnego
        """
        config_loader = TrainingConfigLoader()
        self.config = config_loader.load_config(config_path) or default_config.training_config
        if self.config is None and config_path is not None:
            raise ConfigLoadingUnsuccessful("Could not load config file")

        print("|Training config file '{}' loaded successfully".format(config_path))

    def do_training(self) -> None:
        """Metoda rozpoczynająca proces trenowania modelu i wszystkie akcje z tym związane
        """
        root_dir = self.config['dataset']['root-dir']
        definition_f = self.config['dataset']['definition-file']
        self.dataset = SpeechSamplesDataset(definition_f, root_dir)
        print("|Dataset '{}' loaded successfully".format(root_dir + definition_f))

        # batch_size na 1, ponieważ każdy tensor różni się rozmiarem, więc należy ręcznie dzielić dane na batche
        self.dataloader = DataLoader(self.dataset, batch_size=1, shuffle=True)
        self.dataloader = iter(self.dataloader)
        print("|Dataloader for dataset prepared successfully")

        print(next(self.dataloader))

        text_preprocessor = TextPreprocessor()
        print(text_preprocessor.transform("Hello world, ^73 dssay dupa--9  93 ab  "))

