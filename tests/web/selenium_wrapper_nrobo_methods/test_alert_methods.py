# pylint: disable=R0801
"""test alert methods module."""

import pytest
from selenium.webdriver.common.by import By

from nrobo.framework.pages import Page


class TestAlertMethods:
    """Alert methods tests."""

    @pytest.mark.skip(reason="This test fails in Headless mode")
    def test_example_accept_alert(self, driver, logger):
        """Example of accepting alerts"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_java_script_alert = (By.CSS_SELECTOR, "[href='/javascript_alerts']")
        page.click(*lnk_java_script_alert)

        btn_js_alert = (By.XPATH, "//button[text()='Click for JS Alert']")
        page.click(*btn_js_alert)
        page.accept_alert()

        page.wait_for_a_while(3)

    @pytest.mark.skip(reason="This test fails in Headless mode")
    def test_example_dismiss_alert(self, driver, logger):
        """Example of dismiss alert"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_java_script_alert = (By.CSS_SELECTOR, "[href='/javascript_alerts']")
        page.click(*lnk_java_script_alert)

        btn_js_alert = (By.XPATH, "//button[text()='Click for JS Alert']")
        page.click(*btn_js_alert)
        page.dismiss_alert()

        page.wait_for_a_while(3)

    @pytest.mark.skip(reason="This test fails in Headless mode")
    def test_send_keys_to_prompt(self, driver, logger):
        """Example of sending keys to the prompt"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_java_script_alert = (By.CSS_SELECTOR, "[href='/javascript_alerts']")
        page.click(*lnk_java_script_alert)

        btn_js_prompt = (By.XPATH, "//button[text()='Click for JS Prompt']")
        page.click(*btn_js_prompt)

        page.send_keys_and_accept_alert("Sending keys to the JS Alert prompt.")

        page.wait_for_a_while(3)

    @pytest.mark.skip(reason="This test fails in Headless mode")
    def test_example_get_alert_text(self, driver, logger):
        """Example of get alert text"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_java_script_alert = (By.CSS_SELECTOR, "[href='/javascript_alerts']")
        page.click(*lnk_java_script_alert)

        btn_js_alert = (By.XPATH, "//button[text()='Click for JS Alert']")
        page.click(*btn_js_alert)
        logger.info(f"Alert text=> {page.get_alert_text()}")
        page.dismiss_alert()

        page.wait_for_a_while(3)
