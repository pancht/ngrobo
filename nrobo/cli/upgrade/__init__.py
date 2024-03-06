"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Definition of nRoBo update utility.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
import os
import time
from nrobo.util.network import internet_connectivity
import subprocess
import re
import nrobo.cli.detection as detect


def get_host_version() -> str:
    """get host version of nrobo installation"""
    from nrobo import __version__
    return __version__


def get_pypi_index(package) -> None | str:
    """Get version of <package> from pypi and returns if package is found.
        return None otherwise."""

    if not internet_connectivity():
        """Exit programme."""
        from nrobo import console, STYLE
        console.print(f"[{STYLE.HLRed}]No internet connectivity!")

        # HOW can I proceed without internet connectivity!
        # I need that for performing a few operations.
        # THUS, Quiting NOW!!!
        exit(1)

    result = subprocess.run(['pip', 'index', 'versions', package], text=True, capture_output=True, timeout=10)

    match = re.search(package + r" \(([\d]+[.][\d]+[.][\d]+)\)", result.stdout)

    if match:
        # Tts' a match!
        return match.group(1)
    else:
        # OOPS!, version not found on PyPi. HOW?
        # Don't want to OVERTHINK!
        # Lets' JUST Quit the world of UNKNOWN!
        return None


def update_available() -> bool:
    """Returns version if package is available on pypi
        else returns None otherwise."""
    from nrobo.util.version import Version
    from nrobo import NROBO_CONST
    return Version(get_host_version()) < Version(get_pypi_index(NROBO_CONST.NROBO))


def confirm_update() -> None:
    """Asks host to upgrade.
        Upgrades nrobo if host's reply is affirmative
        else returns with no action"""
    from nrobo.util.version import Version
    from nrobo import NROBO_CONST
    host_version = Version(get_host_version())
    pypi_version = Version(get_pypi_index(NROBO_CONST.NROBO))

    # Apply patches silently
    if Version.present_is_a_patch_release(pypi_version.version, host_version.version) \
            or Version.present_is_a_minor_release(pypi_version.version, host_version.version)\
            or Version.present_is_a_major_release(pypi_version.version, host_version.version):

        from nrobo import console, terminal, STYLE
        from nrobo.cli.ncodes import EXIT_CODES

        version_forced_update = Version(host_version.version)

        if Version.present_is_a_major_release(pypi_version.version, host_version.version):
            request_version = Version.first_major_release(pypi_version.version)
            terminal(['pip', 'install', '--upgrade', f'nrobo=={request_version}', '--require-virtualenv'],
                     debug=False)
            console.rule(f"[{STYLE.HLOrange}]NOTE: A silent major update was installed from "
                         f"{host_version.version} => {pypi_version.version}. Please rerun tests.")
            exit(0)

        elif Version.present_is_a_minor_release(pypi_version.version, host_version.version):

            request_version = Version.first_minor_release(pypi_version.version)
            terminal(['pip', 'install', '--upgrade', f'nrobo=={request_version}', '--require-virtualenv'],
                     debug=False)

            console.rule(f"[{STYLE.HLOrange}]NOTE: A silent minor update was installed from "
                         f"{host_version.version} => {pypi_version.version}. Please rerun tests.")
            exit(0)

        elif host_version <= Version("2024.12.0"):
            # forced update and apply patch delivered in give version

            terminal(['pip', 'install', '--upgrade', f'nrobo=={(host_version + 1).version}', '--require-virtualenv'],
                     debug=False)

        if detect.production_machine() and not detect.developer_machine()\
                and host_version <= Version("2024.12.0"):
            console.rule(f"[{STYLE.HLOrange}]{EXIT_CODES['10001'][1]}")
            exit(EXIT_CODES['10001'][0])

        # return  # Silent patch applied for version 2024.6.10, thus, just return!

    # Ask for major and minor version update
    if host_version < pypi_version:
        # Ok. Since the host version is lower than the latest version,
        # Lets' ask host user if he/she wants to upgrade.
        from nrobo import EnvKeys
        # Enabled Major and Minor release by default.
        # Thus, stopping patch releases from version 2024.25.8
        return

        if int(os.environ[EnvKeys.SUPPRESS_PROMPT]):
            """Return as --suppress switch is supplied"""
            return

        _pypi_version = get_pypi_index(NROBO_CONST.NROBO)
        from nrobo import console, terminal, STYLE
        from rich.prompt import Prompt
        reply = Prompt.ask(
            f"An updated version ({_pypi_version}) is available for nrobo. "
            f"\n Your nRoBo version is {get_host_version()}. "
            f"\n Do you want to upgrade? "
            f"\n(Type [{STYLE.HLGreen}]Yes[/] or [{STYLE.HLRed}]Y[/] to continue. Press any key to skip.)"
            f"\nNOTE: To suppress this propmt, apply CLI switch, --suppress, to your launcher command.")
        if not reply.strip().lower() in ["yes", "y"]:
            # Hmm! Host don't want an update.
            # I don't know why he/she doesn't!!!
            # Anyway, I've had to obey her/his command,
            # Thus, I'm not going to update.
            return  # Bye, Host!

        with console.status("Updating nRoBo"):
            # Host chose to allow update. Lets' update then!

            console.print("Update started")

            return_code = terminal(['pip', 'install', '--upgrade', 'nrobo', '--require-virtualenv'], debug=True)

            if return_code == 0:
                console.print("Update completed successfully.")
            else:
                console.print("Update did not complete.")

            # allow host system to do some stuff!
            time.sleep(2)
