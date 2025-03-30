"""Nrobo wait methods."""

from selenium.webdriver.common.by import By

from nrobo.framework.pages import Page


class TestNroboWaitMethods:
    """Nrobo wait method tests."""

    def test_wait_for_page_to_be_loaded(self, driver, logger):
        """Example of wait for page to be loaded"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        page.wait_for_page_to_be_loaded()

    def test_wait_for_a_while(self, driver, logger):
        """Example of wait_for_a_while method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        page.wait_for_a_while(3)

    def test_wait_for_element_to_be_invisible(self, driver, logger):
        """Example of wait_for_element_to_be_invisible method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_disappearing_elements = (By.CSS_SELECTOR, "[href='/disappearing_elements']")
        page.click(*lnk_disappearing_elements)

        mnu_portfolio = (By.CSS_SELECTOR, "[href='/portfolio/']")
        ele_mnu_portfolio = page.find_element(*mnu_portfolio)
        page.click(*mnu_portfolio)
        page.wait_for_element_to_be_invisible(ele_mnu_portfolio)

        page.wait_for_a_while(3)
