"""
Expected install flow:
    1. User clicks 'Install New Game' button
    2. Dialogue opens -> select path
    3. Dialogue opens -> Request Name, Version
    4. Unzipper type is determined
    5. Installer object is created (including unzipper)
    5. Unzipper extracts files to /Users/user/Games/ folder
    6. User selects executable
    7. Save name, version, path, type to database.
"""
from pathlib import Path

import Install


class TestInstallFunctions:
    def test_installer_asks_for_path_to_file(self, monkeypatch) -> None:
        expected = Path('test/path')
        monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda **_: expected)

        actual = Install.get_path()

        assert actual == expected
