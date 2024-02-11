import os
import subprocess
from pathlib import Path

import pytest

from nrobo.cli.nglobals import Browsers
from nrobo.util.process import terminal
from nrobo import set_environment, EnvKeys, NROBO_CONST, NROBO_PATHS
from nrobo.cli.cli_constansts import NREPORT


class TestNROBO():
    """nRobo tests"""

    def test_nrobo_framework_simplest_way(self):
        """Validate that all nrobo framework tests passed"""

        command = ['python', 'nrobo.py', '--browser', Browsers.CHROME_HEADLESS]
        return_code = terminal(command)

        assert return_code == 0

    def test_conftest_py_file_present_in_root(self):
        """Validate that conftest.py is present in root dir"""

        set_environment()

        conftest_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.CONFTEST_PY

        assert conftest_path.exists() == True

    def test_conftest_py_not_present_in_nrobo_package(self):
        """Validate that conftest.py is not present in the nrobo package directory"""

        set_environment()

        conftest_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.CONFTEST_PY

        assert conftest_path.exists() == False