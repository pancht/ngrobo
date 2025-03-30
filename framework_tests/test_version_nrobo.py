"""
Test version nrobo py.
"""

import os
import time
from pathlib import Path

import pytest

from nrobo import terminal, EnvKeys, NroboPaths, NroboConst
from nrobo.cli.nglobals import Browsers


class TestNRoboFramework:
    """Test nrobo framework class."""

    @pytest.mark.skip
    def test_nrobo_framework_developer_tests(self):
        """Validate that nrobo framework developer-tests passed located at root"""

        command = [
            "python",
            "nrobo.py",
            "--browser",
            Browsers.CHROME_HEADLESS,
            "-n",
            "20",
        ]
        return_code = terminal(command)

        assert return_code == 0

    @pytest.mark.skip
    def test_nrobo_host_framework_tests(self):
        """Validate that nrobo host framework tests passed
        located at root/nrobo/framework/tests dir"""

        # conftest_file_path_in_framework_folder
        conftest_in_framework_pkg = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.FRAMEWORK
            / NroboPaths.CONFTEST_PY
        )
        command = []

        # copy conftest.py from root to nrobo/framework/tests dir
        from nrobo.util.filesystem import (  # pylint: disable=C0415
            copy_file,
            remove_file,
        )

        if conftest_in_framework_pkg.exists():
            # already exists, then remove it
            remove_file(conftest_in_framework_pkg)

        copy_file(
            f"{Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.CONFTEST_PY}",
            f"{conftest_in_framework_pkg}",
        )

        # pause for 1 sec
        time.sleep(1)

        # set command with --confcutdir switch
        command = [
            "python",
            "nrobo.py",
            "--browser",
            Browsers.CHROME,
            "--confcutdir",
            str(conftest_in_framework_pkg),
            "--rootdir",
            str(
                Path(os.environ[EnvKeys.EXEC_DIR])
                / NroboConst.NROBO
                / NroboPaths.FRAMEWORK
                / NroboPaths.TESTS
            ),
        ]
        # run command
        return_code = terminal(command)

        # delete conftest.py from nrobo/framework/tests dir
        remove_file(conftest_in_framework_pkg)

        assert return_code == 0

    @pytest.mark.skip
    def test_upgrade_prompt_presence_in_older_version_of_nrobo(self):
        """Validate that upgrade prompt is showing up when host has lower version of nRoBo"""

        from nrobo.cli.upgrade import (  # pylint: disable=C0415
            get_pypi_index,
            get_host_version,
        )

        command = [
            "python",
            "nrobo.py",
            "--browser",
            Browsers.CHROME_HEADLESS,
            "--rootdir",
            str(
                Path(os.environ[EnvKeys.EXEC_DIR])
                / NroboPaths.FRAMEWORK
                / NroboPaths.TESTS
            ),
        ]

        if get_host_version() == get_pypi_index("nrobo"):
            # no upgrade prompt
            # this scenario already covered in another test: test_nrobo_framework_simplest_way
            assert True
        else:
            # upgrade prompt
            command.append("--suppress")

            assert terminal(command) == 0  # 0 means success

    def test_version_in_nrobo_init_file_method(self):
        """Validate nrobo/__init__.py has correct published version"""

        import nrobo.cli.detection as detect  # pylint: disable=C0415
        from nrobo import __version__  # pylint: disable=C0415

        assert detect.build_version_from_version_files() == __version__
