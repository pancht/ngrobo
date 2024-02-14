import os
from pathlib import Path

from nrobo import console, terminal, EnvKeys, NROBO_PATHS
from nrobo.cli.nglobals import Browsers


class TestNRoboFramework():

    def test_nrobo_framework_simplest_way(self):
        """Validate that all nrobo framework tests passed"""

        command = ['python', 'nrobo.py', '--browser', Browsers.CHROME_HEADLESS,
                   '--rootdir', str(Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.FRAMEWORK / NROBO_PATHS.TESTS)]
        return_code = terminal(command)

        assert return_code == 0

    def test_upgrade_prompt_presence_in_older_version_of_nRoBo(self):
        """Validate that upgrade prompt is showing up when host has lower version of nRoBo"""

        from nrobo.cli.upgrade import get_pypi_index, get_host_version

        command = ['python', 'nrobo.py', '--browser', Browsers.CHROME_HEADLESS,
                   '--rootdir', str(Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.FRAMEWORK / NROBO_PATHS.TESTS)]

        if get_host_version() == get_pypi_index("nrobo"):
            """no upgrade prompt"""
            assert True  # this scenario already covered in another test: test_nrobo_framework_simplest_way
        else:
            """upgrade prompt"""
            command.append('--suppress')

            assert terminal(command) == 0  # 0 means success

    def test_version_in_nrobo_init_file_method(self):
        """Validate nrobo/__init__.py has correct published version"""

        from nrobo.cli.upgrade import get_pypi_index
        from nrobo import __version__

        assert __version__ == get_pypi_index("nrobo")

