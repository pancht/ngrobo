import logging
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Union
from nrobo.selenese import NRobo
AnyBrowser = Union[None, WebDriver]


class Page(NRobo):

    def __init__(self, driver=AnyBrowser, logger=None | logging.Logger):
        """constructor"""
        # call parent constructor
        super().__init__(driver, logger)
        self.driver = driver
        self.logger = logger

    ##################################################
    # Implement application specific page methods here
    ##################################################



