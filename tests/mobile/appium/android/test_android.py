from appium.webdriver.common.appiumby import AppiumBy

from nrobo.framework.pages import Page


class TestAppium:
    """Sample mobile tests using appium open source library"""

    def test_namastey_appium_world(self, driver, logger):
        """First appium test"""
        logger.info("Create page object")
        page = Page(driver=driver, logger=logger)
        page.click(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        # page.wait_for_a_while(5)
