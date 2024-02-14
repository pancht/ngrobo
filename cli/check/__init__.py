import os

from nrobo.util.process import terminal
from nrobo.util.platform import PLATFORMS
from nrobo import *

def check(debug=False):
    """
    Check package before upload

    :return:
    """
    terminal([os.environ[EnvKeys.PYTHON], "-m", "pip", "install", "twine"])
    terminal([os.environ[EnvKeys.PYTHON], "-m", "pip", "install", "--upgrade", "twine"])
    if os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.DARWIN, PLATFORMS.LINUX, PLATFORMS.MACOS]:
        terminal(["twine", "check", "dist" + os.sep + "*"], debug=debug)
    elif os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.WINDOWS]:
        terminal(["twine", "check", "."+os.sep+"dist"+os.sep+"*.*"], debug=debug)

