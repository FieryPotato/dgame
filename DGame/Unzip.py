import shutil
from pathlib import Path
from typing import Protocol


class Unzipper(Protocol):
    src: Path

    def unzip(self, dst: Path) -> None:
        """
        Unzip self.src to dst.

        src is a zip file or directory.
        dst is the directory into which everything is unzipped.
        """
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


class DirUnzipper:
    def __init__(self, src: Path):
        self.src = src

    def unzip(self, dst: Path) -> None:
        shutil.copytree(src=self.src, dst=dst, dirs_exist_ok=True)


class ZipUnzipper:
    def __init__(self, src: Path):
        self.src = src

    def unzip(self, dst: Path) -> None:
        shutil.unpack_archive(filename=self.src, extract_dir=dst)
