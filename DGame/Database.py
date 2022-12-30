from pathlib import Path

import sqlalchemy.orm


Base = sqlalchemy.orm.declarative_base()
DB_PATH = Path.cwd() / 'games.db'
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


def engine():
    return sqlalchemy.create_engine(ENGINE_PATH, echo=True, future=True)


if not DB_PATH.exists():
    Base.metadata.create_all(engine())
