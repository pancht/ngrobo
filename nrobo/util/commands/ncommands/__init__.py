from nrobo.util.commands.posix import POSIX_COMMAND
from nrobo.util.commands.windows import WINDOWS_COMMAND
from nrobo.util.platform import __HOST_PLATFORM__, PLATFORMS
from nrobo.util.process import run_command


class NCOMMAND:
    CLEAR_SCREEN = "clear-screen"


def get_command(command):
    """
    Return the appropriate posix or windows command to caller.

    :param command:
    :return:
    """
    if __HOST_PLATFORM__ == PLATFORMS.MACOS \
            or __HOST_PLATFORM__ == PLATFORMS.DARWIN \
            or __HOST_PLATFORM__ == PLATFORMS.LINUX:
        if command == NCOMMAND.CLEAR_SCREEN:
            return POSIX_COMMAND.CLEAR
    elif __HOST_PLATFORM__ == PLATFORMS.WINDOWS:
        if command == NCOMMAND.CLEAR_SCREEN:
            return WINDOWS_COMMAND.CLS
    elif __HOST_PLATFORM__ == PLATFORMS.JAVA:
        print("No implementation yet in nrobo framework!!!")
        exit(1)
    else:
        print("Unrecognized operating system!!! nrobo cann't proceed.")
        exit(1)


def clear_screen():
    """
    Run the clear screen command.

    :return:
    """
    run_command(get_command(NCOMMAND.CLEAR_SCREEN))
