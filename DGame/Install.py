from pathlib import Path
from tkinter import filedialog as fd
from typing import Protocol

import Database

from Unzip import Unzipper


def get_path() -> Path:
    path: str = fd.askopenfilename(initialdir=Database.DOWNLOADS)
    return Path(path)


class Installer(Protocol):
    path: Path
    name: str
    version: str
    unzipper: Unzipper


class AppInstaller:
    def __init__(self, path: Path, name: str, version: str):
        self.path = path
        self.name = name
        self.version = version
        self.unzipper = get_unzipper()
