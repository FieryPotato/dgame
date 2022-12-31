from pathlib import Path

import Unzip


class TestUnzipFunctions:
    def test_get_unzipper_for_zip(self) -> None:
        path = Path('anything.zip')
        actual = Unzip.get_unzipper(src=path)
        assert type(actual) == Unzip.ZipUnzipper
        assert actual.src == path

    def test_get_unzipper_for_dir(self) -> None:
        path = Path('path/to/whatever')
        actual = Unzip.get_unzipper(src=path)
        assert type(actual) == Unzip.DirUnzipper
        assert actual.src == path
