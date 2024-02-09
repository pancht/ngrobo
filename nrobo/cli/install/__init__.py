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


def install_nrobo(requirements_file: Optional[str] = None):
    """
    Install nrobo

    :return:
    """

    set_environment()

    from nrobo.cli import STYLE
    from nrobo.cli.tools import console

    print(f"Welcome to NROBO install")
    print(f"Installing requirements")
    if requirements_file is None:
        requirements_file = f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}cli{os.sep}install{os.sep}requirements.txt"

        return_code = terminal(command=[os.environ[EnvKeys.PIP_COMMAND], nCLI.INSTALL, '-r', requirements_file],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)

        if return_code:
            """non-zero return code means a success"""
            print(f"Requirements are installed successfully.")
        else:
            print(f"Requirements are not installed successfully!")

    if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION:
        """Install framework on Production environment"""

        print(f"Installing framework")
        # create framework folders on host system

        # Copy framework to current directory
        copy_dir(f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}framework{os.sep}pages",
                 f"{os.environ[EnvKeys.EXEC_DIR]}{os.sep}pages")
        copy_dir(f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}framework{os.sep}tests",
                 f"{os.environ[EnvKeys.EXEC_DIR]}{os.sep}tests")
        copy_dir(f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}browserConfigs",
                 f"{os.environ[EnvKeys.EXEC_DIR]}{os.sep}browserConfigs")

        # Copy conftest.py and other files to current directory
        copy_file(f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}framework{os.sep}__init__.py",
                  f"{os.environ[EnvKeys.EXEC_DIR]}{os.sep}__init__.py")
        copy_file(f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}conftest.py",
                  f"{os.environ[EnvKeys.EXEC_DIR]}{os.sep}conftest.py")
        copy_file(f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}framework{os.sep}nrobo-config.yaml",
                  f"{os.environ[EnvKeys.EXEC_DIR]}{os.sep}nrobo-config.yaml")

        print(f"Installation complete")
