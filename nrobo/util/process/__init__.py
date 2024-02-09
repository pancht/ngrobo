"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================


subprocess doc: https://docs.python.org/3/library/subprocess.html
another subprocess doc: https://www.geeksforgeeks.org/python-subprocess-module/

"""
import subprocess


def terminal(command=[], stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False,
             cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None,
             universal_newlines=None):
    """
    Execute given command, command

    :param capture_output:
    :param command: command
    :return: status code
    """
    try:
        if stdout and stderr:
            return subprocess.check_call(command, stdout=stdout, stderr=stderr)
        else:
            return subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
    except FileNotFoundError as e:
        print(f"Command failed with FileNotFoundError!")
        print(e)
        return 1



