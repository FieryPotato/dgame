from pathlib import Path

import Install


class TestInstallFunctions:
    def test_get_path(self, monkeypatch) -> None:
        expected = Path('test/path')
        monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda **_: expected)

        actual = Install.get_path()

        assert actual == expected

    def test_get_installer(self) -> None:
        path = Path('test.zip')
        name = 'Test II: More Testing'
        version = '1.0'
        installer = Install.get_installer(name, version, path)

        assert installer.path == path
        assert installer.name == name
        assert installer.version == version
