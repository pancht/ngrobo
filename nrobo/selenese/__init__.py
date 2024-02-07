import functools
import os
import time
from abc import ABC
import logging
from nrobo.cli.tools import nprint
from nrobo.cli import STYLE

from selenium.webdriver.remote.webelement import WebElement
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

from nrobo.util.common import Common


class WAITS:
    """Supported wait types in nrobo.
    These names are used as key in nrobo-config.yaml."""
    SLEEP = "sleep"
    WAIT = "static_wait"
    TIMEOUT = "timeout"


@functools.lru_cache(maxsize=None)
def read_nrobo_configs():
    return Common.read_yaml(f"nrobo{os.sep}framework{os.sep}nrobo-config.yaml")


class NroboSeleniumWrapper(ABC, PageFactory):
    """
    Customized wrapper in nrobo of selenium-webdriver commands with enhanced functionality.

    This class is not instantiable.

    Doc: https://www.selenium.dev/selenium/docs/api/py/#
    """

    # Webdriver class variable
    driver = None
    # Logger class variable
    logger = None

    def __init__(self, driver: webdriver, logger: logging.Logger):
        """
        Constructor - NroboSeleniumWrapper

        :param driver: reference to selenium webdriver
        :param logger: reference to logger instance
        """
        super().__init__()
        self.driver = driver
        self.logger = logger
        self.nconfig = read_nrobo_configs()

        # wait for page load
        self.wait_for_page_to_be_loaded()

    def wait_for_page_to_be_loaded(self):
        """Waits for give timeout time for page to completely load.
        timeout time is configurable in nrobo-config.yaml"""

        nprint("Wait for page load...", style=STYLE.HLOrange)
        try:
            WebDriverWait(self.driver, self.nconfig[WAITS.TIMEOUT]).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete')
        except TimeoutException as te:
            nprint(f"Exception: {te}", STYLE.HLRed)
        except AttributeError as ae:
            nprint(f"Exception: {ae}", STYLE.HLRed)
        nprint("End of Wait for page load...", style=STYLE.PURPLE4)

    @staticmethod
    def wait_for_a_while(time_in_sec):
        """
        Pause for <time_in_sec>

        :param time_in_sec:
        :return:
        """
        time.sleep(time_in_sec)

    def wait_for_element_to_be_invisible(self, locator: WebElement | tuple[str, str]):
        """wait till <element> disappears from the UI"""

        nprint("wait for element invisible", style=STYLE.HLOrange)

        # wait a little
        self.wait_for_a_while(self.nconfig[WAITS.WAIT])

        # wait until the locator becomes invisible
        WebDriverWait(self.driver, self.nconfig[WAITS.WAIT]).until(
            expected_conditions.invisibility_of_element_located(locator))

        self.wait_for_a_while(self.nconfig[WAITS.WAIT])

        nprint("end of wait for element invisible", style=STYLE.PURPLE4)

    def wait_for_element_to_be_clickable(self, timeout=None):
        """
        wait till element is visible and clickable.

        :param timeout:
        :return:
        """
        super().element_to_be_clickable(timeout)

    def get(self, url):
        """opens the url in browser"""
        if isinstance(url, str):
            url = str(url).replace('\\', "\\\\")

        nprint(f"Go to url <{url}>", logger=self.logger)
        self.driver.get(url)
