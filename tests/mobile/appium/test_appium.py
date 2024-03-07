from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from nrobo.framework.pages import Page

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium:

    def test_namastey_appium_world(self, driver, logger):
        """First appium test"""
        logger.info("Create page object")
        page = Page(driver=driver, logger=logger)
        #page.click(by=AppiumBy.XPATH, value='//*[@text="Battery"]')




