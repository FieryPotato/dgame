from pathlib import Path

import sqlalchemy.orm


USR: Path = Path('/Users/adrian.mac')
GAMES: Path = USR / 'Games'
DOWNLOADS: Path = USR / 'Downloads'
DB_PATH: Path = GAMES / 'games.db'

Base = sqlalchemy.orm.declarative_base()
ENGINE_PATH = 'sqlite:///' + str(DB_PATH)


class Game(Base):
    __tablename__ = 'game'

    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    version = sqlalchemy.Column(sqlalchemy.String)
    exe_path = sqlalchemy.Column(sqlalchemy.String)
    exe_type = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f"Game(name={self.name!r}, version={self.version!r}, "\
               f"exe_path={self.exe_path!r}, exe_type={self.exe_type!r})"


def sql_engine():
    return sqlalchemy.create_engine(ENGINE_PATH, echo=True, future=True)


def add_game(name: str, version: str, exe_path: str, exe_type: str) -> None:
    with sqlalchemy.orm.Session(sql_engine()) as session:
        new_game = Game(
            name=name,
            version=version,
            exe_path=exe_path,
            exe_type=exe_type
        )
        session.add(new_game)
        session.commit()


if not DB_PATH.exists():
    if not GAMES.exists():
        GAMES.mkdir()
    Base.metadata.create_all(sql_engine())
