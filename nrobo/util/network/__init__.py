import subprocess


def internet_connectivity() -> bool:
    """Returns True if there is internet connectivity
        else return False"""
    try:
        from nrobo import terminal
        # subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        return terminal(["ping", "-c", "1", "8.8.8.8"]) == 0
    except subprocess.CalledProcessError:
        return False