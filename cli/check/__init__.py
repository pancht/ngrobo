"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

This module has actions pertaining to nRoBo verifying packages.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

from nrobo import *
from nrobo.util.platform import PLATFORMS


def check(debug=False) -> None:
    """Checks packages before publishing."""

    terminal([os.environ[EnvKeys.PYTHON], "-m", "pip", "install", "twine"])
    terminal([os.environ[EnvKeys.PYTHON], "-m", "pip", "install", "--upgrade", "twine"])
    if os.environ[EnvKeys.HOST_PLATFORM] in [
        PLATFORMS.DARWIN,
        PLATFORMS.LINUX,
        PLATFORMS.MACOS,
    ]:
        terminal(["twine", "check", "dist" + os.sep + "*"], debug=debug)
    elif os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.WINDOWS]:
        terminal(
            ["twine", "check", "." + os.sep + "dist" + os.sep + "*.*"], debug=debug
        )
