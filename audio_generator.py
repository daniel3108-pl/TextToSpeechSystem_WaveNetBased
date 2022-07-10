import default_config


class AudioGenerator:
    def __init__(self, text: str, config_file: str):
        print("|Provided text to generate audio from")
        print(text)

        self.config = default_config.generator_config

    def do_generation(self) -> None:
        pass