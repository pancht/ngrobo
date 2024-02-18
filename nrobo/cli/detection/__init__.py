import os
from pathlib import Path

from nrobo import EnvKeys, Environment
from nrobo import NROBO_PATHS as NP


def developer_machine() -> bool:
    """Return true if Developer machine else False"""
    if Path(Path(os.environ[EnvKeys.EXEC_DIR]) / NP.PY_PROJECT_TOML_FILE).exists():
        return True

    return False


def production_machine() -> bool:
    """Return true if host machine is in production else false."""
    if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION:
        return True

    return False


def a_success(code) -> bool:
    """Return True if code is non-zero (especially in case of command execution) else False"""
    if code:
        return True

    return False


def development_machine() -> bool:
    """Return true if host machine is in a developer machine else false."""
    if os.environ[EnvKeys.ENVIRONMENT] == Environment.DEVELOPMENT:
        return True

    return False


def host_machine_has_nRoBo() -> bool:
    """Returns True if host machine has nRoBo installed already else False"""
    if Path(Path(os.environ[EnvKeys.EXEC_DIR]) / NP.CONFTEST_PY).exists():
        # if conftest file found on production_machine system, meaning nrobo is already installed there
        return True

    return False
