from pathlib import Path
from tkinter import filedialog as fd


class Installer:
    def __init__(self):
        self.game_name: str | None = None
        self.file_name: Path | None = None

    def get_file_name(self):
        self.file_name = Path(fd.askopenfilename())

    def get_game_name(self):
        self.game_name = input(f'Please input game name.\n>')
