"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================


This class holds definition of nRoBo specific exceptions.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
from nrobo import *


class MissingCommandImplementation(Exception):
    """This exception raise when <command> implementation missing for <host-platform>"""

    # constructor
    def __init__(self, command):
        self.value = f'Command <{command}> for host platform <{os.environ[EnvKeys.HOST_PLATFORM]}>'

    def __str__(self):
        return repr(self.value)


class NRoBoBrowserNotSupported(Exception):
    """This exception raise when <browser> is not supported or
    implementation to mimic <browser> is not yet implemented"""

    # constructor
    def __init__(self, browser):
        self.value = f'browser <{browser}> is not supported in nrobo.'

    def __str__(self):
        return repr(self.value)


class NRoBoIncorrectVersion(Exception):
    """Raises when an incorrect version is supplied to

       nrobo.util.version.Version class."""

    # constructor
    def __init__(self, version):
        self.value = f'Incorrect version <{version}>'

    def __str__(self):
        return repr(self.value)


class NRoBoInvalidOperation(Exception):
    """Raises when an arithmetic operation is performed

       over incompatible type.

       Anything other than type Version is an Invalid Type."""

    # constructor
    def __init__(self, operator: str, _type: type):
        self.value = f"TypeError: unsupported operand type(s) for {operator}: 'Version' and '{_type}'"

    def __str__(self):
        return repr(self.value)
