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

import os

from nrobo import terminal, EnvKeys
from nrobo.util.platform import Platforms


def check(debug=False) -> None:
    """Checks packages before publishing."""

    terminal([os.environ[EnvKeys.PYTHON], "-m", "pip", "install", "twine"])
    terminal([os.environ[EnvKeys.PYTHON], "-m", "pip", "install", "--upgrade", "twine"])
    if os.environ[EnvKeys.HOST_PLATFORM] in [
        Platforms.DARWIN,
        Platforms.LINUX,
        Platforms.MACOS,
    ]:
        terminal(["twine", "check", "dist" + os.sep + "*"], debug=debug)
    elif os.environ[EnvKeys.HOST_PLATFORM] in [Platforms.WINDOWS]:
        terminal(
            ["twine", "check", "." + os.sep + "dist" + os.sep + "*.*"], debug=debug
        )
