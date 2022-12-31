from pathlib import Path
from typing import Protocol


class Unzipper(Protocol):
    src: Path

    def unzip(self, dst) -> None:
        """Unzip self.src to self.dst"""
        ...


def get_unzipper(src: Path) -> Unzipper:
    pass
