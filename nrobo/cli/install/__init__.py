"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Installer for installing nrobo framework at host system.


@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
import os
import shutil
import sys

from nrobo.cli import *
from nrobo.cli.cli_constants import *
from nrobo.cli.nglobals import *
from nrobo.cli.cli_args import *
from nrobo import *
from nrobo.util.filesystem import *
from nrobo.util.process import *


def install_nrobo(requirements_file: Optional[str] = None) -> None:
    """
    This will install nrobo framework and its dependencies on host system in the current directory
    from where nrobo command was executed in the Production environment.

    This will only install nrobo dependencies if it is executed in the Developer environment.

    :return: None
    """

    # Inline imports to handle circular import exception while importing partially initialized module
    from nrobo import set_environment, EnvKeys, Environment, NROBO_PATHS as NP
    set_environment()

    # if conftest file found on production system, meaning nrobo is already installed there
    nrobo_installed = Path(Path(os.environ[EnvKeys.EXEC_DIR]) / NP.CONFTEST_PY).exists()

    if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION\
            and not nrobo_installed:
        print(f"Installing requirements")

    if requirements_file is None:
        requirements_file = f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}cli{os.sep}install{os.sep}requirements.txt"

        return_code = terminal(command=[os.environ[EnvKeys.PIP_COMMAND], nCLI.INSTALL, '-r', requirements_file],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)

        if return_code == NROBO_CONST.SUCCESS:
            """return code zero means success"""
            if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION\
                    and not nrobo_installed:
                print(f"Requirements are installed successfully.")
        else:
            print(f"Requirements are not installed successfully!")
            exit()

    if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION:
        """Install or upgrading framework on Production environment"""

        # create framework folders on host system
        if nrobo_installed:
            """upgrade"""
            # Automatic upgrade logic will be developed later
            pass
        else:
            """fresh installation"""

            print(f"Installing framework")

            # Copy conftest.py and other files to current directory
            # =============================================================
            # THIS FILE OPERATION MUST BE FIRST STATEMENT IN IF BLOCK!!!!
            # =============================================================
            copy_file(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.CONFTEST_PY,
                      Path(os.environ[EnvKeys.EXEC_DIR]) / NP.CONFTEST_PY)
            copy_file(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.FRAMEWORK / NP.INIT_PY,
                      Path(os.environ[EnvKeys.EXEC_DIR]) / NP.INIT_PY)
            copy_file(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.FRAMEWORK / NP.NROBO_CONFIG_FILE,
                      Path(os.environ[EnvKeys.EXEC_DIR]) / NP.NROBO_CONFIG_FILE)

            # Copy framework to current directory
            copy_dir(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.FRAMEWORK_PAGES,
                     Path(os.environ[EnvKeys.EXEC_DIR]) / NP.PAGES)
            copy_dir(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.FRAMEWORK_TESTS,
                     Path(os.environ[EnvKeys.EXEC_DIR]) / NP.TESTS)
            copy_dir(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.BROWSER_CONFIGS,
                     Path(os.environ[EnvKeys.EXEC_DIR]) / NP.BROWSER_CONFIGS)

            print(f"Installation complete")

