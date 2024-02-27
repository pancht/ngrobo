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
from pathlib import Path

from nrobo import EnvKeys, Environment
from nrobo import NROBO_PATHS
from nrobo.util.constants import EXT


def developer_machine() -> bool:
    """Return true if Developer machine else False"""
    if (NROBO_PATHS.EXEC_DIR / NROBO_PATHS.PY_PROJECT_TOML_FILE).exists():
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
    if (NROBO_PATHS.EXEC_DIR / NROBO_PATHS.CONFTEST_PY).exists():
        # if conftest file found on production_machine system, meaning nrobo is already installed there
        return True

    return False


def build_version_from_version_files() -> str:
    """Return build version from version files."""
    from nrobo.util.common import Common
    from nrobo import NROBO_PATHS
    from cli.build import ENV_CLI_SWITCH
    # Grab version number from version yaml files in version/ directory
    return Common.read_yaml(NROBO_PATHS.VERSIONS / f"{ENV_CLI_SWITCH.PROD}{EXT.YAML}", fail_on_failure=False)['version']


def ensure_pathces_dir() -> bool:
    """Ensures that patches dir is present on Host machine"""
    from nrobo import NROBO_PATHS
    import nrobo.cli.detection as detect

    if detect.production_machine() and not detect.developer_machine():
        if not (NROBO_PATHS.NROBO_DIR / NROBO_PATHS.PATCHES).exists():
            os.mkdir(NROBO_PATHS.NROBO_DIR / NROBO_PATHS.PATCHES)
