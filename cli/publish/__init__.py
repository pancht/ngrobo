"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

This module has actions pertaining to nRoBo build
process.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

from cli.build import ENV_CLI_SWITCH
from cli.check import check
from nrobo import *
from nrobo.util.common import Common
from nrobo.util.constants import CONST
from nrobo.util.platform import PLATFORMS
from nrobo.util.process import terminal
from cli.build import ENV_CLI_SWITCH

global __CUR_ENV__


class PUBLISH_TARGET:
    """Publishing target."""

    PYPI = "pypi"
    TESTPYPI = "testpypi"


def publish(target, *, debug: bool = False, override: bool = False):
    """Check and publish package"""

    check(debug=debug)

    from rich.prompt import Prompt
    import nrobo.cli.detection as detect
    reply = Prompt.ask(
        f"Do You really want to publish version: [{STYLE.HLOrange}]{detect.build_version_from_version_files()}[/]"
        f"\n(Type [{STYLE.HLGreen}]Yes[/] or [{STYLE.HLRed}]Y[/] to continue. Press any key to skip.)")
    if not reply.strip().lower() in ["yes", "y"]:
        # Hmm! Host don't want an update.
        # I don't know why he/she doesn't!!!
        # Anyway, I've had to obey her/his command,
        # Thus, I'm not going to update.
        console.print(f"[{STYLE.HLOrange}]Alright! You chose not to publish.\nPublish aborted by choice![/]")
        return  # Bye, Host!

    global __CUR_ENV__

    if str(target).lower() == ENV_CLI_SWITCH.TEST:
        __CUR_ENV__ = PUBLISH_TARGET.TESTPYPI
    elif str(target).lower() == ENV_CLI_SWITCH.PROD:
        __CUR_ENV__ = PUBLISH_TARGET.PYPI
    else:
        print(f"Invalid target environment <{target}>. Options: {ENV_CLI_SWITCH.TEST} | {ENV_CLI_SWITCH.PROD}")
        exit(1)

    # Get pypi token
    pypi_cred = Common.read_yaml('key/pypi_cred.yaml')
    pypi_token = pypi_cred['token']
    TOKEN = '__token__'
    with console.status(f"Publish on {PUBLISH_TARGET.PYPI.upper()}..."):
        command = ""
        if os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.DARWIN, PLATFORMS.LINUX, PLATFORMS.MACOS]:
            command = ["twine", "upload", "--repository", __CUR_ENV__,
                       '--username', TOKEN, '--password', f"{pypi_token}",
                       "dist" + os.sep + "*"]
        elif os.environ[EnvKeys.HOST_PLATFORM] in [PLATFORMS.WINDOWS]:
            command = ["twine", "upload", "--repository", __CUR_ENV__,
                       '--username', TOKEN, '--password', f"{pypi_token}",
                       CONST.DOT + os.sep + "dist" + os.sep + "*.*"]

        # add --skip-existing switch
        if override:
            command.append("--skip-existing")

        # Run command
        console_output = terminal(command, text=True, capture_output=True)

        if errors_in_console(r'(HTTPError:)', console_output.stdout):
            print(console_output.stdout)
            exit(1)
        else:
            from cli.build import get_version_from_yaml_version_files, write_new_version_to_nrobo_init_py_file
            build_version = get_version_from_yaml_version_files(target)
            write_new_version_to_nrobo_init_py_file(build_version)

            console.rule(f"nRoBo {get_version_from_yaml_version_files(target)} is published successfully.")


def errors_in_console(pattern: str, string: str) -> bool:
    """return True if pattern is found in string else false."""
    import re
    return re.search(pattern, string)
