from rich.console import Console
from nrobo.cli.formatting import themes as th
from nrobo.cli import STYLE

console = Console(theme=th)

# following globals will be set at runtime
__APP_NAME__ = ""
__URL__ = ""
__USERNAME__ = ""
__PASSWORD__ = ""
__BROWSER__ = ""

from nrobo.exceptions import BrowserNotSupported


class Browsers:
    CHROME = 'chrome'
    CHROME_HEADLESS = "chrome_headless"
    EDGE = 'edge'
    FIREFOX = 'firefox'
    IE = "ie"
    SAFARI = 'safari'


supported_browsers = [Browsers.CHROME, Browsers.CHROME_HEADLESS, Browsers.SAFARI]
supported_browsers_in_future = [Browsers.EDGE, Browsers.IE, Browsers.FIREFOX]


def raise_exception_if_browser_not_supported(browser_name):
    """raise exception if <browser_name> is not supported in nrobo framework"""
    if str(browser_name).lower() in supported_browsers_in_future:
        console.print(
            f"[{STYLE.HLOrange}]Support for {browser_name} browser will be coming in upcoming releases. Sorry for the "
            f"convenience.")
        exit(1)
    if browser_name not in supported_browsers:
        raise BrowserNotSupported(browser_name)
