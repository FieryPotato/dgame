import os
from pathlib import Path
from tkinter import filedialog as fd

import Database
import Unzip

from Unzip import Unzipper


class Installer:
    def __init__(self, path: Path, name: str, version: str):
        self.path = path
        self.name = name
        self.version = version
        self.unzipper: Unzipper = Unzip.get_unzipper(path)

    def install(self) -> None:
        dst = Database.GAMES / self.name
        title = 'Select Game\'s main executable.'
        exe = Path(fd.askopenfilename(initialdir=dst, title=title))

        # set permissions to avoid windows-compiled software issues
        os.system(f'chmod -R 755 \'{dst}\'')

        Database.add_game(self.name, self.version, str(exe), exe.suffix)


def get_path() -> Path:
    title = 'Select Game File to Install'
    path: str = fd.askopenfilename(initialdir=Database.DOWNLOADS, title=title)
    return Path(path)


def get_installer(path: Path, name: str, version: str) -> Installer:
    return Installer(path=path, name=name, version=version)
