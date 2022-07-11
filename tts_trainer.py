import logging
from typing import *

from torch.utils.data import DataLoader

from network_utils.dataset import SpeechSamplesDataset
from utils import default_config
from utils.config_loader import TrainingConfigLoader
from utils.exceptions import ConfigLoadingUnsuccessful


class TtsTrainer:
    """Klasa, która odpowieada za proces trenowania modelu, wywoływanie odpowiednich akcji
        by ten model wytrenować
    """
    def __init__(self, config_path: Optional[str]) -> None:
        """Konstruktor klasy, który ładuje plik konfiguracyjny

        :param config_path: ściezka do pliku konfiguracyjnego
        :raises ConfigLoadingUnsuccessful: kiedy nie udało się załadować poprawnego pliku konfiguracyjnego
        """
        config_loader = TrainingConfigLoader()
        loaded_config = config_loader.load_config(config_path)
        if loaded_config is None:
            logging.warning("Provided config was not correct, loading default configuration")
        self.config = loaded_config or default_config.training_config
        if self.config is None and config_path is not None:
            raise ConfigLoadingUnsuccessful("Could not load config file")

        logging.info("|Training config file '{}' loaded successfully".format(config_path))

    def do_training(self) -> None:
        """Metoda rozpoczynająca proces trenowania modelu i wszystkie akcje z tym związane
        """
        root_dir = self.config['dataset']['root-dir']
        definition_f = self.config['dataset']['definition-file']
        self.dataset = SpeechSamplesDataset(definition_f, root_dir, is_zip=root_dir.endswith('.zip'))
        logging.info("|Dataset '{}' loaded successfully".format(root_dir))

        # batch_size na 1, ponieważ każdy tensor różni się rozmiarem, więc należy ręcznie dzielić dane na batche
        self.dataloader = DataLoader(self.dataset, batch_size=1, shuffle=True)
        self.dataloader = iter(self.dataloader)
        logging.info("|Dataloader for dataset prepared successfully")

        n_sample = next(self.dataloader)
        print(n_sample)
        #
        # example_text = n_sample.get('transcription')[0]
        #
        # text_pre = TextPreprocessor()
        # cleaned_text = text_pre.clean(example_text)
        #
        # one_hot = OneHotVectorSequencer()
        # seq_text = one_hot.sequence_text(cleaned_text)
        #
        # print("\nSequenced text:")
        # print(seq_text)
        #
        # print("\nDesequenced text:")
        # print(one_hot.desequence_text(seq_text))
        # print("Og text")
        # print(example_text)
        #
        # inpu = torch.Tensor(seq_text).to(torch.int32)
        #
        # netw = EncoderNetwork(256, 512, 2, len(inpu), 0.5)
        # dect = DecoderNetwork(256, 512, 2, len(n_sample.get('mel')), 0.5)
        #
        # with torch.no_grad():
        #     pr = netw.forward(inpu)
        #     print(pr[1])
        #     dec = dect.forward(n_sample.get('mel'), pr[0].to(torch.float32), pr[1].to(torch.float32))
        #     print(dec)
