from pathlib import Path
from typing import Protocol


class Unzipper(Protocol):
    src: Path

    def unzip(self, dst: Path) -> None:
        """Unzip self.src to self.dst"""
        ...


def get_unzipper(src: Path) -> Unzipper:
    file_types = {
        '.zip': ZipUnzipper
    }
    if (suffix := src.suffix) in file_types:
        unzipper = file_types[suffix]
    else:
        unzipper = DirUnzipper
    return unzipper(src=src)


class ZipUnzipper:
    def __init__(self, src: Path):
        self.src = src

    def unzip(self, dst: Path) -> None:
        return


class DirUnzipper:
    def __init__(self, src: Path):
        self.src = src

    def unzip(self, dst: Path) -> None:
        return
