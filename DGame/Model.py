from collections import namedtuple

import Database
import Install
import Launch


Game = namedtuple('Game', ['name', 'version', 'date'])


class Model:
    DownloadsFolder = Database.DOWNLOADS

    def read_game_names(self) -> list[str]:
        return Database.get_column('name')

    def get_game(self, game_name) -> Game:
        game = Database.get_game(game_name)
        name, version, date = game['name'], game['version'], game['date']
        return Game(str(name), str(version), str(date))

    def launch_game(self, game_name) -> None:
        Launch.get_launcher(game_name).launch()

    def database_is_empty(self, game_list: list[str]) -> bool:
        return Database.EMPTY_DB in game_list

    def install_scenario(self, scenario_path: str) -> None:
        raise NotImplementedError

    def install_game(self, name: str, version: str, path: str) -> None:
        Install.get_installer(name, version, path).install()

    def game_in_database(self, game_name) -> bool:
        return game_name in self.read_game_names()
