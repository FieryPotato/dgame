import subprocess
from pathlib import Path
from typing import Protocol

import Database


class Launcher(Protocol):
    exe_path: str

    def launch(self) -> None:
        ...


class HTMLLauncher:
    def __init__(self, exe_path: Path) -> None:
        self.exe_path = str(exe_path)

    def launch(self) -> None:
        subprocess.Popen(['open', '-a', '\'Google Chrome\'', self.exe_path])


class FlashLauncher:
    def __init__(self, exe_path: Path) -> None:
        self.exe_path = str(exe_path)

    def launch(self) -> None:
        subprocess.Popen(['open', '-a', '\'Elmedia Player\'', self.exe_path])


class AppLauncher:
    def __init__(self, exe_path: Path) -> None:
        self.exe_path = str(exe_path)

    def launch(self) -> None:
        subprocess.Popen(['open', self.exe_path])


launchers = {
    '.html': HTMLLauncher,
    '.swf': FlashLauncher,
    '.': AppLauncher
}


def get_launcher(game_name: str) -> Launcher:
    game = Database.get_game(game_name)
    exe_path = game.exe_path
    if (extension := exe_path.suffix) in launchers:
        launcher = launchers[extension]
    else:
        launcher = launchers['.']
    return launcher(exe_path)
