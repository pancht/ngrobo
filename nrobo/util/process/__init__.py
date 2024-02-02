"""
subprocess doc: https://docs.python.org/3/library/subprocess.html

"""
import os, subprocess as sp


def run_command(command=[], stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False,
                cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None,
                universal_newlines=None):
    """
    Execute given command, command

    :param capture_output:
    :param command: command
    :return: status code
    """

    try:
        # status_code = os.system(command)
        cp = sp.run(command, capture_output)
    except Exception as e:
        print(e)

    # return with status_code.
    return cp.returncode
