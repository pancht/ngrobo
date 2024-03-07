import pytest
from selenium.webdriver.common.by import By

from pages import Page


class TestActionChainMethods:

    @pytest.mark.skip(reason="This test is an nRoBo example test.")
    def test_action_chain_reference(self, driver, logger):
        """Example of action chain reference"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnkDragAndDrop = (By.CSS_SELECTOR, "[href='/drag_and_drop']")
        page.click(*lnkDragAndDrop)

        boxHeaderA = (By.XPATH, "//header[text()='A']")
        boxHeaderB = (By.XPATH, "//header[text()='B']")

        eleHeaderA = page.find_element(*boxHeaderA)
        eleHeaderB = page.find_element(*boxHeaderB)
        page.action_chain().drag_and_drop(eleHeaderA, eleHeaderB).perform()

        page.wait_for_a_while(4)


