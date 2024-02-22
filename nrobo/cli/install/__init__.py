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
from nrobo.cli.cli_constants import nCLI
from nrobo.util.common import Common
from nrobo.util.filesystem import copy_file, copy_dir, move, remove_filetree
from nrobo.util.version import Version
from nrobo.cli.upgrade import get_host_version, get_pypi_index
import nrobo.cli.detection as detect
from datetime import datetime


def transfer_files_to_host_project() -> None:
    """Transfer nrobo project files to HOST project dir"""
    # Copy conftest.py and other files to current directory
    # =============================================================
    # THIS FILE OPERATION MUST BE FIRST STATEMENT IN IF BLOCK!!!!
    # =============================================================
    from nrobo import console, STYLE, set_environment, EnvKeys, Environment, NROBO_PATHS as NP, NROBO_CONST

    if detect.host_machine_has_nRoBo():

        host_version = Version(get_host_version())
        pypi_version = Version(get_pypi_index(NROBO_CONST.NROBO))

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

        if host_version <= Version("2024.12.0"):
            # Re-install
            pass
        else:
            return  # Return from  installation if nRoBo is already installed on HOST system! SMART! RIGHT! :)

    # nRoBo was not found on HOST machine.
    # Lets' make it found then!!!
    # Lets' make an ADDRESS on the HOST machine. :)

    exec_dir = Path(os.environ[EnvKeys.EXEC_DIR])
    nrobo_dir = Path(os.environ[EnvKeys.NROBO_DIR])

    force_reinstall = False

    if host_version <= Version("2024.12.0"):
        """force re-install"""
        force_reinstall = True

    if force_reinstall:
        print(f"Re-installing framework")
    else:
        print(f"Installing framework")

    if (exec_dir / NP.CONFTEST_PY).exists():
        # create a copy of host conftest.py
        copy_file(exec_dir / NP.CONFTEST_PY,
                  exec_dir / f"copy-conftest-{datetime.today().strftime('%Y_%m_%d_%H_%M')}"
                             f"_{Common.generate_random_numbers(1000, 9999)}.py")

    # copy nrobo conftest-host.py
    copy_file(nrobo_dir / NP.NROBO_CONFTEST_HOST_FILE, exec_dir / NP.CONFTEST_PY)

    if (exec_dir / NP.INIT_PY).exists():
        copy_file(exec_dir / NP.INIT_PY,
                  exec_dir / f"copy-__init__-{datetime.today().strftime('%Y_%m_%d_%H_%M')}"
                             f"_{Common.generate_random_numbers(1000, 9999)}.py")

    copy_file(nrobo_dir / NP.INIT_PY), exec_dir / NP.INIT_PY

    if (exec_dir / NP.NROBO_CONFIG_FILE).exists():
        copy_file(exec_dir / NP.NROBO_CONFIG_FILE), \
        exec_dir / f"copy-nrobo-config-{datetime.today().strftime('%Y_%m_%d_%H_%M')}" \
                   f"_{Common.generate_random_numbers(1000, 9999)}.yaml"

    copy_file(nrobo_dir / NP.FRAMEWORK / NP.NROBO_CONFIG_FILE,
              exec_dir / NP.NROBO_CONFIG_FILE)

    # Copy framework to current directory
    if (exec_dir / NP.FRAMEWORK_PAGES).exists():
        # move directory
        move(exec_dir / NP.FRAMEWORK_PAGES,
             exec_dir / NP.FRAMEWORK / f"copy-pages--{datetime.today().strftime('%Y_%m_%d_%H_%M')}"
                                       f"_{Common.generate_random_numbers(1000, 9999)}")

    copy_dir(nrobo_dir / NP.FRAMEWORK_PAGES, exec_dir / NP.PAGES)

    if (exec_dir / NP.FRAMEWORK_TESTS).exists():
        # move directory
        move(exec_dir / NP.FRAMEWORK_TESTS,
             exec_dir / NP.FRAMEWORK / f"copy-tests--{datetime.today().strftime('%Y_%m_%d_%H_%M')}"
                                       f"_{Common.generate_random_numbers(1000, 9999)}")

    copy_dir(nrobo_dir / NP.FRAMEWORK_TESTS, exec_dir / NP.TESTS)

    if (exec_dir / NP.BROWSER_CONFIGS).exists():
        # move directory
        move(exec_dir / NP.BROWSER_CONFIGS,
             exec_dir / NP.FRAMEWORK / f"copy-browserConfigs-{datetime.today().strftime('%Y_%m_%d_%H_%M')}"
                                       f"_{Common.generate_random_numbers(1000, 9999)}")

    copy_dir(nrobo_dir / NP.BROWSER_CONFIGS, exec_dir / NP.BROWSER_CONFIGS)

    if force_reinstall:
        print(print(f"Re-install complete"))

        console.rule(f"[{STYLE.HLRed}]A silent re-install has been made to nrobo framework. "
                     f"We have kept a copy of each of your directory and files under project root. "
                     f"Please take an action on them and clean unwanted directory and files.")
    else:
        print(f"Installation complete")


def install_nrobo(requirements_file: Optional[str] = None) -> None:
    """This will install nrobo framework and its dependencies on host system in the current directory
    from where nrobo command was executed in the Production environment.

    This will only install nrobo dependencies if it is executed in the Developer environment."""

    # Inline imports to handle circular import exception while importing partially initialized module
    from nrobo import set_environment, EnvKeys, Environment, NROBO_PATHS as NP
    set_environment()

    if detect.production_machine() and not detect.host_machine_has_nRoBo():
        print(f"Installing requirements")

    if requirements_file is None:
        requirements_file = f"{os.environ[EnvKeys.NROBO_DIR]}{os.sep}cli{os.sep}install{os.sep}requirements.txt"
        from nrobo import terminal, NROBO_CONST
        return_code = terminal(command=[os.environ[EnvKeys.PIP_COMMAND], nCLI.INSTALL, '-r', requirements_file],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)

        if return_code == NROBO_CONST.SUCCESS:
            """return code zero means success"""
            if detect.production_machine() and not detect.host_machine_has_nRoBo():
                print(f"Requirements are installed successfully.")
        else:
            print(f"Requirements are not installed successfully!")
            exit()

    if detect.production_machine():
        """Install or upgrading framework on Production environment"""

        # triggers forced update or normal update by comparing host version and pypi version
        from nrobo.cli.upgrade import confirm_update
        confirm_update()

        # create framework folders on host system

        # Heck logic to check if this is a developer machine in production_machine
        if detect.developer_machine():
            # Developer machine in production_machine detected! I'm not going to install framework BRO!!! :)
            pass
        else:
            """fresh installation"""
            transfer_files_to_host_project()
