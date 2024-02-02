"""
Trigger for nrobo framework!

"""

import argparse
import os

from nrobo.cli.install import install_dependencies, __REQUIREMENTS__
from nrobo.util.commands.ncommands import clear_screen, remove_files_recursively
from nrobo.util.constants import CONST
from nrobo.util.python import verify_set_python_install_pip_command
from nrobo import FRAMEWORK_PATHS

# refer to global defined in nrobo.util.process
global __PYTHON__


def greet_the_guest():
    greet_msg = 'Namastey Wolrd!. Thank you for choosing, NROBO.'.format(CONST.NEWLINE)
    formatted_heart_string = CONST.HEART_RED * (len(greet_msg) // 2)

    print('\n{}\n{}\n{}'.format(formatted_heart_string, greet_msg, formatted_heart_string))
    print('\nWe are still in the process of refactoring next gen nrobo.'
          '\nStay tuned!\n')


def parse_cli_args():
    """
    Parse command-line-arguments
    Doc: https://docs.python.org/3/library/argparse.html#example

    :return:
    """
    parser = argparse.ArgumentParser(
        prog="nrobo",
        description='Run tests through nrobo framework')
    parser.add_argument("-i", "--install", action="store_true")

    args = parser.parse_args()

    if args.install:
        # Install dependencies
        print("Installing dependencies...")
        install_dependencies(FRAMEWORK_PATHS.REQUIREMENTS + __REQUIREMENTS__)


def main():
    """
    Entry point of nrobo command-line-utility.

    :return:
    """

    clear_screen()
    greet_the_guest()
    verify_set_python_install_pip_command()
    remove_files_recursively("dist")
    parse_cli_args()
