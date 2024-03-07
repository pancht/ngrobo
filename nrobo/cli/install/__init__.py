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
import time
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

    stop_auto_silent_update_version = Version("2024.19.3")
    host_version = Version(get_host_version())
    pypi_version = Version(get_pypi_index(NROBO_CONST.NROBO))
    detect.ensure_pathces_dir()

    if detect.host_machine_has_nRoBo():

        patch_2024_6_10 = NP.NROBO_DIR / "patch_2024_6_10"
        patch_2024_6_12 = NP.NROBO_DIR / "patch_2024_6_12"
        patch_2024_19_5 = NP.NROBO_DIR / NP.PATCHES / "2024.19.5"

        if patch_2024_19_5.exists() and host_version < Version("2024.20.0"):
            return

        if host_version < Version("2024.20.0"):
            # apply patch for 2024.19.4
            # [NewFile] Copy browserConfigs/markers.yaml to user's project dir from nrobo
            copy_file(NP.NROBO_DIR / NP.MARKERS_YAML
                      , NP.EXEC_DIR / NP.MARKERS_YAML)
            Common.write_text_to_file(patch_2024_19_5, "")

            print("\n")
            console.rule(f"[{STYLE.HLOrange}]A silent update has been made to your nRoBo copy. "
                         f"We have added a new file {NP.MARKERS_YAML} under project root. "
                         f"Now You can add your custom markers to nRoBo using this file."
                         f"Please take note of it. And rerun tests!")
            print("\n")
            exit(1)

        if patch_2024_6_12.exists() and host_version < Version("2024.7.0"):
            return

        if host_version < Version("2024.7.0"):
            if Version(get_host_version()) == Version("2024.6.12"):
                from nrobo.util.filesystem import remove_file
                if patch_2024_6_10.exists():
                    remove_file(patch_2024_6_10)
                # Create new patch file
                Common.write_text_to_file(NP.NROBO_DIR / "patch_2024_6_12", "")

        if patch_2024_6_10.exists() and host_version < Version("2024.7.0"):
            return

        if host_version < Version("2024.7.0"):
            # Apply patches

            if Version(get_host_version()) == Version("2024.6.10"):
                Common.write_text_to_file(NP.NROBO_DIR / "patch_2024_6_10", "")

                # create a copy of host conftest.py
                copy_file(NP.EXEC_DIR / NP.CONFTEST_PY, NP.EXEC_DIR / "copy-conftest.py")
                # copy nrobo conftest-host.py
                copy_file(NP.NROBO_DIR / NP.NROBO_CONFTEST_HOST_FILE, NP.EXEC_DIR / NP.CONFTEST_PY)

            print("\n")
            console.rule(f"[{STYLE.HLOrange}]A silent update has been made to your conftest.py. "
                         f"We have kept a copy of your conftest.py as copy-conftest.py under project root. "
                         f"Please take note of it.")
            print("\n")

        if host_version <= stop_auto_silent_update_version:
            # Re-install
            pass
        else:
            return  # Return from  installation if nRoBo is already installed on HOST system! SMART! RIGHT! :)

    # nRoBo was not found on HOST machine.
    # Lets' make it found then!!!
    # Lets' make an ADDRESS on the HOST machine. :)

    force_reinstall = False

    patch_file = str(stop_auto_silent_update_version.version).replace('.', "_") + ".txt"
    if host_version <= stop_auto_silent_update_version\
            and not (NP.NROBO_DIR / patch_file).exists():
        """force re-install"""
        force_reinstall = True

    if force_reinstall:
        print(f"Re-installing framework")
    elif (NP.EXEC_DIR / NP.CONFTEST_PY).exists():
        return  # Framework already installed, thus, just do nothing and return.
    else:
        # Fresh install
        print(f"Installing framework")

    if (NP.EXEC_DIR / NP.CONFTEST_PY).exists():
        # create a copy of host conftest.py
        copy_file(NP.EXEC_DIR / NP.CONFTEST_PY,
                  NP.EXEC_DIR / f"copy-conftest-{datetime.today().strftime('%Y_%m_%d_%H_%M')}"
                             f"_{Common.generate_random_numbers(1000, 9999)}.py")

    # copy nrobo conftest-host.py
    copy_file(NP.NROBO_DIR / NP.NROBO_CONFTEST_HOST_FILE, NP.EXEC_DIR / NP.CONFTEST_PY)

    if (NP.EXEC_DIR / NP.INIT_PY).exists():
        copy_file(NP.EXEC_DIR / NP.INIT_PY,
                  NP.EXEC_DIR / f"copy-__init__-{datetime.today().strftime('%Y_%m_%d_%H_%M')}"
                             f"_{Common.generate_random_numbers(1000, 9999)}.py")

    copy_file(NP.NROBO_DIR / NP.INIT_PY, NP.EXEC_DIR / NP.INIT_PY)

    if (NP.EXEC_DIR / NP.NROBO_CONFIG_FILE).exists():
        copy_file(NP.EXEC_DIR / NP.NROBO_CONFIG_FILE, \
        NP.EXEC_DIR / f"copy-nrobo-config-{datetime.today().strftime('%Y_%m_%d_%H_%M')}" \
                   f"_{Common.generate_random_numbers(1000, 9999)}.yaml")

    copy_file(NP.NROBO_DIR / NP.FRAMEWORK / NP.NROBO_CONFIG_FILE,
              NP.EXEC_DIR / NP.NROBO_CONFIG_FILE)

    # Copy framework to current directory
    if (NP.EXEC_DIR / NP.PAGES).exists():
        # move directory
        move(NP.EXEC_DIR / NP.PAGES,
             NP.EXEC_DIR /  f"copy-pages--{datetime.today().strftime('%Y_%m_%d_%H_%M')}"
                                       f"_{Common.generate_random_numbers(1000, 9999)}")

    copy_dir(NP.NROBO_DIR / NP.FRAMEWORK_PAGES, NP.EXEC_DIR / NP.PAGES)

    if (NP.EXEC_DIR / NP.TESTS).exists():
        # move directory
        move(NP.EXEC_DIR / NP.TESTS,
             NP.EXEC_DIR / f"copy-tests--{datetime.today().strftime('%Y_%m_%d_%H_%M')}"
                                       f"_{Common.generate_random_numbers(1000, 9999)}")

    copy_dir(NP.NROBO_DIR / NP.FRAMEWORK_TESTS, NP.EXEC_DIR / NP.TESTS)

    if (NP.EXEC_DIR / NP.BROWSER_CONFIGS).exists():
        # move directory
        move(NP.EXEC_DIR / NP.BROWSER_CONFIGS,
             NP.EXEC_DIR / f"copy-browserConfigs-{datetime.today().strftime('%Y_%m_%d_%H_%M')}"
                                       f"_{Common.generate_random_numbers(1000, 9999)}")

    copy_dir(NP.NROBO_DIR / NP.BROWSER_CONFIGS, NP.EXEC_DIR / NP.BROWSER_CONFIGS)

    if force_reinstall:
        print(f"Re-install complete")

        console.rule(f"[{STYLE.HLRed}]A silent re-install has been made to nrobo framework. "
                     f"We have kept a copy of each of your directory and files under project root. "
                     f"Please take an action on them and clean unwanted directory and files.")
        Common.write_text_to_file(NP.NROBO_DIR / patch_file, "")
        exit()
    else:
        print(f"Installation complete")


def install_nrobo(requirements_file: Optional[str] = None, install_only: bool = False) -> None:
    """This will install nrobo framework and its dependencies on host system in the current directory
    from where nrobo command was executed in the Production environment.

    This will only install nrobo dependencies if it is executed in the Developer environment."""

    # Inline imports to handle circular import exception while importing partially initialized module
    from nrobo import set_environment, EnvKeys, Environment, NROBO_PATHS as NP
    set_environment()

    if detect.production_machine() and not detect.host_machine_has_nRoBo():
        print(f"Installing requirements")

    if requirements_file is None:
        requirements_file = f"{NP.NROBO_DIR}{os.sep}cli{os.sep}install{os.sep}requirements.txt"

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
            return

    if install_only:
        # No need to install or upgrade framework
        # Just return after installing requirements
        return

    if detect.production_machine():
        """Install or upgrading framework on Production environment"""

        # triggers forced update or normal update by comparing host version and pypi version
        from nrobo.cli.upgrade import confirm_update
        if detect.production_machine() and not detect.developer_machine():
            confirm_update()

        # create framework folders on host system

        # Heck logic to check if this is a developer machine in production_machine
        if detect.developer_machine():
            # Developer machine in production_machine detected! I'm not going to install framework BRO!!! :)
            pass
        else:
            """fresh installation"""
            transfer_files_to_host_project()
