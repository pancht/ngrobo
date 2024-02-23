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
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Union
from nrobo.selenese import NRobo

AnyBrowser = Union[None, WebDriver]
from selenium.webdriver.common.actions.wheel_input import WheelInput
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.key_input import KeyInput

AnyDevice = Union[PointerInput, KeyInput, WheelInput]


class Page(NRobo):
    """
    Page class is the base class for every _page objects
    that one is going to be created for his/her project.

    Page class inherits wrapper classes wraps the most
    frequently used api's of the Webdriver, WebElement,
    and other selenium classes which brings the power of
    readability of your scripts. Along with readable code,
    comes the power of highly maintainable and understandable
    code-base.

    And many more...
    I would request to checkout video tutorials uploaded at the
    following YouTube channel: https://shorturl.at/lpqKS

    Example usage: Assume that you want to create a Page Object
    in your automation project for home _page, then you should
    declare your Page Class as following:

    Package: pages
    File: home.py
    ============FileContent of home.py===========================

    from pages import Page

    class PageHome(Page):

        def __init__(self, driver, logger):
            super().__init__(driver, logger)

            # Definition of home _page locators should go below

        def page_method_1(self):
            ...

        def page_mathod_2(self):
            ...

        # and so on per project need.
    """

    def __init__(self, driver=AnyBrowser, logger=None | logging.Logger, duration: int = 250,
                 devices: list[AnyDevice] | None = None):
        """constructor"""
        # call parent constructor
        super().__init__(driver, logger, duration=duration, devices=devices)

    ##################################################
    # Implement application specific _page methods here
    ##################################################
