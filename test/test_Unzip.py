from pathlib import Path

import Unzip


def rm_tree(files):
    for file in files:
        if file.is_dir():
            rm_tree(file.iterdir())
            file.rmdir()
        else:
            file.unlink(missing_ok=True)


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

    def test_get_unzipper_for_app(self) -> None:
        path = Path('myApp.app')
        actual = Unzip.get_unzipper(path)
        assert type(actual) == Unzip.AppUnzipper
        assert actual.src == path


class TestZipUnzipper:
    mocks = Path('mocks')
    fake_zip = mocks / 'fake_zip'
    fake_text = fake_zip / 'fake_text.txt'
    fake_rdme = fake_zip / 'fake_readme.md'
    zip_file = mocks / 'fake_archive.zip'

    def teardown_method(self, test_method):
        if self.fake_zip.exists():
            rm_tree(self.fake_zip.iterdir())
            self.fake_zip.rmdir()

    def test_unzip(self):
        unzipper = Unzip.ZipUnzipper(src=self.zip_file)
        unzipper.unzip(self.fake_zip)

        assert self.fake_zip.exists()
        assert self.fake_text.exists()
        assert self.fake_rdme.exists()


class TestDirUnzipper:
    mocks = Path('mocks')
    fake_dir = mocks / 'fake_dir'
    fake_text = fake_dir / 'fake_text.txt'
    fake_rdme = fake_dir / 'fake_readme.md'
    dir_file = mocks / 'fake_directory'

    def teardown_method(self, test_method):
        if self.fake_dir.exists():
            rm_tree(self.fake_dir.iterdir())
            self.fake_dir.rmdir()

    def test_unzip(self):
        unzipper = Unzip.DirUnzipper(src=self.dir_file)
        unzipper.unzip(self.fake_dir)

        assert self.fake_dir.exists()
        assert self.fake_text.exists()
        assert self.fake_rdme.exists()


class TestAppUnzipper:
    mocks = Path('mocks')
    fake_app = mocks / 'fake_app.app'
    app_file = mocks / 'fake_application.app'

    def teardown_method(self, test_method):
        if self.fake_app.exists():
            rm_tree(self.fake_app.iterdir())
            self.fake_app.rmdir()

    def test_unzip(self):
        unzipper = Unzip.DirUnzipper(src=self.app_file)
        unzipper.unzip(self.fake_app)

        assert self.fake_app.exists()
