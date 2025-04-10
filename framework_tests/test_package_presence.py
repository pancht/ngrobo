"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Unit tests for validating framework directories.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

import os
from pathlib import Path

import pytest

from nrobo import (
    set_environment,
    EnvKeys,
    NroboConst,
    NroboPaths,
    NroboCliToolPath,
    NroboFrameworkTests,
)


class TestNRoboFrameworkPaths:  # pylint: disable=R0904
    """nRobo tests"""

    def test_cli_package_is_present(self):
        """Validate that cli package is present_release"""
        set_environment()

        cli_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.CLI

        assert cli_pkg_path.exists()

        cli_pkg_init_path = cli_pkg_path / NroboPaths.INIT_PY

        assert cli_pkg_init_path.exists()

    def test_build_pkg_is_present(self):
        """Validate that build package is present_release"""
        set_environment()

        build_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboCliToolPath.BUILD

        assert build_pkg_path.exists()

        build_pkg_init_path = build_pkg_path / NroboPaths.INIT_PY

        assert build_pkg_init_path.exists()

    def test_check_pkg_is_present(self):
        """Validate that check package is present_release"""
        set_environment()

        check_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboCliToolPath.CHECK

        assert check_pkg_path.exists()

        check_pkg_init_path = check_pkg_path / NroboPaths.INIT_PY

        assert check_pkg_init_path.exists()

    def test_compile_pkg_is_present(self):
        """Validate that compile package is present_release"""
        set_environment()

        compile_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboCliToolPath.COMPILE

        assert compile_pkg_path.exists()

        compile_pkg_init_path = compile_pkg_path / NroboPaths.INIT_PY

        assert compile_pkg_init_path.exists()

    def test_development_pkg_is_present(self):
        """Validate that development package is present_release"""
        set_environment()

        development_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboCliToolPath.DEVELOPMENT
        )

        assert development_pkg_path.exists()

        development_pkg_init_path = development_pkg_path / NroboPaths.INIT_PY

        assert development_pkg_init_path.exists()

    def test_publish_pkg_is_present(self):
        """Validate that publish package is present_release"""
        set_environment()

        publish_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboCliToolPath.PUBLISH

        assert publish_pkg_path.exists()

        publish_pkg_init_path = publish_pkg_path / NroboPaths.INIT_PY

        assert publish_pkg_init_path.exists()

    def test_browser_configs_chrome_pkg_is_present(self):
        """Validate that browser_configs.chrome package is present_release"""
        set_environment()

        browser_configs_chrome_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.BROWSERS_CHROME_PKG
        )

        assert browser_configs_chrome_pkg_path.exists()

        browser_configs_chrome_pkg_init_path = (
            browser_configs_chrome_pkg_path / NroboPaths.INIT_PY
        )

        assert browser_configs_chrome_pkg_init_path.exists()

    def test_browsers_edge_pkg_is_present(self):
        """Validate that browsers.edge package is present_release"""
        set_environment()

        browsers_edge_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.BROWSERS_EDGE_PKG
        )

        assert browsers_edge_pkg_path.exists()

        browsers_edge_pkg_init_path = browsers_edge_pkg_path / NroboPaths.INIT_PY

        assert browsers_edge_pkg_init_path.exists()

    def test_browsers_firefox_pkg_is_present(self):
        """Validate that browsers.firefox package is present_release"""
        set_environment()

        browsers_firefox_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.BROWSERS_FIREFOX_PKG
        )

        assert browsers_firefox_pkg_path.exists()

        browsers_firefox_pkg_init_path = browsers_firefox_pkg_path / NroboPaths.INIT_PY

        assert browsers_firefox_pkg_init_path.exists()

    def test_browsers_safari_pkg_is_present(self):
        """Validate that browsers.safari package is present_release"""
        set_environment()

        browsers_safari_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.BROWSERS_CHROME_PKG
        )

        assert browsers_safari_pkg_path.exists()

        browsers_safari_pkg_init_path = browsers_safari_pkg_path / NroboPaths.INIT_PY

        assert browsers_safari_pkg_init_path.exists()

    def test_cli_detection_pkg_is_present(self):
        """Validate that cli.detection package is present_release"""
        set_environment()

        cli_detection_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.DETECTION_PKG
        )

        assert cli_detection_pkg_path.exists()

    def test_cli_formatting_pkg_is_present(self):
        """Validate that cli.formatting package is present_release"""
        set_environment()

        cli_formatting_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.FORMATTING_PKG
        )

        assert cli_formatting_pkg_path.exists()

    def test_cli_install_pkg_is_present(self):
        """Validate that cli.install package is present_release"""
        set_environment()

        cli_install_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.INSTALL_PKG
        )

        assert cli_install_pkg_path.exists()

    def test_cli_install_requirements_txt_file_is_present(self):
        """Validate that cli.tools.requirements.txt file is present_release"""
        set_environment()

        cli_install_requirements_txt_file_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.REQUIREMENTS_TXT_FILE_CLI
        )

        assert cli_install_requirements_txt_file_pkg_path.exists()

    def test_cli_ncodes_pkg_is_present(self):
        """Validate that cli.ncodes package is present_release"""
        set_environment()

        cli_ncodes_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.NCODES_PKG
        )

        assert cli_ncodes_pkg_path.exists()

    def test_cli_nrobo_args_pkg_is_present(self):
        """Validate that cli.nrobo_args package is present_release"""
        set_environment()

        cli_nrobo_args_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.CLI_NROBO_ARGS_PKG
        )

        assert cli_nrobo_args_pkg_path.exists()

    def test_cli_tools_pkg_is_present(self):
        """Validate that cli.tools package is present_release"""
        set_environment()

        cli_tools_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.CLI_TOOLS_PKG
        )

        assert cli_tools_pkg_path.exists()

    def test_cli_upgrade_pkg_is_present(self):
        """Validate that cli.upgrade package is present_release"""
        set_environment()

        cli_upgrade_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.UPGRADE_PKG
        )

        assert cli_upgrade_pkg_path.exists()

    def test_cli_cli_launcher_py_file_is_present(self):
        """Validate that cli.launcher.py file is present_release"""
        set_environment()

        cli_launcher_py_file_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.CLI_LAUNCHER_PY_FILE
        )

        assert cli_launcher_py_file_pkg_path.exists()

    def test_cli_constants_py_file_is_present(self):
        """Validate that cli.cli_constants.py file is present_release"""
        set_environment()

        cli_cli_constants_py_file_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.CLI_CONSTANTS_PY_FILE
        )

        assert cli_cli_constants_py_file_pkg_path.exists()

    def test_cli_cli_version_yaml_file_is_present(self):
        """Validate that cli.version.yaml file is present_release"""
        set_environment()

        cli_cli_version_yaml_file_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.CLI_VERSION_YAML_FILE
        )

        assert cli_cli_version_yaml_file_pkg_path.exists()

    def test_cli_nglobals_py_file_is_present(self):
        """Validate that cli.nglobals.py file is present_release"""
        set_environment()

        cli_nglobals_py_file_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.NGLOBALS_PY_FILE
        )

        assert cli_nglobals_py_file_pkg_path.exists()

    def test_conftest_py_file_present_in_root(self):
        """Validate that conftest.py is present_release in root dir"""

        set_environment()

        conftest_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.CONFTEST_PY

        assert conftest_path.exists()

    def test_conftest_py_not_present_in_nrobo_package(self):
        """Validate that conftest.py is not present_release in the nrobo package"""

        set_environment()

        conftest_path = NroboPaths.EXEC_DIR / NroboConst.NROBO / NroboPaths.CONFTEST_PY

        assert not conftest_path.exists()

    def test_browser_config_package_is_present(self):
        """Validate that browserConfig package is present_release"""
        set_environment()

        browser_config_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.BROWSER_CONFIGS
        )

        assert browser_config_path.exists()

        browser_config_init_path = browser_config_path / NroboPaths.INIT_PY

        assert browser_config_init_path.exists()

    def test_browsers_package_is_present(self):
        """Validate that browsers package is present in release"""
        set_environment()

        browsers_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboConst.NROBO / NroboPaths.BROWSERS
        )

        assert browsers_path.exists()

        browsers_init_path = browsers_path / NroboPaths.INIT_PY

        assert browsers_init_path.exists()

    def test_browsers_package_capability_yaml_present(self):
        """Validate that browsers package > capability.yaml file is present in release"""
        set_environment()

        capability_yaml_file = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.CAPABILITY_YAML
        )

        assert capability_yaml_file.exists()

    def test_browsers_package_markers_yaml_present(self):
        """Validate that browsers package > markers.yaml file is present in release"""
        set_environment()

        markers_yaml_file = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.MARKERS_YAML
        )

        assert markers_yaml_file.exists()

    def test_cli_package_is_present(self):  # pylint: disable=E0102
        """Validate that cli package is present_release"""
        set_environment()

        cli_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboConst.NROBO / NroboPaths.CLI
        )

        assert cli_path.exists()

        cli_init_path = cli_path / NroboPaths.INIT_PY

        assert cli_init_path.exists()

    def test_exceptions_package_is_present(self):
        """Validate that exceptions package is present_release"""
        set_environment()

        excepations_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.EXCEPTIONS
        )

        assert excepations_pkg_path.exists()

        exceptions_pkg_init_path = excepations_pkg_path / NroboPaths.INIT_PY

        assert exceptions_pkg_init_path.exists()

    def test_framework_pkg_is_present(self):
        """Validate that framework package is present_release"""
        set_environment()

        framework_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboConst.NROBO / NroboPaths.FRAMEWORK
        )

        assert framework_pkg_path.exists()

        framework_pkg_init_path = framework_pkg_path / NroboPaths.INIT_PY

        assert framework_pkg_init_path.exists()

    def test_framework_pages_pkg_is_present(self):
        """Validate that nrobo.framework.pages package is present_release"""
        set_environment()

        nrobo_framework_pages_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.FRAMEWORK_PAGES
        )

        assert nrobo_framework_pages_pkg_path.exists()

    def test_framework_pages_page_pypi_home_py_file_is_present(self):
        """Validate that nrobo.framework.pages.page_pypi_home.py file is present_release"""
        set_environment()

        nrobo_framework_pages_page_pypi_homw_py_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.FRAMEWORK_PAGE_PYPI_HOME_PY_FILE
        )

        assert nrobo_framework_pages_page_pypi_homw_py_file_path.exists()

    def test_framework_tests_gui_pkg_is_present(self):
        """Validate that nrobo.framework.tests.gui package is present_release"""
        set_environment()

        nrobo_framework_tests_gui_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboConst.NROBO / NroboPaths.GUI_PKG
        )

        assert nrobo_framework_tests_gui_pkg_path.exists()

    def test_framework_tests_nogui_pkg_is_present(self):
        """Validate that nrobo.framework.tests.no_gui package is present_release"""
        set_environment()

        nrobo_framework_tests_no_gui_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.FRAMEWORK
            / NroboPaths.NO_GUI_PKG
        )

        assert nrobo_framework_tests_no_gui_pkg_path.exists()

    def test_framework_tests_gui_pypi_home_page_test_py_file_is_present(self):
        """Validate that nrobo.framework.tests.gui.PyPi_home_page_test.py file is present_release"""
        set_environment()

        nrobo_framework_tests_gui_pypi_home_page_test_py_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.GUI_PYPI_HOME_PAGE_TEST_PY_FILE
        )

        assert nrobo_framework_tests_gui_pypi_home_page_test_py_file_path.exists()

    def test_framework_tests_pkg_is_present(self):
        """Validate that nrobo.framework.tests package is present_release"""
        set_environment()

        nrobo_framework_tests_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.FRAMEWORK_TESTS
            / NroboPaths.INIT_PY
        )

        assert nrobo_framework_tests_pkg_path.exists()

    def test_framework_nrobo_config_yaml_file_is_present(self):
        """Validate that nrobo.framework.nrobo-config.yaml file is present_release"""
        set_environment()

        nrobo_framework_nrobo_config_yaml_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.FRAMEWORK_NROBO_CONFIG
        )

        assert nrobo_framework_nrobo_config_yaml_file_path.exists()

    def test_framework_conftest_host_py_file_is_present(self):
        """Validate that nrobo.framework.conftest_host.py file is present_release"""
        set_environment()

        nrobo_framework_conftest_host_py_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.NROBO_CONFTEST_HOST_FILE
        )

        assert nrobo_framework_conftest_host_py_file_path.exists()

    def test_framework_requirements_txt_file_is_present(self):
        """Validate that nrobo.framework.requirements.txt file is present_release"""
        set_environment()

        framework_requirements_txt_file_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.FRAMEWORK
            / NroboPaths.REQUIREMENTS_TXT_FILE
        )
        assert framework_requirements_txt_file_pkg_path.exists()

    def test_selenes_pkg_is_present(self):
        """Validate that selenes pkg is present_release"""
        set_environment()

        selenes_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboConst.NROBO / NroboPaths.SELENESE
        )

        assert selenes_pkg_path.exists()

        selenes_pkg_init_path = selenes_pkg_path / NroboPaths.INIT_PY

        assert selenes_pkg_init_path.exists()

    def test_util_pkg_is_present(self):
        """Validate that util package is present_release"""
        set_environment()

        util_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboConst.NROBO / NroboPaths.UTIL
        )

        assert util_pkg_path.exists()

        util_pkg_init_path = util_pkg_path / NroboPaths.INIT_PY

        assert util_pkg_init_path.exists()

    def test_util_commands_ncommands_pkg_is_present(self):
        """Validate that nrobo.util.commands.ncommands package is present_release"""
        set_environment()

        nrobo_util_commands_ncommands_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboConst.NROBO / NroboPaths.GUI_PKG
        )

        assert nrobo_util_commands_ncommands_pkg_path.exists()

    def test_util_commands_posix_pkg_is_present(self):
        """Validate that nrobo.util.commands.posix package is present_release"""
        set_environment()

        nrobo_util_commands_posix_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_POSIX_PKG
        )

        assert nrobo_util_commands_posix_pkg_path.exists()

    def test_util_commands_windows_pkg_is_present(self):
        """Validate that nrobo.util.commands.windows package is present_release"""
        set_environment()

        nrobo_util_commands_windows_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_WINDOWS_PKG
        )

        assert nrobo_util_commands_windows_pkg_path.exists()

    def test_util_commands_pkg_is_present(self):
        """Validate that nrobo.util.commands package is present_release"""
        set_environment()

        nrobo_util_commands_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboConst.NROBO
            / NroboPaths.UTIL
            / NroboPaths.COMMANDS
            / NroboPaths.INIT_PY
        )

        assert nrobo_util_commands_pkg_path.exists()

    def test_util_common_pkg_is_present(self):
        """Validate that nrobo.util.common package is present_release"""
        set_environment()

        nrobo_util_common_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_COMMON_PKG
        )

        assert nrobo_util_common_pkg_path.exists()

    def test_util_constants_pkg_is_present(self):
        """Validate that nrobo.util.constant package is present_release"""
        set_environment()

        nrobo_util_constants_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_CONSTANT_PKG
        )

        assert nrobo_util_constants_pkg_path.exists()

    def test_util_filesystem_pkg_is_present(self):
        """Validate that nrobo.util.filesystem package is present_release"""
        set_environment()

        nrobo_util_filesystem_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_FILESYSTEM_PKG
        )

        assert nrobo_util_filesystem_pkg_path.exists()

    def test_util_network_pkg_is_present(self):
        """Validate that nrobo.util.network package is present_release"""
        set_environment()

        nrobo_util_network_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_NETWORK_PKG
        )

        assert nrobo_util_network_pkg_path.exists()

    def test_util_platform_pkg_is_present(self):
        """Validate that nrobo.util.platform package is present_release"""
        set_environment()

        nrobo_util_platform_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_PLATFORM_PKG
        )

        assert nrobo_util_platform_pkg_path.exists()

    def test_util_process_pkg_is_present(self):
        """Validate that nrobo.util.process package is present_release"""
        set_environment()

        nrobo_util_process_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_PROCESS_PKG
        )

        assert nrobo_util_process_pkg_path.exists()

    def test_util_python_pkg_is_present(self):
        """Validate that nrobo.util.python package is present_release"""
        set_environment()

        nrobo_util_python_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_PYTHON_PKG
        )

        assert nrobo_util_python_pkg_path.exists()

    def test_util_regex_pkg_is_present(self):
        """Validate that nrobo.util.regex package is present_release"""
        set_environment()

        nrobo_util_regex_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_REGEX_PKG
        )

        assert nrobo_util_regex_pkg_path.exists()

    def test_util_version_pkg_is_present(self):
        """Validate that nrobo.util.version package is present_release"""
        set_environment()

        nrobo_util_version_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.UTIL_VERSION_PKG
        )

        assert nrobo_util_version_pkg_path.exists()

    def test_nrobo_framework_tests_pkg_is_present(self):
        """Validate that nrobo_framework_tests package is present_release"""
        set_environment()

        nrobo_framework_tests_pkg_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.NROBO_FRAMEWORK_TESTS
        )

        assert nrobo_framework_tests_pkg_path.exists()

        nrobo_framework_tests_pkg_init_path = (
            nrobo_framework_tests_pkg_path / NroboPaths.INIT_PY
        )

        assert nrobo_framework_tests_pkg_init_path.exists()

    @pytest.mark.skip
    def test_nrobo_framework_tests_conftest_py_file_is_present(self):
        """Validate that nrobo_framework_tests.conftest.py file is present_release"""
        set_environment()

        nrobo_framework_tests_conftest_py_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboFrameworkTests.NROBO_FRAMEWORK_TESTS_CONFTEST_PY_FILE
        )

        assert nrobo_framework_tests_conftest_py_file_path.exists()

    def test_test_nrobo_framework_py_file_is_present(self):
        """Validate that nrobo_framework_tests.test_package_presence.py file is present_release"""
        set_environment()

        test_nrobo_framework_py_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR])
            / NroboFrameworkTests.TEST_NROBO_FRAMEWORK_PY_FILE
        )

        assert test_nrobo_framework_py_file_path.exists()

    def test_tests_pkg_is_present(self):
        """Validate that tests package is present_release"""
        set_environment()

        tests_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.TESTS

        assert tests_pkg_path.exists()

        tests_pkg_init_path = tests_pkg_path / NroboPaths.INIT_PY

        assert tests_pkg_init_path.exists()

    def test_versions_folder_is_present(self):
        """Validate that versions directory is present_release"""
        set_environment()

        versions_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.VERSIONS

        assert versions_path.exists()

    def test_versions_prod_yaml_file_is_present(self):
        """Validate that version/prod.yaml file is present_release"""
        set_environment()

        prod_yaml_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.PROD_YAML

        assert prod_yaml_file_path.exists()

    def test_test_versions_test_yaml_file_is_present(self):
        """Validate that versions/test.yaml file is present_release"""
        set_environment()

        test_yaml_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.TEST_YAML

        assert test_yaml_file_path.exists()

    def test_license_file_is_present(self):
        """Validate that LICENSE file is present_release"""
        set_environment()

        license_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.LICENSE_FILE

        assert license_file_path.exists()

    def test_nrobo_py_file_is_present(self):
        """Validate that nrobo.py file is present_release"""
        set_environment()

        nrobo_py_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.NROBO_PY_FILE
        )

        assert nrobo_py_file_path.exists()

    def test_package_py_file_is_present(self):
        """Validate that package.py file is present_release"""
        set_environment()

        package_py_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.PACKAGE_PY_FILE
        )

        assert package_py_file_path.exists()

    def test_pyproject_toml_file_is_present(self):
        """Validate that pyproject.toml file is present_release"""
        set_environment()

        pyproject_toml_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.PY_PROJECT_TOML_FILE
        )

        assert pyproject_toml_file_path.exists()

    def test_readme_rst_file_is_present(self):
        """Validate that README.rst file is present_release"""
        set_environment()

        readme_rst_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.README_RST_FILE
        )

        assert readme_rst_file_path.exists()

    def test_validate_nrobo_py_file_is_present(self):
        """Validate that validate.py file is present_release"""
        set_environment()

        validate_nrob_py_file_path = (
            Path(os.environ[EnvKeys.EXEC_DIR]) / NroboPaths.VALIDATE_NROBO_PY_FILE
        )

        assert validate_nrob_py_file_path.exists()
