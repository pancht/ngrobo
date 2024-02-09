# Holds python command to run other commands.
# Options: python | python3
__PYTHON__ = "python"

import re
import platform
from nrobo.util.process import *


def verify_set_python_install_pip_command():
    """
    Verifies if python is installed on the host system.

    If found, sets the appropriate python command
    Else exit the nrobo framework with message.

    If found and sets python command, install pip as well.

    :return:
    """

    # regular expression to verify python version
    # major.minor.nightly-build
    regx = re.compile(r'([\d]+).[\d]+.[\d]+.*')

    if regx.match(platform.python_version()) is None:
        print("Exit because Python is not found on your system!!!")
        exit(1)
    else:
        # python is installed on the host system

        if int(re.search(r'[\d]+', platform.python_version())[0]) >= 3:
            # check if python version is >=3

            python3 = "python3"

            # update the global constant
            global __PYTHON__
            __PYTHON__ = python3

            if terminal([__PYTHON__, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) != 0:
                __PYTHON__ = "python"

    # Install pip now!
    terminal([__PYTHON__, '-m', 'ensurepip', '--upgrade'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
