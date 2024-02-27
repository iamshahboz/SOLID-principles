# This class violates Single Responsibility Principle because it has two different responsibilities
# it uses read and write method to manage file and also deals with Zip archieve

from pathlib import Path 
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding='utf-8'):
        return self.path.read_text(encoding)
    
    def write(self, data, encoding='utf-8'):
        self.path.write_text(data,encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix('.zip'),mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

