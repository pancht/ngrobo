import logging
import time

import pytest
from selenium.webdriver.remote.webelement import WebElement

from nrobo.framework.pages.PageDemo import PageDemo


class TestSample1:

    @pytest.mark.sanity
    def test_google_branding_displayed_on_home_page(self, driver, logger):
        # Instantiate page object
        page_demo = PageDemo(driver, logger)
        # call page method
        page_demo.open_home_page()

        # Asset test condition
        assert page_demo.exist_branding_image() == True



