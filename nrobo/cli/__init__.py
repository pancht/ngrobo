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


def main():
    """Entry point of nrobo command-line-utility."""

    try:
        import os
        from nrobo.util.process import terminal
        import subprocess
        terminal(["pip", "install", "PyYAML"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        from nrobo.cli.launcher import launch_nrobo, launcher_command
        from nrobo.cli.upgrade import confirm_update
        from nrobo import EnvKeys, NROBO_CONST, NROBO_PATHS
        from nrobo import greet_the_guest, NROBO_CONST, EnvKeys
        from nrobo.cli.nrobo_args import nrobo_cli_parser
        from nrobo.cli.install import install_nrobo
        from nrobo.util.commands.ncommands import clear_screen, remove_files_recursively
        from nrobo.util.process import terminal
        from nrobo.util.constants import CONST
        from nrobo.cli.cli_constants import NREPORT
        from nrobo.util.python import verify_set_python_install_pip_command

        # clear screen
        clear_screen()

        # called to set EnvKeys dependent on args
        command, args, command_builder_notes = launcher_command()
        if command is None:
            exit(0)

        # greet the guest
        greet_the_guest()

        # install dependencies
        install_nrobo(install_only=True)

        # verify python installation and version
        verify_set_python_install_pip_command()

        # remove 'dist' directory created by python build module during packaging
        remove_files_recursively(NROBO_CONST.DIST_DIR)

        # delete results directory created by nrobo for storing test results
        # remove_files_recursively(NREPORT.REPORT_DIR)

        # parse nrobo cli arguments
        launch_nrobo()

    except KeyboardInterrupt as e:
        print(e)

    return 0
