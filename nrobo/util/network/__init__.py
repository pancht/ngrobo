"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================


networking functions.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmaill.com
"""

import subprocess


def internet_connectivity() -> bool:
    """Returns True if there is internet connectivity
        else return False"""
    try:
        from nrobo.main import terminal
        # subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        return terminal(["ping", "-c", "1", "8.8.8.8"]) == 0
    except subprocess.CalledProcessError:
        return False
