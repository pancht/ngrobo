"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Platform functions.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
import os
import platform

from nrobo import EnvKeys


class PLATFORMS:
    """PLATFORMS class holds possible platform names."""

    LINUX = "Linux"
    DARWIN = "Darwin"
    MACOS = DARWIN
    JAVA = "Java"
    WINDOWS = "Windows"


os.environ[EnvKeys.HOST_PLATFORM] = platform.system()
