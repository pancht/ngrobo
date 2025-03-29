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

# Holds python command to run other commands.
# Options: python | python3
import os
import platform
import subprocess


def verify_set_python_install_pip_command() -> None:
    """Verifies if python is installed on the host system.

    If found, sets the appropriate python command
    Else exit the nrobo framework with message.

    If found and sets python command, install pip as well."""

    # regular expression to verify python version
    # major.minor.nightly-build
    import re
    regx = re.compile(r"([\d]+).[\d]+.[\d]+.*")

    if regx.match(platform.python_version()) is None:
        print(
            "Required dependency python is not installed on system! Please, install python >= 3.8 and retry."
        )
        exit(1)
    else:
        # python is installed on the host system
        import re
        from nrobo import terminal, NroboConst, EnvKeys
        if int(re.search(r"[\d]+", platform.python_version())[0]) >= 3:
            # check if python version is >=3

            python3 = "python3"

            if (
                terminal(
                    [python3, "--version"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT,
                )
                == NroboConst.SUCCESS
            ):
                os.environ[EnvKeys.PYTHON] = python3
            elif (
                    terminal(
                    [os.environ[EnvKeys.PYTHON], "--version"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT,
                )
                    == NroboConst.SUCCESS
            ):
                pass
            else:
                print(
                    "Required dependency python is not installed on system! Please, install python >= 3.8 and retry."
                )
                exit()

    # Install pip now!
    terminal(
        [os.environ[EnvKeys.PYTHON], "-m", "ensurepip", "--upgrade"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
