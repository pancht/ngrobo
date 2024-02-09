# rich console
from nrobo import console, STYLE
import logging


def nprint(msg, style=STYLE.HLGreen, logger=None):
    """Prints <msg> to console and logs it as well if logger is given"""

    # print msg to console
    console.print(f"[{style}]{msg}")

    if logger is not None:
        """if logger is given"""

        # log the msg
        logger.log(logging.INFO, f"{msg}")