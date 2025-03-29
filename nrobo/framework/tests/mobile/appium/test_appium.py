from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from pages import Page


class TestAppium:

    def test_namastey_appium_world(self, driver, logger):
        """First appium test"""
        logger.info("Create page object")
        page = Page(driver=driver, logger=logger)
        # page.click(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
