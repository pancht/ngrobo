"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

nRoBo Constants.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
from nrobo.exceptions import NRoBoBrowserNotSupported

from rich.console import *
from nrobo.cli.formatting import *

from nrobo.cli import *
console = Console(theme=themes)


class Browsers:
    """browser names constants"""

    CHROME = 'chrome'
    CHROME_HEADLESS = "chrome_headless"
    ANTI_BOT_CHROME = "anti_bot_chrome"
    EDGE = 'edge'
    FIREFOX = 'firefox'
    FIREFOX_HEADLESS = "firefox_headless"
    IE = "ie"
    SAFARI = 'safari'
    OPERA = 'opera'


# list holding supported browser in nRoBo framework
supported_browsers = [Browsers.CHROME, Browsers.CHROME_HEADLESS, Browsers.ANTI_BOT_CHROME,
                      Browsers.SAFARI,
                      Browsers.FIREFOX, Browsers.FIREFOX_HEADLESS, Browsers.EDGE, Browsers.IE]
# # list holding browsers not supported in nRoBo framework
supported_browsers_in_future = [Browsers.OPERA]


def raise_exception_if_browser_not_supported(browser_name):
    """raise exception if <browser_name> is not supported in nrobo framework"""

    if str(browser_name).lower() in supported_browsers_in_future:
        console.print(
            f"[{STYLE.HLOrange}]Support for {browser_name} browser will be coming in upcoming releases. Sorry for the "
            f"convenience.")
        exit(1)
    if browser_name not in supported_browsers:
        raise NRoBoBrowserNotSupported(browser_name)




