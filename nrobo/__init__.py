"""
This module loads nRoBo globals.
"""
import os

from nrobo.util.constants import CONST


class Python:
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

