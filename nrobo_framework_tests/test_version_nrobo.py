from nrobo import console


class TestVersionInfo():

    def test_version_in_nrobo_init_file_method(self):
        """Validate nrobo/__init__.py has correct published version"""

        from nrobo.cli.upgrade import get_pypi_index
        from nrobo import __version__

        assert __version__ == get_pypi_index("nrobo")

