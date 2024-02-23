from selenium.webdriver.common.by import By

from nrobo.framework.pages import Page


class TestNroboWaitMethods:

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

        lnkDisappearingElements = (By.CSS_SELECTOR, "[href='/disappearing_elements']")
        page.click(*lnkDisappearingElements)

        mnuPortfolio = (By.CSS_SELECTOR, "[href='/portfolio/']")
        eleMnuPortfolio = page.find_element(*mnuPortfolio)
        page.click(*mnuPortfolio)
        page.wait_for_element_to_be_invisible(eleMnuPortfolio)

        page.wait_for_a_while(3)



