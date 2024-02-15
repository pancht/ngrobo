import os
import time
from pathlib import Path

import pytest

from nrobo import console, terminal, EnvKeys, NROBO_PATHS, NROBO_CONST
from nrobo.cli.nglobals import Browsers
from nrobo.util.filesystem import remove_filetree


class TestNRoboFramework():

    @pytest.mark.skip
    def test_nrobo_framework_developer_tests(self):
        """Validate that nrobo framework developer-tests passed located at root"""

        command = ['python', 'nrobo.py', '--browser', Browsers.CHROME_HEADLESS, '-n', '20']
        return_code = terminal(command)

        assert return_code == 0

    @pytest.mark.skip
    def test_nrobo_host_framework_tests(self):
        """Validate that nrobo host framework tests passed located at root/nrobo/framework/tests dir"""

        # conftest_file_path_in_framework_folder
        conftest_in_framework_pkg = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.FRAMEWORK / NROBO_PATHS.CONFTEST_PY
        command = []

        # copy conftest.py from root to nrobo/framework/tests dir
        from nrobo.util.filesystem import copy_file, remove_file

        if conftest_in_framework_pkg.exists():
            # already exists, then remove it
            remove_file(conftest_in_framework_pkg)

        copy_file(f"{Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.CONFTEST_PY}",
                      f"{conftest_in_framework_pkg}")

        # pause for 1 sec
        time.sleep(1)

        # set command with --confcutdir switch
        command = ['python', 'nrobo.py', '--browser', Browsers.CHROME,
                       '--confcutdir', str(conftest_in_framework_pkg),
                       '--rootdir', str(Path(os.environ[EnvKeys.EXEC_DIR]) /
                                        NROBO_CONST.NROBO / NROBO_PATHS.FRAMEWORK / NROBO_PATHS.TESTS)]
        # run command
        return_code = terminal(command)

        # delete conftest.py from nrobo/framework/tests dir
        remove_file(conftest_in_framework_pkg)

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

