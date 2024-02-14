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
from nrobo import NROBO_CONST


def get_host_version():
    """get host version of nrobo installation"""
    from nrobo import __version__
    return __version__


def get_pypi_index(package) -> None | str:
    """Get version of <package> from pypi and returns if package is found.
        return None otherwise."""

    from nrobo.util.network import internet_connectivity
    if not internet_connectivity():
        """Exit programme."""
        from nrobo import console, STYLE
        console.print(f"[{STYLE.HLRed}]No internet connectivity. Thus, Building package is aborted by nRoBo!")
        exit(1)

    import subprocess
    result = subprocess.run(['pip', 'index', 'versions', package], text=True, capture_output=True, timeout=10)

    import re
    match = re.search(package + r" \(([\d]+4[.][\d]+[.][\d]+)\)", result.stdout)

    if match:
        return match.group(1)
    else:
        return None


def update_available() -> bool:
    """Returns version if package is available on pypi
        else returns None otherwise."""
    return not get_host_version() == get_pypi_index(NROBO_CONST.NROBO)


def confirm_update() -> None:
    """Asks host to upgrade.
        Upgrades nrobo if host's reply is affirmative
        else returns with no action"""
    from nrobo import STYLE
    if update_available():
        _pypi_version = get_pypi_index(NROBO_CONST.NROBO)
        from nrobo import console
        from rich.prompt import Prompt
        reply = Prompt.ask(f"An updated version ({_pypi_version}) is available for nrobo. \n Your nRoBo version is {get_host_version()}. \n Do you want to upgrade? "
                           f"\n(Type [{STYLE.HLGreen}]Yes[/] or [{STYLE.HLRed}]Y[/] to continue. Press any key to skip.)"
                           f"\nNOTE: To suppress this propmt, apply CLI switch, --suppress, to your launcher command.")
        if reply.strip().lower() in ["yes", "y"]:
            from nrobo import terminal
            with console.status("Updating nRoBo"):
                console.print("Update started")
                return_code = terminal(['pip', 'install', '--upgrade', 'nrobo'],debug=True)
                if return_code == 0:
                    console.print("Update completed successfully.")
                else:
                    console.print("Update did not complete.")

        else:
            pass

