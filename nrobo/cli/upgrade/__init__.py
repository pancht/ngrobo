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
import time

from nrobo.util.version import Version
from nrobo import NROBO_CONST
from nrobo import console, terminal, STYLE
from rich.prompt import Prompt
from nrobo import __version__
from nrobo.util.network import internet_connectivity
import subprocess
import re


def get_host_version() -> str:
    """get host version of nrobo installation"""

    return __version__


def get_pypi_index(package) -> None | str:
    """Get version of <package> from pypi and returns if package is found.
        return None otherwise."""

    if not internet_connectivity():
        """Exit programme."""

        console.print(f"[{STYLE.HLRed}]No internet connectivity. Thus, Building package is aborted by nRoBo!")

        # HOW can I proceed without internet connectivity!
        # I need that for performing a few operations.
        # THUS, Quiting NOW!!!
        exit(1)

    result = subprocess.run(['pip', 'index', 'versions', package], text=True, capture_output=True, timeout=10)

    match = re.search(package + r" \(([\d]+4[.][\d]+[.][\d]+)\)", result.stdout)

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

    return Version(get_host_version()) < Version(get_pypi_index(NROBO_CONST.NROBO))


def confirm_update() -> None:
    """Asks host to upgrade.
        Upgrades nrobo if host's reply is affirmative
        else returns with no action"""

    host_version = get_host_version()
    pypi_version = get_pypi_index(NROBO_CONST.NROBO)

    if host_version <= Version('2024.6.10').version:
        # forced update and apply patch delivered in give version

        terminal(['pip', 'install', '--upgrade', f'nrobo==2024.6.10'], debug=False)

        return  # Silent patch applied for version 2024.6.10, thus, just return!

    if host_version < pypi_version:
        # Ok. Since the host version is lower than the latest version,
        # Lets' ask host user if he/she wants to upgrade.

        _pypi_version = get_pypi_index(NROBO_CONST.NROBO)

        reply = Prompt.ask(
            f"An updated version ({_pypi_version}) is available for nrobo. \n Your nRoBo version is {get_host_version()}. \n Do you want to upgrade? "
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

            return_code = terminal(['pip', 'install', '--upgrade', 'nrobo'], debug=True)

            if return_code == 0:
                console.print("Update completed successfully.")
            else:
                console.print("Update did not complete.")

            # allow host system to do some stuff!
            time.sleep(2)
