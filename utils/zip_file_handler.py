import logging
import zipfile
from typing import *

from .exceptions import ZipFileIsNotOpened


class ZipFileHandler:

    logger = logging.getLogger("Zip file handler")

    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.zipfile: zipfile.ZipFile = None

    def get_file(self, filename: str):
        if self.zipfile:
            return self.zipfile.open(filename)
        raise ZipFileIsNotOpened("Zip file is not opened")

    def get_filenames(self) -> List[str]:
        if self.zipfile:
            return self.zipfile.namelist()
        raise ZipFileIsNotOpened("Zip file is not opened")

    def get_directories(self) -> List[str]:
        if self.zipfile:
            self.zipfile.printdir()
        raise ZipFileIsNotOpened("Zip file is not opened")

    def load_zip(self):
        try:
            self.zipfile = zipfile.ZipFile(self.__file_path)
        except zipfile.BadZipfile as error:
            self.logger.exception(error)
            return None

    def close(self):
        if not self.zipfile:
            raise ZipFileIsNotOpened("Zip file is not opened")
        self.zipfile.close()



