import logging

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from nrobo.selenese import NRoboWebdriverWrapper, NRoboWaitImplementations
from typing import Union

AnyBrowser = Union[None, WebDriver]


class Page(NRoboWebdriverWrapper, NRoboWaitImplementations):

    def __init__(self, driver=AnyBrowser, logger=None | logging.Logger):
        """constructor"""
        # call parent constructor
        super().__init__(driver, logger)
