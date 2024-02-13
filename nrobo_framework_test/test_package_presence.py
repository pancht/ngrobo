import os
import subprocess
from pathlib import Path

import pytest

from nrobo.cli.nglobals import Browsers
from nrobo.util.process import terminal
from nrobo import set_environment, EnvKeys, NROBO_CONST, NROBO_PATHS, NROBO_CLI_TOOL_PATH, NROBO_FRAMEWORK_TESTS
from nrobo.cli.cli_constants import NREPORT


class TestNRoboFrameworkPaths():
    """nRobo tests"""

    def test_cli_package_is_present(self):
        """Validate that cli package is present"""
        set_environment()

        cli_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.CLI

        assert cli_pkg_path.exists() == True

        cli_pkg_init_path = cli_pkg_path / NROBO_PATHS.INIT_PY

        assert cli_pkg_init_path.exists() == True

    def test_build_pkg_is_present(self):
        """Validate that build package is present"""
        set_environment()

        build_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CLI_TOOL_PATH.BUILD

        assert build_pkg_path.exists() == True

        build_pkg_init_path = build_pkg_path / NROBO_PATHS.INIT_PY

        assert build_pkg_init_path.exists() == True

    def test_check_pkg_is_present(self):
        """Validate that check package is present"""
        set_environment()

        check_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CLI_TOOL_PATH.CHECK

        assert check_pkg_path.exists() == True

        check_pkg_init_path = check_pkg_path / NROBO_PATHS.INIT_PY

        assert check_pkg_init_path.exists() == True

    def test_compile_pkg_is_present(self):
        """Validate that compile package is present"""
        set_environment()

        compile_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CLI_TOOL_PATH.COMPILE

        assert compile_pkg_path.exists() == True

        compile_pkg_init_path = compile_pkg_path / NROBO_PATHS.INIT_PY

        assert compile_pkg_init_path.exists() == True

    def test_development_pkg_is_present(self):
        """Validate that development package is present"""
        set_environment()

        development_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CLI_TOOL_PATH.DEVELOPMENT

        assert development_pkg_path.exists() == True

        development_pkg_init_path = development_pkg_path / NROBO_PATHS.INIT_PY

        assert development_pkg_init_path.exists() == True

    def test_publish_pkg_is_present(self):
        """Validate that publish package is present"""
        set_environment()

        publish_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CLI_TOOL_PATH.PUBLISH

        assert publish_pkg_path.exists() == True

        publish_pkg_init_path = publish_pkg_path / NROBO_PATHS.INIT_PY

        assert publish_pkg_init_path.exists() == True

    def test_browser_configs_chrome_pkg_is_present(self):
        """Validate that browserConfigs.chrome package is present"""
        set_environment()

        browserConfigs_chrome_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.BROWSERS_CHROME_PKG

        assert browserConfigs_chrome_pkg_path.exists() == True

        browserConfigs_chrome_pkg_init_path = browserConfigs_chrome_pkg_path / NROBO_PATHS.INIT_PY

        assert browserConfigs_chrome_pkg_init_path.exists() == True

    def test_browsers_edge_pkg_is_present(self):
        """Validate that browsers.edge package is present"""
        set_environment()

        browsers_edge_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.BROWSERS_EDGE_PKG

        assert browsers_edge_pkg_path.exists() == True

        browsers_edge_pkg_init_path = browsers_edge_pkg_path / NROBO_PATHS.INIT_PY

        assert browsers_edge_pkg_init_path.exists() == True

    def test_browsers_firefox_pkg_is_present(self):
        """Validate that browsers.firefox package is present"""
        set_environment()

        browsers_firefox_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.BROWSERS_FIREFOX_PKG

        assert browsers_firefox_pkg_path.exists() == True

        browsers_firefox_pkg_init_path = browsers_firefox_pkg_path / NROBO_PATHS.INIT_PY

        assert browsers_firefox_pkg_init_path.exists() == True

    def test_browsers_safari_pkg_is_present(self):
        """Validate that browsers.safari package is present"""
        set_environment()

        browsers_safari_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.BROWSERS_CHROME_PKG

        assert browsers_safari_pkg_path.exists() == True

        browsers_safari_pkg_init_path = browsers_safari_pkg_path / NROBO_PATHS.INIT_PY

        assert browsers_safari_pkg_init_path.exists() == True

    def test_cli_formatting_pkg_is_present(self):
        """Validate that cli.formatting package is present"""
        set_environment()

        cli_formatting_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.FORMATTING_PKG

        assert cli_formatting_pkg_path.exists() == True

    def test_cli_install_pkg_is_present(self):
        """Validate that cli.install package is present"""
        set_environment()

        cli_install_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.INSTALL_PKG

        assert cli_install_pkg_path.exists() == True

    def test_cli_install_requirements_txt_file_is_present(self):
        """Validate that cli.tools.requirements.txt file is present"""
        set_environment()

        cli_install_requirements_txt_file_pkg_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.REQUIREMENTS_TXT_FILE

        assert cli_install_requirements_txt_file_pkg_path.exists() == True

    def test_cli_tools_pkg_is_present(self):
        """Validate that cli.tools package is present"""
        set_environment()

        cli_tools_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.CLI_TOOLS_PKG

        assert cli_tools_pkg_path.exists() == True

    def test_cli_upgrade_pkg_is_present(self):
        """Validate that cli.upgrade package is present"""
        set_environment()

        cli_upgrade_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.UPGRADE_PKG

        assert cli_upgrade_pkg_path.exists() == True

    def test_cli_cli_args_py_file_is_present(self):
        """Validate that cli.cli_args.py file is present"""
        set_environment()

        cli_cli_args_py_file_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.CLI_ARGS_PY_FILE

        assert cli_cli_args_py_file_pkg_path.exists() == True

    def test_cli_constants_py_file_is_present(self):
        """Validate that cli.cli_constants.py file is present"""
        set_environment()

        cli_cli_constants_py_file_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.CLI_CONSTANTS_PY_FILE

        assert cli_cli_constants_py_file_pkg_path.exists() == True

    def test_cli_cli_version_yaml_file_is_present(self):
        """Validate that cli.version.yaml file is present"""
        set_environment()

        cli_cli_version_yaml_file_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.CLI_VERSION_YAML_FILE

        assert cli_cli_version_yaml_file_pkg_path.exists() == True

    def test_cli_nglobals_py_file_is_present(self):
        """Validate that cli.nglobals.py file is present"""
        set_environment()

        cli_nglobals_py_file_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.NGLOBALS_PY_FILE

        assert cli_nglobals_py_file_pkg_path.exists() == True

    def test_conftest_py_file_present_in_root(self):
        """Validate that conftest.py is present in root dir"""

        set_environment()

        conftest_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.CONFTEST_PY

        assert conftest_path.exists() == True

    def test_conftest_py_present_in_project_root_package(self):
        """Validate that conftest.py is present in the nrobo project root directory"""

        set_environment()

        conftest_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.CONFTEST_PY

        assert conftest_path.exists() == True

    def test_browser_config_package_is_present(self):
        """Validate that browserConfig package is present"""
        set_environment()

        browser_config_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.BROWSER_CONFIGS

        assert browser_config_path.exists() == True

        browser_config_init_path = browser_config_path / NROBO_PATHS.INIT_PY

        assert browser_config_init_path.exists() == True

    def test_browsers_package_is_present(self):
        """Validate that browsers package is present"""
        set_environment()

        browsers_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.BROWSERS

        assert browsers_path.exists() == True

        browsers_init_path = browsers_path / NROBO_PATHS.INIT_PY

        assert browsers_init_path.exists() == True

    def test_cli_package_is_present(self):
        """Validate that cli package is present"""
        set_environment()

        cli_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.CLI

        assert cli_path.exists() == True

        cli_init_path = cli_path / NROBO_PATHS.INIT_PY

        assert cli_init_path.exists() == True

    def test_exceptions_package_is_present(self):
        """Validate that exceptions package is present"""
        set_environment()

        excepations_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.EXCEPTIONS

        assert excepations_pkg_path.exists() == True

        exceptions_pkg_init_path = excepations_pkg_path / NROBO_PATHS.INIT_PY

        assert exceptions_pkg_init_path.exists() == True

    def test_framework_pkg_is_present(self):
        """Validate that framework package is present"""
        set_environment()

        framework_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.FRAMEWORK

        assert framework_pkg_path.exists() == True

        framework_pkg_init_path = framework_pkg_path / NROBO_PATHS.INIT_PY

        assert framework_pkg_init_path.exists() == True

    def test_framework_pages_pkg_is_present(self):
        """Validate that nrobo.framework.pages package is present"""
        set_environment()

        nrobo_framework_pages_pkg_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.FRAMEWORK_PAGES

        assert nrobo_framework_pages_pkg_path.exists() == True

    def test_framework_pages_page_demo_py_file_is_present(self):
        """Validate that nrobo.framework.pages.PageDemo.py file is present"""
        set_environment()

        nrobo_framework_pages_page_demo_py_file_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.FRAMEWORK_PAGES_PAGE_DEMO_PY_FILE

        assert nrobo_framework_pages_page_demo_py_file_path.exists() == True

    def test_framework_tests_gui_pkg_is_present(self):
        """Validate that nrobo.framework.tests.gui package is present"""
        set_environment()

        nrobo_framework_tests_gui_pkg_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.GUI_PKG

        assert nrobo_framework_tests_gui_pkg_path.exists() == True

    def test_framework_tests_nogui_pkg_is_present(self):
        """Validate that nrobo.framework.tests.no_gui package is present"""
        set_environment()

        nrobo_framework_tests_no_gui_pkg_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.FRAMEWORK / NROBO_PATHS.NO_GUI_PKG

        assert nrobo_framework_tests_no_gui_pkg_path.exists() == True

    def test_framework_tests_gui_google_home_page_test_py_file_is_present(self):
        """Validate that nrobo.framework.tests.gui.google_home_page_test.py file is present"""
        set_environment()

        nrobo_framework_tests_gui_google_home_page_test_py_file_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.GUI_GOOGLE_HOME_PAGE_TEST_PY_FILE

        assert nrobo_framework_tests_gui_google_home_page_test_py_file_path.exists() == True

    def test_framework_tests_pkg_is_present(self):
        """Validate that nrobo.framework.tests package is present"""
        set_environment()

        nrobo_framework_tests_pkg_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.FRAMEWORK_TESTS / NROBO_PATHS.INIT_PY

        assert nrobo_framework_tests_pkg_path.exists() == True

    def test_framework_nrobo_config_yaml_file_is_present(self):
        """Validate that nrobo.framework.nrobo-config.yaml file is present"""
        set_environment()

        nrobo_framework_nrobo_config_yaml_file_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.FRAMEWORK_NROBO_CONFIG

        assert nrobo_framework_nrobo_config_yaml_file_path.exists() == True

    def test_selenes_pkg_is_present(self):
        """Validate that selenes pkg is present"""
        set_environment()

        selenes_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.SELENESE

        assert selenes_pkg_path.exists() == True

        selenes_pkg_init_path = selenes_pkg_path / NROBO_PATHS.INIT_PY

        assert selenes_pkg_init_path.exists() == True

    def test_util_pkg_is_present(self):
        """Validate that util package is present"""
        set_environment()

        util_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.UTIL

        assert util_pkg_path.exists() == True

        util_pkg_init_path = util_pkg_path / NROBO_PATHS.INIT_PY

        assert util_pkg_init_path.exists() == True

    def test_util_commands_ncommands_pkg_is_present(self):
        """Validate that nrobo.util.commands.ncommands package is present"""
        set_environment()

        nrobo_util_commands_ncommands_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / NROBO_PATHS.GUI_PKG

        assert nrobo_util_commands_ncommands_pkg_path.exists() == True

    def test_util_commands_posix_pkg_is_present(self):
        """Validate that nrobo.util.commands.posix package is present"""
        set_environment()

        nrobo_util_commands_posix_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.UTIL_POSIX_PKG

        assert nrobo_util_commands_posix_pkg_path.exists() == True

    def test_util_commands_windows_pkg_is_present(self):
        """Validate that nrobo.util.commands.windows package is present"""
        set_environment()

        nrobo_util_commands_windows_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.UTIL_WINDOWS_PKG

        assert nrobo_util_commands_windows_pkg_path.exists() == True

    def test_util_commands_pkg_is_present(self):
        """Validate that nrobo.util.commands package is present"""
        set_environment()

        nrobo_util_commands_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_CONST.NROBO / \
                                       NROBO_PATHS.UTIL / NROBO_PATHS.COMMANDS / NROBO_PATHS.INIT_PY

        assert nrobo_util_commands_pkg_path.exists() == True

    def test_util_common_pkg_is_present(self):
        """Validate that nrobo.util.common package is present"""
        set_environment()

        nrobo_util_common_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.UTIL_COMMON_PKG

        assert nrobo_util_common_pkg_path.exists() == True

    def test_util_constants_pkg_is_present(self):
        """Validate that nrobo.util.constant package is present"""
        set_environment()

        nrobo_util_constants_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.UTIL_CONSTANT_PKG

        assert nrobo_util_constants_pkg_path.exists() == True

    def test_util_filesystem_pkg_is_present(self):
        """Validate that nrobo.util.filesystem package is present"""
        set_environment()

        nrobo_util_filesystem_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.UTIL_FILESYSTEM_PKG

        assert nrobo_util_filesystem_pkg_path.exists() == True

    def test_util_platform_pkg_is_present(self):
        """Validate that nrobo.util.platform package is present"""
        set_environment()

        nrobo_util_platform_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.UTIL_PLATFORM_PKG

        assert nrobo_util_platform_pkg_path.exists() == True

    def test_util_process_pkg_is_present(self):
        """Validate that nrobo.util.process package is present"""
        set_environment()

        nrobo_util_process_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.UTIL_PROCESS_PKG

        assert nrobo_util_process_pkg_path.exists() == True

    def test_util_python_pkg_is_present(self):
        """Validate that nrobo.util.python package is present"""
        set_environment()

        nrobo_util_python_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.UTIL_PYTHON_PKG

        assert nrobo_util_python_pkg_path.exists() == True

    def test_nrobo_framework_tests_pkg_is_present(self):
        """Validate that nrobo_framework_tests package is present"""
        set_environment()

        nrobo_framework_tests_pkg_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.NROBO_FRAMEWORK_TESTS

        assert nrobo_framework_tests_pkg_path.exists() == True

        nrobo_framework_tests_pkg_init_path = nrobo_framework_tests_pkg_path / NROBO_PATHS.INIT_PY

        assert nrobo_framework_tests_pkg_init_path.exists() == True

    def test_nrobo_framework_tests_conftest_py_file_is_present(self):
        """Validate that nrobo_framework_tests.conftest.py file is present"""
        set_environment()

        nrobo_framework_tests_conftest_py_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_FRAMEWORK_TESTS.NROBO_FRAMEWORK_TESTS_CONFTEST_PY_FILE

        assert nrobo_framework_tests_conftest_py_file_path.exists() == True

    def test_test_nrobo_framework_py_file_is_present(self):
        """Validate that nrobo_framework_tests.test_package_presence.py file is present"""
        set_environment()

        test_nrobo_framework_py_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_FRAMEWORK_TESTS.TEST_NROBO_FRAMEWORK_PY_FILE

        assert test_nrobo_framework_py_file_path.exists() == True
    def test_tests_pkg_is_present(self):
        """Validate that tests package is present"""
        set_environment()

        tests_pkg_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.TESTS

        assert tests_pkg_path.exists() == True

        tests_pkg_init_path = tests_pkg_path / NROBO_PATHS.INIT_PY

        assert tests_pkg_init_path.exists() == True

    def test_versions_folder_is_present(self):
        """Validate that versions directory is present"""
        set_environment()

        versions_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.VERSIONS

        assert versions_path.exists() == True

    def test_versions_prod_yaml_file_is_present(self):
        """Validate that version/prod.yaml file is present"""
        set_environment()

        prod_yaml_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.PROD_YAML

        assert prod_yaml_file_path.exists() == True

    def test_test_versions_test_yaml_file_is_present(self):
        """Validate that versions/test.yaml file is present"""
        set_environment()

        test_yaml_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.TEST_YAML

        assert test_yaml_file_path.exists() == True

    def test_license_file_is_present(self):
        """Validate that LICENSE file is present"""
        set_environment()

        license_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.LICENSE_FILE

        assert license_file_path.exists() == True

    def test_nrobo_py_file_is_present(self):
        """Validate that nrobo.py file is present"""
        set_environment()

        nrobo_py_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.NROBO_PY_FILE

        assert nrobo_py_file_path.exists() == True

    def test_package_py_file_is_present(self):
        """Validate that package.py file is present"""
        set_environment()

        package_py_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.PACKAGE_PY_FILE

        assert package_py_file_path.exists() == True

    def test_pyproject_toml_file_is_present(self):
        """Validate that pyproject.toml file is present"""
        set_environment()

        pyproject_toml_file_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.PY_PROJECT_TOML_FILE

        assert pyproject_toml_file_path.exists() == True

    def test_readme_rst_file_is_present(self):
        """Validate that README.rst file is present"""
        set_environment()

        readme_rst_file_path = Path(os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.README_RST_FILE

        assert readme_rst_file_path.exists() == True

    def test_validate_nrobo_py_file_is_present(self):
        """Validate that validate.py file is present"""
        set_environment()

        validate_nrob_py_file_path = Path(
            os.environ[EnvKeys.EXEC_DIR]) / NROBO_PATHS.VALIDATE_NROBO_PY_FILE

        assert validate_nrob_py_file_path.exists() == True