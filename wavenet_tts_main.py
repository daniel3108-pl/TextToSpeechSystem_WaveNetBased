from typing import *
import os, sys
from config_loader import TrainingConfigLoader
import threading
from utils import Monad


def main(args: List[str]) -> None:
    config_loader = TrainingConfigLoader()
    config = config_loader.load_config(args[1])
    print(config)

    x = Monad(True, 5)


if __name__ == "__main__":
    main(sys.argv)
