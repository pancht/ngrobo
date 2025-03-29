from appium.webdriver.common.appiumby import AppiumBy

from nrobo.framework.pages import Page


class TestAppium:
    """Sample mobile tests using appium open source library"""

    def test_namastey_appium_world_ios_device(self, driver, logger):
        """First appium test on ios device"""
        logger.info("Create page object")
        page = Page(driver=driver, logger=logger)
        page.click(by=AppiumBy.IOS_PREDICATE, value='name == "Safari"')
        page.wait_for_a_while(2)




