"""
This module loads nRoBo globals.
"""
import os
from pathlib import Path
import re
from rich.console import Console
from nrobo.cli.formatting import themes as th, STYLE

from nrobo.util.constants import CONST
from nrobo.cli.tools import *


console = Console(theme=th)


class NROBO_PATHS:
    """nRoBo framework directories and files"""
    NROBO = Path("nrobo")
    INIT_PY = Path("__init__.py")
    BROWSER_CONFIS = Path("browserConfigs")
    BROWSERS = Path("browsers")
    CLI = Path("cli")
    EXCEPTIONS = Path("exceptions")
    FRAMEWORK = Path("framework")
    PAGES = Path("pages")
    FRAMEWORK_PAGES = FRAMEWORK / PAGES
    TESTS = Path("tests")
    FRAMEWORK_TESTS = FRAMEWORK / TESTS
    NROBO_CONFIG_FILE = Path("nrobo-config.yaml")
    FRAMEWORK_NROBO_CONFIG = FRAMEWORK / NROBO_CONFIG_FILE
    SELENESE = Path("selenese")
    UTIL = Path("util")
    CONFTEST_PY = Path("conftest.py")


class NROBO_CONST:
    """nrobo special constants"""

    NROBO = "nrobo"
    DIST_DIR = "dist"
    SUCCESS = 0


class Python:
    """Information related to python"""

    PIP = "pip"
    VERSION = "Version"


class Environment:
    """Environments"""

    PRODUCTION = "Production"
    DEVELOPMENT = "Development"


class EnvKeys:
    """nRoBo environment keys

    Example:
        PIP_COMMAND = pip | pip3

        and many more such...
    """
    PIP_COMMAND = "Pip Command"
    EXEC_DIR = "Execution Directory"
    NROBO_DIR = "nRoBo Installation Directory"
    ENVIRONMENT = "Environment"
    PYTHON = "Python"


# load environment keys with defaults
os.environ[EnvKeys.PIP_COMMAND] = Python.PIP
os.environ[EnvKeys.EXEC_DIR] = CONST.EMPTY
os.environ[EnvKeys.NROBO_DIR] = CONST.EMPTY
os.environ[EnvKeys.ENVIRONMENT] = Environment.DEVELOPMENT
os.environ[EnvKeys.PYTHON] = "python"


def greet_the_guest():
    """greet the guest with Indian way of greeting!"""

    greet_msg = 'Namastey Wolrd!. Thank you for choosing, NROBO.'.format(CONST.NEWLINE)
    formatted_heart_string = CONST.HEART_RED * (len(greet_msg) // 2)

    console.print(f'\n[{STYLE.HLRed}]{formatted_heart_string}'
                  f'\n[{STYLE.HLOrange}]{greet_msg}'
                  f'\n[{STYLE.HLRed}]{formatted_heart_string}')


def set_environment() -> None:
    """set nrobo environment"""

    # get directory from where the script was executed
    os.environ[EnvKeys.EXEC_DIR] = os.getcwd()
    # get directory where this script resides
    nrobo_loader_file_path = os.path.dirname(os.path.realpath(__file__))
    # grab nrobo installation path
    os.environ[EnvKeys.NROBO_DIR] = re.findall(f"(.*{NROBO_CONST.NROBO})", str(nrobo_loader_file_path))[0]

    if os.path.exists(Path(os.environ[EnvKeys.EXEC_DIR] / NROBO_PATHS.NROBO)):
        os.environ[EnvKeys.ENVIRONMENT] = Environment.DEVELOPMENT
    else:
        os.environ[EnvKeys.ENVIRONMENT] = Environment.PRODUCTION
