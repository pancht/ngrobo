"""
This module loads nRoBo globals.
"""
import os
from pathlib import Path

from nrobo.util.constants import CONST


class N_DIRS:
    """nRoBo framework directories and files"""
    NROBO = Path("nrobo")
    BROWSER_CONFIS = Path("browserConfigs")
    BROWSERS = Path("browsers")
    CLI = Path("cli")
    EXCEPTIONS = Path("exceptions")
    FRAMEWORK = Path("framework")
    FRAMEWORK_PAGES = FRAMEWORK / "pages"
    FRAMEWORK_TESTS = FRAMEWORK / "tests"
    FRAMEWORK_NROBO_CONFIG = FRAMEWORK / "nrobo-config.yaml"
    SELENESE = Path("selenese")
    UTIL = Path("util")
    CONFTEST_PY = Path("conftest.py")


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


# load environment keys with defaults
os.environ[EnvKeys.PIP_COMMAND] = Python.PIP
os.environ[EnvKeys.EXEC_DIR] = CONST.EMPTY
os.environ[EnvKeys.NROBO_DIR] = CONST.EMPTY
os.environ[EnvKeys.ENVIRONMENT] = Environment.DEVELOPMENT
