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
import os
import subprocess


def terminal_nogui(command) -> int:
    """run command without any terminal output"""
    return terminal(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def terminal(command=[], stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False,
             cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None,
             universal_newlines=None, debug=False):
    """
    Execute given command, command

    :param capture_output:
    :param command: command
    :return: status code
    """
    if debug is False:
        """check environment debug flag"""
        from nrobo import EnvKeys
        if str(os.environ[EnvKeys.DEBUG]) == "True":
            debug = True

    try:
        if (stdout and stderr) or debug is False:
            return subprocess.check_call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            return subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
    except FileNotFoundError as e:
        print(f"Command failed with FileNotFoundError!")
        print(e)
        return 1
