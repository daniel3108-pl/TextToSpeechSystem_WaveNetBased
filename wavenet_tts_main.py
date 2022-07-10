from typing import *
import os, sys
import json
from config_loader import TrainingConfigLoader
import threading
import logging
from utils import Monad
import argparse
from audio_generator import AudioGenerator
from tts_trainer import TtsTrainer


def argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help="Choose program functionality [training model | generating audio from text], \n"
                                            "You can use [--help | -h] with each command to see its arguments", dest='func')

    train_parser = subparsers.add_parser("train", help="Using it will make program train your model")
    train_parser.add_argument("--config", help="Set optional config file to your training process", required=False, dest="config")

    generate_parser = subparsers.add_parser("generate", help="Using it will make program generate audio based on your input")
    generate_parser.add_argument("--config", help="Set optional config file to your generating process", required=False, dest="config")
    generate_parser.add_argument("--out", help="Name of output file", required=False, dest="out_file")
    generate_parser.add_argument("--text", help="Text to generate audio from", required=False, dest="text")
    return parser


def main(args: argparse.Namespace) -> None:
    logging.basicConfig(level=logging.INFO)

    if args.func == "train":
        trainer = TtsTrainer(args.config)
    elif args.func == "generate":
        text = args.text or input("Text to generate from: \n")
        audio_generator = AudioGenerator(text)


if __name__ == "__main__":
    parser = argument_parser()
    main(parser.parse_args())
