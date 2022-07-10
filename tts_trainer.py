from typing import *
import logging
import json
from config_loader import TrainingConfigLoader


class TtsTrainer:
    def __init__(self, config_path: str):
        config_loader = TrainingConfigLoader()
        self.config = config_loader.load_config(config_path)

        print("|Loaded training config file:")
        print(json.dumps(self.config, indent="    "))