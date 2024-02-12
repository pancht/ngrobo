from nrobo import NROBO_CONST


def get_host_version():
    """get host version of nrobo installation"""
    from nrobo import __version__
    return __version__


def get_pypi_index(package) -> None | str:
    """Get version of <package> from pypi and returns if package is found.
        return None otherwise."""

    # search
    # index
    # --require-virtualenv
    import subprocess
    result = subprocess.run(['pip', 'index', 'versions', package], text=True, capture_output=True)

    import re
    match = re.search(package + r" \(([\d]+4[.][\d]+[.][\d]+)\)", result.stdout)

    if match:
        return match.group(1)
    else:
        return None


def update_available() -> bool:
    """Returns version if package is available on pypi
        else returns None otherwise."""
    try:
        return not get_host_version() == get_pypi_index(NROBO_CONST.NROBO)
    except Exception as e:
        return False


def confirm_update() -> None:
    """Asks host to upgrade.
        Upgrades nrobo if host's reply is affirmative
        else returns with no action"""
    from nrobo import STYLE
    if not update_available():
        _pypi_version = get_pypi_index(NROBO_CONST.NROBO)
        from nrobo import console
        from rich.prompt import Prompt
        reply = Prompt.ask(f"An updated version ({_pypi_version}) is available for nrobo. Do you want to upgrade? "
                           f"\n(Type [{STYLE.HLGreen}]Yes[/] or [{STYLE.HLRed}]Y[/] to continue. Press any key to skip.)")
        if reply.strip().lower() in ["yes", "y"]:
            from nrobo import terminal
            with console.status("Updating nRoBo"):
                console.print("Update started")
                return_code = terminal(['pip', 'install', '--upgrade', 'nrobo'])
                if return_code == 0:
                    console.print("Update completed successfully.")
                else:
                    console.print("Update did not complete.")

        else:
            pass


if __name__ == '__main__':
    confirm_update()
