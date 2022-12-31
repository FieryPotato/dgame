import shutil

import Database


class Uninstaller:
    def __init__(self, name):
        self.name = name

    def uninstall(self) -> None:
        game = Database.get_game(self.name)
        shutil.rmtree(game.exe_path)
        Database.remove_game(self.name)
