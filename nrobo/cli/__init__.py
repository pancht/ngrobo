"""
Trigger for nrobo framework!

"""
import subprocess


def main():
    """
    Entry point of nrobo command-line-utility.

    :return:
    """
    from nrobo import greet_the_guest, NROBO_CONST
    from nrobo.cli.cli_args import parse_cli_args
    from nrobo.cli.install import install_nrobo
    from nrobo.util.commands.ncommands import clear_screen, remove_files_recursively
    from nrobo.util.process import terminal
    from nrobo.util.constants import CONST
    from nrobo.cli.cli_constansts import NREPORT
    from nrobo.util.python import verify_set_python_install_pip_command

    # refer to global defined in nrobo.util.process
    __APP_NAME__ = CONST.EMPTY

    # install rich library
    terminal(["pip", "install", "rich"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # clear screen
    clear_screen()

    # greet the guest
    greet_the_guest()

    # install dependencies
    install_nrobo(None)

    # verify python installation and version
    verify_set_python_install_pip_command()

    # remove 'dist' directory created by python build module during packaging
    remove_files_recursively(NROBO_CONST.DIST_DIR)

    # delete results directory created by nrobo for storing test results
    remove_files_recursively(NREPORT.REPORT_DIR)

    # parse nrobo cli arguments
    parse_cli_args()
