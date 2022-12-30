"""
Expected install flow:
    1 - get path
    2 - user inputs name
    3 - user inputs version #
    4 - extract files from path to games folder
    5 - user selects executable
    6 - initialize executable using chmod
    7 - open database connection
    8 - save name, version, path, type to database
    9 - close database connection

    1 - done using tkinter.filedialog.askopenfilename()
    2 - Installer object asks using input
    3 - Installer object asks using input
    4 - Depending on whether files are in zipfile, rarfile, or directory:
        - Installer object contains an unzipper from a factory that checks
        what kind the file is.
        - Unzipper does the moving from current location to games directory.
    5 - done using tkinter.filedialog.askopenfilename()
    6 - done through os.chmod (unless there's a better way)
    7 - from DGame.Database import Database --> open database connection
    8 - DGame.Database --> insert name, version, path, type
    9 - DGame.Database --> connection.close()
"""
from pathlib import Path

from Install import Installer


class TestInstaller:
    def test_installer_asks_for_file(self, monkeypatch) -> None:
        monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda: Path('test/path'))

        installer = Installer()
        installer.get_file_name()
        expected = Path('test/path')

        assert installer.file_name == expected

    def test_installer_asks_for_name(self, monkeypatch) -> None:
        monkeypatch.setattr('builtins.input', lambda _: 'Skyrim')

        installer = Installer()
        installer.get_game_name()
        expected = 'Skyrim'

        assert installer.game_name == expected

