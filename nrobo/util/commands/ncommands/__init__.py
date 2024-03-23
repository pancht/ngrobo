"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

import os

from nrobo import *
from nrobo.exceptions import *
from nrobo.util.commands.posix import POSIX_COMMAND
from nrobo.util.commands.windows import WINDOWS_COMMAND
from nrobo.util.platform import PLATFORMS
from nrobo.util.process import terminal, terminal_nogui


class N_COMMANDS:
    """N_COMMANDS class hold nrobo command mappings for host platform.

    Raises <MissingCommandImplementation> exception
    If there is no implementation for host platform."""

    CLEAR_SCREEN = "clear screen"
    COMMAND = {
        PLATFORMS.WINDOWS: {
            CLEAR_SCREEN: WINDOWS_COMMAND.CLS,
        },
        PLATFORMS.DARWIN: {
            CLEAR_SCREEN: POSIX_COMMAND.CLEAR
        }
    }


def get_command(command) -> None:
    """Return the appropriate posix or windows <command> to caller."""

    try:
        return N_COMMANDS.COMMAND[os.environ[EnvKeys.HOST_PLATFORM]][N_COMMANDS.CLEAR_SCREEN]
    except KeyError as ke:
        raise MissingCommandImplementation(N_COMMANDS.CLEAR_SCREEN)


def clear_screen():
    """Run the clear screen command."""
    terminal([get_command(N_COMMANDS.CLEAR_SCREEN)])


def remove_files_recursively(directory) -> int:
    """Remove <directory>

    :param directory:
    :return:"""

    if os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.DARWIN, PLATFORMS.LINUX, PLATFORMS.MACOS]:
        try:
            return terminal(["rm", "-rf", directory])
        except Exception as e:
            print(e)

    if os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.WINDOWS]:
        try:
            return terminal(["del", "/q", "/S", directory + os.sep + "*.*"])
        except Exception as e:
            print(e)

    return 1
