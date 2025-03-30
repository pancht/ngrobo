# pylint: disable=R0401
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


def get_os_system_command(command: [str]) -> str:
    """Returns os.system command from given <command>"""

    _command = ""

    for _cmd in command:
        _command += str(_cmd) + " "

    return _command


def terminal(  # pylint: disable=W0613,R0911,R0912,R0913,R0917,R0914,W0102
    command=[],  # pylint: disable=W0102
    stdin=None,  # pylint: disable=W0613
    input=None,  # pylint: disable=W0613,W0622
    stdout=None,
    stderr=None,
    capture_output=False,
    shell=False,  # pylint: disable=W0613
    cwd=None,  # pylint: disable=W0613
    timeout=None,  # pylint: disable=W0613
    check=False,  # pylint: disable=W0613
    encoding=None,  # pylint: disable=W0613
    errors=None,  # pylint: disable=W0613
    text=None,
    env=None,  # pylint: disable=W0613
    universal_newlines=None,  # pylint: disable=W0613
    debug=False,
    use_os_system_call=False,
) -> int:
    """Execute given command, command

    :param debug:
    :param universal_newlines:
    :param env:
    :param text:
    :param errors:
    :param encoding:
    :param check:
    :param timeout:
    :param cwd:
    :param shell:
    :param stderr:
    :param stdout:
    :param input:
    :param stdin:
    :param capture_output:
    :param command: command
    :return: status code
    """
    if use_os_system_call:
        return os.system(get_os_system_command(command))

    if debug is False:
        # check environment debug flag
        from nrobo import EnvKeys  # pylint: disable=C0415

        if str(os.environ[EnvKeys.DEBUG]) == "True":
            debug = True

    try:
        if text and capture_output:
            try:
                return subprocess.run(  # pylint: disable=W1510
                    command, text=text, capture_output=capture_output
                )
            except subprocess.CalledProcessError as e:
                print(f"Command failed with return code {e.returncode}: \n{e}")
                return e.returncode

        if debug:
            try:
                subprocess.check_call(command)
            except subprocess.CalledProcessError as e:
                if e.returncode == 1:
                    print(f"Command failed with return code {e.returncode}: \n{e}")
                return e.returncode
        if (stdout and stderr) or debug is False:
            try:
                subprocess.check_call(
                    command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
                )
            except subprocess.CalledProcessError as e:
                if e.returncode == 1:
                    print(f"Command failed with return code {e.returncode}: \n{e}")
                return e.returncode
        else:
            try:
                subprocess.check_call(command)
            except subprocess.CalledProcessError as e:
                if not e.returncode == 1:
                    print(f"Command failed with return code {e.returncode}: \n{e}")
                return e.returncode
    except FileNotFoundError as e:
        print(f"Command failed with FileNotFoundError!\n{e}")
        return 100
    except Exception as e:  # pylint: disable=W0718
        print(f"Command failed with exception:\n\t{e}")
        return 100

    return 0
