import Database
import Launch


class Model:
    def read_game_names(self) -> list[str]:
        return Database.get_column('name')

    def launch_game(self, game_name) -> None:
        Launch.get_launcher(game_name).launch()

    def database_is_empty(self, game_list: list[str]) -> bool:
        return Database.EMPTY_DB in game_list
