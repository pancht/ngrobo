import logging

from selenium import webdriver

from nrobo.selenese import NroboSeleniumWrapper
from typing import Union

AnyBrowser = Union[None, webdriver.Chrome, webdriver.Edge,
                   webdriver.Ie, webdriver.Safari, webdriver.Firefox]


class Page(NroboSeleniumWrapper):

    def __init__(self, driver=AnyBrowser, logger=None | logging.Logger):
        """constructor"""
        # call parent constructor
        super().__init__(driver, logger)
