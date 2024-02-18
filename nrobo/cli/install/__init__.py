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
import subprocess
from pathlib import Path
from typing import Optional
from nrobo import EnvKeys, NROBO_PATHS as NP, Environment, terminal, NROBO_CONST
from nrobo.cli.cli_constants import nCLI
from nrobo.util.common import Common
from nrobo.util.filesystem import copy_file, copy_dir
from nrobo.util.version import Version
from nrobo.cli.upgrade import get_host_version


def transfer_files_to_host_project() -> None:
    """Transfer nrobo project files to HOST project dir"""
    # Copy conftest.py and other files to current directory
    # =============================================================
    # THIS FILE OPERATION MUST BE FIRST STATEMENT IN IF BLOCK!!!!
    # =============================================================
    from nrobo import console, STYLE, set_environment, EnvKeys, Environment, NROBO_PATHS as NP

    if (Path(os.environ[EnvKeys.EXEC_DIR]) / NP.CONFTEST_PY).exists():

        patch_2024_6_10 = Path(os.environ[EnvKeys.NROBO_DIR]) / "patch_2024_6_10"
        patch_2024_6_12 = Path(os.environ[EnvKeys.NROBO_DIR]) / "patch_2024_6_12"

        if patch_2024_6_12.exists():
            return
        else:
            if Version(get_host_version()) == Version("2024.6.12"):
                from nrobo.util.filesystem import remove_file
                if patch_2024_6_10.exists():
                    remove_file(patch_2024_6_10)
                # Create new patch file
                Common.write_text_to_file(Path(os.environ[EnvKeys.NROBO_DIR]) / "patch_2024_6_12", "")

        if patch_2024_6_10.exists():
            return
        else:
            # Apply patches

            if Version(get_host_version()) == Version("2024.6.10"):
                Common.write_text_to_file(Path(os.environ[EnvKeys.NROBO_DIR]) / "patch_2024_6_10", "")

                # create a copy of host conftest.py
                copy_file(Path(os.environ[EnvKeys.EXEC_DIR]) / NP.CONFTEST_PY,
                          Path(os.environ[EnvKeys.EXEC_DIR]) / "copy-conftest.py")
                # copy nrobo conftest-host.py
                copy_file(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.NROBO_CONFTEST_HOST_FILE,
                          Path(os.environ[EnvKeys.EXEC_DIR]) / NP.CONFTEST_PY)

                print("\n")

                console.rule(f"[{STYLE.HLOrange}]A silent update has been made to your conftest.py. "
                             f"We have kept a copy of your conftest.py as copy-conftest.py under project root. "
                             f"Please take note of it.")
                print("\n")

        return

    print(f"Installing framework")

    copy_file(Path(os.environ[EnvKeys.NROBO_DIR]) / NP.NROBO_CONFTEST_HOST_FILE,
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


def install_nrobo(requirements_file: Optional[str] = None) -> None:
    """This will install nrobo framework and its dependencies on host system in the current directory
    from where nrobo command was executed in the Production environment.

    This will only install nrobo dependencies if it is executed in the Developer environment."""

    # Inline imports to handle circular import exception while importing partially initialized module
    from nrobo import set_environment, EnvKeys, Environment, NROBO_PATHS as NP
    set_environment()

    # if conftest file found on production system, meaning nrobo is already installed there
    nrobo_installed = Path(Path(os.environ[EnvKeys.EXEC_DIR]) / NP.CONFTEST_PY).exists()

    if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION \
            and not nrobo_installed:
        print(f"Installing requirements")

    if requirements_file is None:
        requirements_file = f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}cli{os.sep}install{os.sep}requirements.txt"

        return_code = terminal(command=[os.environ[EnvKeys.PIP_COMMAND], nCLI.INSTALL, '-r', requirements_file],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)

        if return_code == NROBO_CONST.SUCCESS:
            """return code zero means success"""
            if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION \
                    and not nrobo_installed:
                print(f"Requirements are installed successfully.")
        else:
            print(f"Requirements are not installed successfully!")
            exit()

    if os.environ[EnvKeys.ENVIRONMENT] == Environment.PRODUCTION:
        """Install or upgrading framework on Production environment"""

        # triggers forced update or normal update by comparing host version and pypi version
        from nrobo.cli import confirm_update
        confirm_update()

        # create framework folders on host system

        # Heck logic to check if this is a developer machine in production
        if Path(Path(os.environ[EnvKeys.EXEC_DIR]) / NP.PY_PROJECT_TOML_FILE).exists():
            # Developer machine in production detected! I'm not going to install framework BRO!!! :)
            pass
        else:
            """fresh installation"""
            transfer_files_to_host_project()
