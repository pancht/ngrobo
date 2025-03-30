"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Trigger for nrobo framework!

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com

"""

import sys

from nrobo.util.python import verify_set_python_install_pip_command


def main():  # pylint: disable=R0914
    """Entry point of nrobo command-line-utility."""

    try:
        import os  # pylint: disable=W0611,C0415
        from nrobo.util.process import terminal  # pylint: disable=C0415
        import subprocess  # pylint: disable=C0415

        terminal(
            ["pip", "install", "PyYAML"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )
        from nrobo.cli.launcher import (
            launch_nrobo,
            launcher_command,
        )  # pylint: disable=C0415
        from nrobo.cli.upgrade import confirm_update  # pylint: disable=W0611,C0415
        from nrobo import EnvKeys, NroboConst, NroboPaths  # pylint: disable=W0611,C0415
        from nrobo import greet_the_guest  # pylint: disable=W0611,C0415
        from nrobo.cli.nrobo_args import nrobo_cli_parser  # pylint: disable=W0611,C0415
        from nrobo.cli.install import (  # pylint: disable=W0611,C0415
            install_nrobo,
            install_user_specified_requirements,
            missing_user_files_on_production,
        )
        from nrobo.util.commands.ncommands import (
            clear_screen,
            remove_files_recursively,
        )  # pylint: disable=C0415
        from nrobo.util.process import terminal  # pylint: disable=W0611,C0415
        from nrobo.util.constants import Const  # pylint: disable=W0611,C0415

        # clear screen
        clear_screen()

        # called to set EnvKeys dependent on args
        command, args, command_builder_notes = (
            launcher_command()
        )  # pylint: disable=W0612
        if command is None:
            if missing_user_files_on_production():
                install_nrobo(install_only=False)

            sys.exit(0)

        # greet the guest
        greet_the_guest()

        # install nRoBo dependencies
        if missing_user_files_on_production():
            install_nrobo(install_only=False)
        else:
            install_nrobo(install_only=True)

        # install user specified project dependencies
        install_user_specified_requirements()

        # verify python installation and version
        verify_set_python_install_pip_command()

        # remove 'dist' directory created by python build module during packaging
        remove_files_recursively(NroboConst.DIST_DIR)

        # delete results directory created by nrobo for storing test results
        # remove_files_recursively(NREPORT.REPORT_DIR)

        # parse nrobo cli arguments
        launch_nrobo()

    except KeyboardInterrupt as e:
        print(e)

    return 0
