import os

from nrobo.util.process import terminal
from nrobo.util.platform import __HOST_PLATFORM__, PLATFORMS
from nrobo.util.python import verify_set_python_install_pip_command, __PYTHON__


def check():
    """
    Check package before upload

    :return:
    """
    terminal([__PYTHON__, "-m", "pip", "install", "twine"])
    terminal([__PYTHON__, "-m", "pip", "install", "--upgrade", "twine"])
    if __HOST_PLATFORM__ in [PLATFORMS.DARWIN, PLATFORMS.LINUX, PLATFORMS.MACOS]:
        terminal(["twine", "check", "dist"+os.sep+"*"])
    elif __HOST_PLATFORM__ in [PLATFORMS.WINDOWS]:
        terminal(["twine", "check", "."+os.sep+"dist"+os.sep+"*.*"])

