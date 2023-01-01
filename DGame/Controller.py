import Database


class Controller:
    def get_game_names(self):
        return Database.request_column('name')
