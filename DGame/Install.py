import os
from pathlib import Path
from tkinter import filedialog as fd

import Database
import Unzip

from Unzip import Unzipper


class Installer:
    ask_path_title = 'Select Game\'s main executable.'

    def __init__(self, path: Path, name: str, version: str):
        self.path = path
        self.name = name
        self.version = version
        self.unzipper: Unzipper = Unzip.get_unzipper(path)
        self.dst = Database.GAMES / self.name

    def install(self) -> None:
        exe = Path(fd.askopenfilename(initialdir=self.dst, title=self.ask_path_title))
        self.set_permissions()
        Database.add_game(self.name, self.version, str(exe), exe.suffix)

    def update(self) -> None:
        exe = Path(fd.askopenfilename(initialdir=self.dst, title=self.ask_path_title))
        self.set_permissions()
        Database.update_game(self.name, self.version, str(exe), exe.suffix)

    def set_permissions(self) -> None:
        os.system(f'chmod -R 755 \'{self.dst}\'')


def get_path() -> Path:
    title = 'Select Game File to Install'
    path: str = fd.askopenfilename(initialdir=Database.DOWNLOADS, title=title)
    return Path(path)


def get_installer(path: Path, name: str, version: str) -> Installer:
    return Installer(path=path, name=name, version=version)
