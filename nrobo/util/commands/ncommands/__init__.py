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
from dataclasses import dataclass

from nrobo import EnvKeys
from nrobo.exceptions import MissingCommandImplementation
from nrobo.util.commands.posix import PosixCommand
from nrobo.util.commands.windows import WindowsCommand
from nrobo.util.platform import Platforms
from nrobo.util.process import terminal


@dataclass
class NCommands:
    """N_COMMANDS class hold nrobo command mappings for host platform.

    Raises <MissingCommandImplementation> exception
    If there is no implementation for host platform."""

    CLEAR_SCREEN = "clear screen"
    COMMAND = {
        Platforms.WINDOWS: {
            CLEAR_SCREEN: WindowsCommand.CLS,
        },
        Platforms.DARWIN: {CLEAR_SCREEN: PosixCommand.CLEAR},
    }


def get_command(command) -> None:  # pylint: disable=W0613
    """Return the appropriate posix or windows <command> to caller."""

    try:
        return NCommands.COMMAND[os.environ[EnvKeys.HOST_PLATFORM]][
            NCommands.CLEAR_SCREEN
        ]
    except KeyError:  # pylint: disable=W0707
        raise MissingCommandImplementation(
            NCommands.CLEAR_SCREEN
        )  # pylint: disable=W0707


def clear_screen():
    """Run the clear screen command."""
    terminal([get_command(NCommands.CLEAR_SCREEN)])


def remove_files_recursively(directory) -> int:
    """Remove <directory>

    :param directory:
    :return:"""

    if os.environ[EnvKeys.HOST_PLATFORM] in [
        Platforms.DARWIN,
        Platforms.LINUX,
        Platforms.MACOS,
    ]:
        try:
            return terminal(["rm", "-rf", directory])
        except Exception as e:  # pylint: disable=W0718
            print(e)

    if os.environ[EnvKeys.HOST_PLATFORM] in [Platforms.WINDOWS]:
        try:
            return terminal(["del", "/q", "/S", directory + os.sep + "*.*"])
        except Exception as e:  # pylint: disable=W0718
            print(e)

    return 1
