from selenium.webdriver.common.by import By

from nrobo.framework.pages import Page


class TestAlertMethods:

    def test_example_accept_alert(self, driver, logger):
        """Example of accepting alerts"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnkJavaScriptAlert = (By.CSS_SELECTOR, "[href='/javascript_alerts']")
        page.click(*lnkJavaScriptAlert)

        btnJSAlert = (By.XPATH, "//button[text()='Click for JS Alert']")
        page.click(*btnJSAlert)
        page.accept_alert()

        page.wait_for_a_while(3)

    def test_example_dismiss_alert(self, driver, logger):
        """Example of dismiss alert"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnkJavaScriptAlert = (By.CSS_SELECTOR, "[href='/javascript_alerts']")
        page.click(*lnkJavaScriptAlert)

        btnJSAlert = (By.XPATH, "//button[text()='Click for JS Alert']")
        page.click(*btnJSAlert)
        page.dismiss_alert()

        page.wait_for_a_while(3)

    def test_send_keys_to_prompt(self, driver, logger):
        """Example of sending keys to the prompt"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnkJavaScriptAlert = (By.CSS_SELECTOR, "[href='/javascript_alerts']")
        page.click(*lnkJavaScriptAlert)

        btnJSPrompt = (By.XPATH, "//button[text()='Click for JS Prompt']")
        page.click(*btnJSPrompt)

        page.send_keys_and_accept_alert("Sending keys to the JS Alert prompt.")

        page.wait_for_a_while(3)

    def test_example_get_alert_text(self, driver, logger):
        """Example of get alert text"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnkJavaScriptAlert = (By.CSS_SELECTOR, "[href='/javascript_alerts']")
        page.click(*lnkJavaScriptAlert)

        btnJSAlert = (By.XPATH, "//button[text()='Click for JS Alert']")
        page.click(*btnJSAlert)
        logger.info(f"Alert text=> {page.get_alert_text()}")
        page.dismiss_alert()

        page.wait_for_a_while(3)

