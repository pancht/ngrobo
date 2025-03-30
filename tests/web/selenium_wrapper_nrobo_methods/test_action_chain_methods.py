"""Action chain methods."""

from selenium.webdriver.common.by import By

from nrobo.framework.pages import Page


class TestActionChainMethods:  # pylint: disable=R0903
    """Action Chain method tests."""

    def test_action_chain_reference(self, driver, logger):
        """Example of action chain reference"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_drag_and_drop = (By.CSS_SELECTOR, "[href='/drag_and_drop']")
        page.click(*lnk_drag_and_drop)

        box_header_a = (By.XPATH, "//header[text()='A']")
        box_header_b = (By.XPATH, "//header[text()='B']")

        ele_header_a = page.find_element(*box_header_a)
        ele_header_b = page.find_element(*box_header_b)
        page.action_chain().drag_and_drop(ele_header_a, ele_header_b).perform()

        page.wait_for_a_while(4)
