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

import sys
from dataclasses import dataclass
from cli.build import EnvCliSwitch
from cli.check import check
from nrobo import *
from nrobo.util.constants import Const
from nrobo.util.platform import Platforms
from nrobo.util.process import terminal

global __CUR_ENV__  # pylint: disable=W0604


@dataclass
class PublishTarget:
    """Publishing target."""

    PYPI = "pypi"
    TESTPYPI = "testpypi"


def publish(target, *, debug: bool = False, override: bool = False):
    """Check and publish package"""

    check(debug=debug)

    from rich.prompt import Prompt  # pylint: disable=C0415
    import nrobo.cli.detection as detect  # pylint: disable=C0415

    reply = Prompt.ask(
        f"Do You really want to publish version: [{STYLE.HLOrange}]"
        f"{detect.build_version_from_version_files()}[/]"
        f"\n(Type [{STYLE.HLGreen}]Yes[/] or [{STYLE.HLRed}]Y[/] "
        f"to continue. Press any key to skip.)"
    )
    if reply.strip().lower() not in ["yes", "y"]:
        # Hmm! Host don't want an update.
        # I don't know why he/she doesn't!!!
        # Anyway, I've had to obey her/his command,
        # Thus, I'm not going to update.
        console.print(
            f"[{STYLE.HLOrange}]Alright! You chose not to publish.\nPublish aborted by choice![/]"
        )
        return  # Bye, Host!

    global __CUR_ENV__  # pylint: disable=W0601

    if str(target).lower() == EnvCliSwitch.TEST:
        __CUR_ENV__ = PublishTarget.TESTPYPI
    elif str(target).lower() == EnvCliSwitch.PROD:
        __CUR_ENV__ = PublishTarget.PYPI
    else:
        print(
            f"Invalid target environment <{target}>. "
            f"Options: {EnvCliSwitch.TEST} | {EnvCliSwitch.PROD}"
        )
        sys.exit(1)

    with console.status(f"Publish on {PublishTarget.PYPI.upper()}..."):
        command = ""
        if os.environ[EnvKeys.HOST_PLATFORM] in [
            Platforms.DARWIN,
            Platforms.LINUX,
            Platforms.MACOS,
        ]:
            command = [
                "twine",
                "upload",
                "--repository",
                __CUR_ENV__,  # pylint: disable=E0601
                "dist" + os.sep + "*",
            ]
        elif os.environ[EnvKeys.HOST_PLATFORM] in [Platforms.WINDOWS]:
            command = [
                "twine",
                "upload",
                "--repository",
                __CUR_ENV__,
                Const.DOT + os.sep + "dist" + os.sep + "*.*",
            ]

        # add --skip-existing switch
        if override:
            command.append("--skip-existing")

        # Run command
        console_output = terminal(command, text=True, capture_output=True)

        if errors_in_console(r"(HTTPError:)", console_output.stdout):
            print(console_output.stdout)
            sys.exit(1)
        else:
            from cli.build import (  # pylint: disable=C0415
                get_version_from_yaml_version_files,
                write_new_version_to_nrobo_init_py_file,
            )

            build_version = get_version_from_yaml_version_files(target)
            write_new_version_to_nrobo_init_py_file(build_version)

            console.rule(
                f"nRoBo {get_version_from_yaml_version_files(target)} is published successfully."
            )


def errors_in_console(pattern: str, string: str) -> bool:
    """return True if pattern is found in string else false."""
    import re  # pylint: disable=C0415,W0621

    return re.search(pattern, string)
