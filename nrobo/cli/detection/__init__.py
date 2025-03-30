"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Detection module has methods to detect environment,
nRoBo installation and many more...


@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

import os

from nrobo import EnvKeys, Environment
from nrobo import NroboPaths
from nrobo.util.constants import Ext
from nrobo.util.common import Common
from cli.build import EnvCliSwitch


def developer_machine() -> bool:
    """Return true if Developer machine else False"""
    if (NroboPaths.EXEC_DIR / NroboPaths.PY_PROJECT_TOML_FILE).exists():
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


def host_machine_has_nrobo() -> bool:
    """Returns True if host machine has nRoBo installed already else False"""
    if (NroboPaths.EXEC_DIR / NroboPaths.CONFTEST_PY).exists():
        # if conftest file found on production_machine system,
        # meaning nrobo is already installed there
        return True

    return False


def build_version_from_version_files() -> str:
    """Return build version from version files."""

    # Grab version number from version yaml files in version/ directory
    return Common.read_yaml(
        NroboPaths.VERSIONS / f"{EnvCliSwitch.PROD}{Ext.YAML}", fail_on_failure=False
    )["version"]


def ensure_pathces_dir() -> None:
    """Ensures that patches dir is present on Host machine"""

    if production_machine() and not developer_machine():
        if not (NroboPaths.NROBO_DIR / NroboPaths.PATCHES).exists():
            os.mkdir(NroboPaths.NROBO_DIR / NroboPaths.PATCHES)
