import os
import shutil
import sys

from nrobo.cli.cli_constansts import *
from nrobo.cli.nglobals import *

from nrobo.util.process import *
from nrobo.util.python import __PIP__

__REQUIREMENTS__ = "requirements.txt"

global __PIP__


def copy_dir(src, dest):
    try:
        shutil.copytree(src, dest)
    except FileExistsError as e:
        print(e)


def copy_file(src, dest):
    try:
        shutil.copyfile(src, dest)
    except FileExistsError as e:
        print(e)


def install_nrobo(requirements_file: Optional[str]=None):
    """
    Install nrobo

    :return:
    """
    # Find the directory we executed the script from:
    os.environ[EnvKeys.DirExecution] = os.getcwd()

    # Find the directory in which the current script resides:
    file_dir = os.path.dirname(os.path.realpath(__file__))

    import re
    os.environ[EnvKeys.DirNrobo] = re.findall(r"(.*nrobo)", str(file_dir))[0]

    if os.path.exists(f"{os.environ[EnvKeys.DirExecution]}{os.sep}nrobo"):
        os.environ[EnvKeys.Environment] = Environment.DEVELOPMENT
    else:
        os.environ[EnvKeys.Environment] = Environment.PRODUCTION

    from nrobo.cli import STYLE
    from nrobo.cli.tools import console

    print(f"Welcome to NROBO install")
    print(f"Installing requirements")
    if requirements_file is None:
        requirements_file = f"{os.environ[EnvKeys.DirNrobo]}{os.sep}cli{os.sep}install{os.sep}requirements.txt"

    terminal([__PIP__, nCLI.INSTALL, '-r', requirements_file])

    if os.environ[EnvKeys.Environment] == Environment.PRODUCTION:
        """Install framework on Production environment"""

        print(f"Installing framework")
        # create framework folders on host system

        # Copy framework to current directory
        copy_dir(f"{os.environ[EnvKeys.DirNrobo]}{os.sep}framework{os.sep}pages",
                 f"{os.environ[EnvKeys.DirExecution]}{os.sep}pages")
        copy_dir(f"{os.environ[EnvKeys.DirNrobo]}{os.sep}framework{os.sep}tests",
                 f"{os.environ[EnvKeys.DirExecution]}{os.sep}tests")
        copy_dir(f"{os.environ[EnvKeys.DirNrobo]}{os.sep}browserConfigs",
                 f"{os.environ[EnvKeys.DirExecution]}{os.sep}browserConfigs")

        # Copy conftest.py and other files to current directory
        copy_file(f"{os.environ[EnvKeys.DirNrobo]}{os.sep}framework{os.sep}__init__.py",
                  f"{os.environ[EnvKeys.DirExecution]}{os.sep}__init__.py")
        copy_file(f"{os.environ[EnvKeys.DirNrobo]}{os.sep}conftest.py",
                  f"{os.environ[EnvKeys.DirExecution]}{os.sep}conftest.py")

        print(f"Installation complete")

