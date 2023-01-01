import Database


class Controller:
    def get_game_names(self) -> list[str]:
        return Database.get_column('name')
