from pathlib import Path
from tkinter import filedialog as fd

import Database
import Unzip

from Unzip import Unzipper


def get_path() -> Path:
    path: str = fd.askopenfilename(initialdir=Database.DOWNLOADS)
    return Path(path)


class Installer:
    def __init__(self, path: Path, name: str, version: str):
        self.path = path
        self.name = name
        self.version = version
        self.unzipper: Unzipper = Unzip.get_unzipper(path)
