import logging


class ColorFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        fmt = logging.Formatter(log_fmt)
        return fmt.format(record)


class Logger(logging.Logger):

    __level = logging.DEBUG

    @classmethod
    def set_default_logging_level(cls, level):
        cls.__level = level

    @classmethod
    def get_logger(cls, name: str):
        logger = logging.getLogger(name)
        logger.setLevel(cls.__level)
        ch = logging.StreamHandler()
        ch.setLevel(cls.__level)
        ch.setFormatter(ColorFormatter())
        logger.addHandler(ch)
        return logger

