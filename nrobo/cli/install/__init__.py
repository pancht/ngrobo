"""
Installer for installing nrobo framework at host system.
"""
import os
import shutil
import sys

from nrobo.cli import *
from nrobo.cli.cli_constansts import *
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

    from nrobo import set_environment, EnvKeys, Environment, NROBO_PATHS as NP
    set_environment()

    if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION:
        print(f"Welcome to NROBO install")
        print(f"Installing requirements")

    if requirements_file is None:
        requirements_file = f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}cli{os.sep}install{os.sep}requirements.txt"

        return_code = terminal(command=[os.environ[EnvKeys.PIP_COMMAND], nCLI.INSTALL, '-r', requirements_file],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)

        if return_code == NROBO_CONST.SUCCESS:
            """return code zero means success"""
            if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION:
                print(f"Requirements are installed successfully.")
        else:
            print(f"Requirements are not installed successfully!")
            exit()

    if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION:
        """Install framework on Production environment"""

        print(f"Installing framework")
        # create framework folders on host system

        # Copy framework to current directory
        copy_dir(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.FRAMEWORK_PAGES,
                 Path(os.environ[EnvKeys.EXEC_DIR]) / NP.PAGES)
        copy_dir(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.FRAMEWORK_TESTS,
                 Path(os.environ[EnvKeys.EXEC_DIR]) / NP.TESTS)
        copy_dir(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.BROWSER_CONFIS,
                 Path(os.environ[EnvKeys.EXEC_DIR]) / NP.BROWSER_CONFIS)

        # Copy conftest.py and other files to current directory
        copy_file(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.FRAMEWORK / NP.INIT_PY,
                  Path(os.environ[EnvKeys.EXEC_DIR]) / NP.INIT_PY)
        copy_file(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.FRAMEWORK / NP.NROBO_CONFIG_FILE,
                  Path(os.environ[EnvKeys.EXEC_DIR]) / NP.NROBO_CONFIG_FILE)
        copy_file(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.CONFTEST_PY,
                  Path(os.environ[EnvKeys.EXEC_DIR]) / NP.CONFTEST_PY)

        print(f"Installation complete")
