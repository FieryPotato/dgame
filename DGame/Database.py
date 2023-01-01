import datetime
from pathlib import Path

import sqlalchemy.orm


USR: Path = Path('/Users/adrian.mac')
GAMES: Path = USR / 'Games'
DOWNLOADS: Path = USR / 'Downloads'
DB_PATH: Path = GAMES / 'games.db'

Base = sqlalchemy.orm.declarative_base()
ENGINE_PATH = 'sqlite:///' + str(DB_PATH)

EMPTY_DB = 'No Games Installed'


class Game(Base):
    __tablename__ = 'game'

    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    version = sqlalchemy.Column(sqlalchemy.String)
    exe_path = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.DATETIME)

    def __repr__(self):
        return f"Game(name={self.name!r}, version={self.version!r}, "\
               f"exe_path={self.exe_path!r}, date={self.date!r})"


def sql_engine():
    return sqlalchemy.create_engine(ENGINE_PATH, echo=True, future=True)


def add_game(name: str, version: str, exe_path: str) -> None:
    with sqlalchemy.orm.Session(sql_engine()) as session:
        new_game = Game(
            name=name,
            version=version,
            exe_path=exe_path,
            date=datetime.date.today()
        )
        session.add(new_game)
        session.commit()


def update_game(name: str, version: str, exe_path: str):
    with sqlalchemy.orm.Session(sql_engine()) as session:
        statement = sqlalchemy.select(Game).where(Game.name == name)
        game = session.scalar(statement).one()

        # Push new values into game row
        game.name = name
        game.version = version
        game.exe_path = exe_path
        game.date = datetime.datetime.today()

        session.commit()


def get_game(name: str) -> Game | None:
    if name == EMPTY_DB:
        return None
    with sqlalchemy.orm.Session(sql_engine()) as session:
        statement = sqlalchemy.select(Game).where(Game.name == name)
        game = session.scalar(statement).one()
    return game


def remove_game(name: str) -> None:
    with sqlalchemy.orm.Session(sql_engine()) as session:
        statement = sqlalchemy.select(Game).where(Game.name == name)
        game = session.scalar(statement).one()
        session.delete(game)


def get_column(column: str) -> list[str]:
    if column not in {'name', 'version', 'exe_path', 'exe_type', 'date'}:
        raise ValueError(f'Requested column \'{column}\' not in database.')
    with sqlalchemy.orm.Session(sql_engine()) as session:
        statement = sqlalchemy.select(getattr(Game, column))
        column_scalar = session.scalar(statement)
        if not column_scalar:
            column_contents = [EMPTY_DB]
        else:
            column_contents = column_scalar.fetchall
    return column_contents


if not DB_PATH.exists():
    if not GAMES.exists():
        GAMES.mkdir()
    Base.metadata.create_all(sql_engine())
