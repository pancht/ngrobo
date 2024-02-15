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
import logging

# rich console
from nrobo import console, STYLE


def nprint(msg, style=STYLE.HLGreen, logger=None):
    """Prints <msg> to console and logs it as well if logger is given"""

    # print msg to console
    console.print(f"[{style}]{msg}")

    if logger is not None:
        """if logger is given"""

        # log the msg
        logger.log(logging.INFO, f"{msg}")