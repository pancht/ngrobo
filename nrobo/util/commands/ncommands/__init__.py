from nrobo.exceptions import *
from nrobo.util.commands.posix import POSIX_COMMAND
from nrobo.util.commands.windows import WINDOWS_COMMAND
from nrobo.util.platform import __HOST_PLATFORM__, PLATFORMS
from nrobo.util.process import run_command


class N_COMMANDS:
    """
    This class hold nrobo command mappings for host platform.

    Raises <MissingCommandImplementation> exception
    If there is no implementation for host platform.
    """
    CLEAR_SCREEN = "clear screen"
    COMMAND = {
        PLATFORMS.WINDOWS: {
            CLEAR_SCREEN: WINDOWS_COMMAND.CLS,
        },
        PLATFORMS.DARWIN: {
            CLEAR_SCREEN: POSIX_COMMAND.CLEAR
        }
    }


def get_command(command):
    """
    Return the appropriate posix or windows <command> to caller.

    :param command:
    :return:
    """
    try:
        return N_COMMANDS.COMMAND[__HOST_PLATFORM__][N_COMMANDS.CLEAR_SCREEN]
    except KeyError as ke:
        raise MissingCommandImplementation(N_COMMANDS.CLEAR_SCREEN)


def clear_screen():
    """
    Run the clear screen command.

    :return:
    """
    run_command([get_command(N_COMMANDS.CLEAR_SCREEN)])


def remove_files_recursively(directory):
    """
    Remove <directory>

    :param directory:
    :return:
    """
    run_status = run_command(["rm", "-rf", directory])
    return run_status
