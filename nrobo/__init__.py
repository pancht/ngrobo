"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================


nrobo module loads nRoBo globals.


@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

__version__ = '2025.0.0'

# install rich library
import os
from pathlib import Path
import re
from dataclasses import dataclass
import subprocess
from rich.console import Console
from nrobo.util.process import terminal
from nrobo.cli.formatting import themes as th, STYLE
from nrobo.util.constants import Const


@dataclass
class DbConnectorType:
    """Database Connector Types"""

    MYSQL = "mysql"


@dataclass
class NroboConst:
    """nrobo special constants"""

    NROBO = "nrobo"
    DIST_DIR = "dist"
    SUCCESS = 0


@dataclass
class Python:
    """Information related to python"""

    PIP = "pip"
    VERSION = "Version"
    PYPINFO = "pypinfo"


@dataclass
class Environment:
    """Environments"""

    PRODUCTION = "Production"
    DEVELOPMENT = "Development"


@dataclass
class EnvKeys:
    """nRoBo environment keys

    Example:
        PIP_COMMAND = pip | pip3

        and many more such...
    """

    APPIUM = "appium"
    PIP_COMMAND = "Pip Command"
    EXEC_DIR = "Execution Directory"
    NROBO_DIR = "nRoBo Installation Directory"
    ENVIRONMENT = "Environment"
    PYTHON = "Python"
    APP = "App Name"
    URL = "App Url"
    USERNAME = "Username"
    PASSWORD = "Password"
    TITLE = "Title"
    BROWSER = "Browser"
    HOST_PLATFORM = "Host Platform"
    DEBUG = "debug mode"
    SUPPRESS_PROMPT = "suppress prompt"


# load environment keys with defaults
os.environ[EnvKeys.APPIUM] = "0"
os.environ[EnvKeys.PIP_COMMAND] = Python.PIP
os.environ[EnvKeys.EXEC_DIR] = ""
os.environ[EnvKeys.NROBO_DIR] = ""
os.environ[EnvKeys.ENVIRONMENT] = Environment.DEVELOPMENT
os.environ[EnvKeys.PYTHON] = "python"
os.environ[EnvKeys.APP] = "nRoBo"
os.environ[EnvKeys.URL] = ""
os.environ[EnvKeys.USERNAME] = ""
os.environ[EnvKeys.PASSWORD] = ""
os.environ[EnvKeys.TITLE] = ""
os.environ[EnvKeys.BROWSER] = ""
os.environ[EnvKeys.HOST_PLATFORM] = ""
os.environ[EnvKeys.DEBUG] = "False"
os.environ[EnvKeys.SUPPRESS_PROMPT] = "0"


@dataclass
class NroboPaths:
    """nRoBo framework directories and files"""

    EXEC_DIR = Path(os.environ[EnvKeys.EXEC_DIR])
    NROBO_DIR = Path(os.environ[EnvKeys.NROBO_DIR])
    NODE_MODULES = Path("node_modules")
    PATCHES = Path("patches")
    NROBO = Path("nrobo")
    INIT_PY = Path("__init__.py")
    APPIUM = Path("appium")
    BROWSER_CONFIGS = Path("browser_configs")
    CAPABILITY_YAML = BROWSER_CONFIGS / "capability.yaml"
    CAPABILITY_APPIUM_ANDROID_YAML = APPIUM / "android_capability.yaml"
    CAPABILITY_APPIUM_IOS_YAML = APPIUM / "ios_capability.yaml"
    MARKERS_YAML = BROWSER_CONFIGS / "markers.yaml"

    # Browsers packages
    BROWSERS = Path("browsers")
    CHROME = Path("chrome")
    BROWSERS_CHROME_PKG = BROWSERS / CHROME
    EDGE = Path("edge")
    BROWSERS_EDGE_PKG = BROWSERS / EDGE
    FIREFOX = Path("firefox")
    BROWSERS_FIREFOX_PKG = BROWSERS / FIREFOX
    SAFARI = Path("safari")
    BROWSERS_SAFARI_PKG = BROWSERS / SAFARI

    # cli packages
    CLI = Path("cli")
    CLI_PKG = CLI / INIT_PY
    DETECTION = Path("detection")
    DETECTION_PKG = CLI / DETECTION / INIT_PY
    FORMATTING = Path("formatting")
    FORMATTING_PKG = CLI / FORMATTING / INIT_PY
    INSTALL = Path("install")
    INSTALL_PKG = CLI / INSTALL / INIT_PY
    NCODES = Path("ncodes")
    NCODES_PKG = CLI / NCODES / INIT_PY
    REQUIREMENTS_TXT_FILE = Path("requirements.txt")
    REQUIREMENTS_TXT_FILE_CLI = CLI / INSTALL / REQUIREMENTS_TXT_FILE
    CLI_NROBO_ARGS = Path("nrobo_args")
    CLI_NROBO_ARGS_PKG = CLI / CLI_NROBO_ARGS / INIT_PY
    CLI_TOOLS = Path("tools")
    CLI_TOOLS_PKG = CLI / CLI_TOOLS / INIT_PY
    UPGRADE = Path("upgrade")
    UPGRADE_PKG = CLI / UPGRADE / INIT_PY
    CLI_LAUNCHER_PY_FILE = CLI / Path("launcher.py")
    CLI_CONSTANTS_PY_FILE = CLI / Path("cli_constants.py")
    CLI_VERSION_YAML_FILE = CLI / Path("cli_version.yaml")
    NGLOBALS_PY_FILE = CLI / Path("nglobals.py")

    EXCEPTIONS = Path("exceptions")

    # framework packages
    FRAMEWORK = Path("framework")
    PAGES = Path("pages")
    TEST_DATA = Path("test_data")
    FRAMEWORK_PAGES = FRAMEWORK / PAGES
    FRAMEWORK_PAGE_PYPI_HOME_PY_FILE = FRAMEWORK_PAGES / Path("page_pypi_home.py")
    TESTS = Path("tests")
    MOBILE = Path("mobile")
    WEB = Path("web")
    FRAMEWORK_TESTS = FRAMEWORK / TESTS
    GUI = FRAMEWORK_TESTS / WEB / Path("gui")
    GUI_PKG = GUI / INIT_PY
    GUI_PYPI_HOME_PAGE_TEST_PY_FILE = GUI / Path("PyPi_home_page_test.py")
    NO_GUI_PKG = TESTS / WEB / "no_gui" / INIT_PY

    FRAMEWORK_TESTS = FRAMEWORK / TESTS
    NROBO_CONFIG_FILE = Path("nrobo-config.yaml")
    FRAMEWORK_NROBO_CONFIG = FRAMEWORK / NROBO_CONFIG_FILE
    NROBO_CONFTEST_HOST_FILE = FRAMEWORK / "conftest_host.py"

    SELENESE = Path("selenese")

    # nrobo.util packages
    UTIL = Path("util")
    COMMANDS = Path("commands")
    NCOMMANDS = Path("ncommands")
    POSIX = Path("posix")
    WINDOWS = Path("windows")
    UTIL_NCOMMANDS_PKG = NROBO / UTIL / COMMANDS / NCOMMANDS / INIT_PY
    UTIL_POSIX_PKG = NROBO / UTIL / COMMANDS / POSIX / INIT_PY
    UTIL_WINDOWS_PKG = NROBO / UTIL / COMMANDS / WINDOWS / INIT_PY
    UTIL_COMMON = Path("common")
    UTIL_COMMON_PKG = NROBO / UTIL / UTIL_COMMON / INIT_PY
    UTIL_CONSTANT = Path("constants")
    UTIL_CONSTANT_PKG = NROBO / UTIL / UTIL_CONSTANT / INIT_PY
    UTIL_FILESYSTEM = Path("filesystem")
    UTIL_FILESYSTEM_PKG = NROBO / UTIL / UTIL_FILESYSTEM / INIT_PY
    UTIL_PLATFORM = Path("platform")
    UTIL_NETWORK = Path("network")
    UTIL_NETWORK_PKG = NROBO / UTIL / UTIL_NETWORK / INIT_PY
    UTIL_PLATFORM_PKG = NROBO / UTIL / UTIL_PLATFORM / INIT_PY
    UTIL_PROCESS = Path("process")
    UTIL_PROCESS_PKG = NROBO / UTIL / UTIL_PROCESS / INIT_PY
    UTIL_PYTHON = Path("python")
    UTIL_PYTHON_PKG = NROBO / UTIL / UTIL_PYTHON / INIT_PY
    UTIL_REGEX = Path("regex")
    UTIL_REGEX_PKG = NROBO / UTIL / UTIL_REGEX / INIT_PY
    UTIL_VERSION = Path("version")
    UTIL_VERSION_PKG = NROBO / UTIL / UTIL_VERSION / INIT_PY
    CONFTEST_PY = Path("conftest.py")

    NROBO_FRAMEWORK_TESTS = Path("framework_tests")
    TESTS = Path("tests")

    VERSIONS = Path("versions")
    PROD_YAML = VERSIONS / Path("prod.yaml")
    TEST_YAML = VERSIONS / Path("test.yaml")

    NROBO_PY_FILE = Path("nrobo.py")
    PACKAGE_PY_FILE = Path("package.py")
    LICENSE_FILE = Path("LICENSE")
    PY_PROJECT_TOML_FILE = Path("pyproject.toml")
    README_RST_FILE = Path("README.rst")
    VALIDATE_NROBO_PY_FILE = Path("validatenrobo.py")

    PYTEST_LIFE_CYCLE_LOGS = (
        Path("key") / "experiments" / "pytest" / "pytest-life-cycle-logs"
    )


@dataclass
class NroboCliToolPath:
    """nRoBo CLI tool paths"""

    CLI = Path("cli")
    BUILD = CLI / Path("build")
    CHECK = CLI / Path("check")
    COMPILE = CLI / Path("compile")
    DEVELOPMENT = CLI / Path("development")
    PUBLISH = CLI / Path("publish")


@dataclass
class NroboFrameworkTests:
    """nrobo_framework_tests package"""

    NROBO_FRAMEWORK_TESTS_CONFTEST_PY_FILE = (
        NroboPaths.NROBO_FRAMEWORK_TESTS / NroboPaths.CONFTEST_PY
    )
    TEST_NROBO_FRAMEWORK_PY_FILE = NroboPaths.NROBO_FRAMEWORK_TESTS / Path(
        "test_package_presence.py"
    )


terminal(
    ["pip", "install", "rich"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
)


# rich console
console = Console(theme=th)


def greet_the_guest():
    """greet the guest with Indian way of greeting!"""

    greet_msg = "Namastey World! Thank you for choosing, nRoBo."
    formatted_heart_string = Const.HEART_RED * len(greet_msg)

    console.print(f"[{STYLE.HLRed}]{formatted_heart_string}")
    console.print(f"[{STYLE.HLOrange}]{greet_msg}[/]")
    console.print(f"[{STYLE.HLRed}]{formatted_heart_string}")


def set_environment() -> None:
    """set nrobo environment

    Not complete implementation as the name suggests.
    This implementation will be corrected in future versions..."""

    # get directory from where the script was executed
    os.environ[EnvKeys.EXEC_DIR] = os.getcwd()
    # get directory where this script resides
    nrobo_loader_file_path = os.path.dirname(os.path.realpath(__file__))
    # grab nrobo installation path
    os.environ[EnvKeys.NROBO_DIR] = re.findall(
        f"(.*{NroboConst.NROBO})", str(nrobo_loader_file_path)
    )[0]

    NroboPaths.EXEC_DIR = Path(os.environ[EnvKeys.EXEC_DIR])
    NroboPaths.NROBO_DIR = Path(os.environ[EnvKeys.NROBO_DIR])
