import os
import shutil

from pathlib import Path
from tkinter import filedialog as fd
from typing import Protocol

import Database


class Installer:
    ask_path_title = 'Select Game\'s main executable.'

    def __init__(self, name: str, version: str, path: Path):
        self.path = path / name
        self.name = name
        self.version = version
        self.unzipper: Unzipper = get_unzipper(path)
        self.dst = Database.GAMES / self.name

    def install(self) -> None:
        self.unzipper.unzip(self.dst)
        exe = Path(fd.askopenfilename(initialdir=self.dst, title=self.ask_path_title))
        self.set_permissions()
        Database.add_game(self.name, self.version, str(exe))

    def set_permissions(self) -> None:
        os.system(f'chmod -R 755 \'{self.dst}\'')


def get_path() -> Path:
    title = 'Select Game File to Install'
    path: str = fd.askopenfilename(initialdir=Database.DOWNLOADS, title=title)
    return Path(path)


def get_installer(name: str, version: str, path: Path | str) -> Installer:
    if not isinstance(path, Path):
        path = Path(path)
    return Installer(name=name, version=version, path=path)


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


def uninstall(game_name) -> None:
    game = Database.get_game(game_name)
    if game is None:
        print('No game was removed.')
        return
    shutil.rmtree(game.exe_path)
    Database.remove_game(game_name)