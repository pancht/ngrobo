"""
@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

from selenium.webdriver.common.by import By
from pages import Page  # pylint: disable=E0401
from pages.PageSearch import PageSearch  # pylint: disable=E0401


class PagePyPiHome(Page):
    """Page class for PyPi.org home page"""

    def __init__(self, driver, logger):  # pylint: disable=W0246
        """page constructor"""

        # Mandatory call to parent constructor
        # Always place as a first statement in each of your Page Classes
        super().__init__(driver, logger)

        # other initialization may proceed after this

    # Page locators definition should go here
    # ----------------------------------------
    url = "https://pypi.org/"
    txt_search = (By.ID, "search")
    btn_search = (By.CSS_SELECTOR, ".search-form__button")
    # lnkLogin = (By.ID, 'login2')
    # btnSubmit = (By, Value)
    # txtName = (By, Value)
    # ...

    # Page method specification should go here
    # ----------------------------------------

    def open(self):
        """Open url."""
        self.logger.info(f"Open url: {self.url}")
        self.get(self.url)

    def search_button_present(self):
        """Search button present."""
        return self.find_element(*self.txt_search).is_displayed()

    def type_search_keyword(self, keyword):
        """type_search_keyword."""
        self.logger.info(f"Type search keyword: {keyword}")
        self.send_keys(*self.txt_search, keyword)

    def search(self) -> PageSearch:
        """Search."""
        self.logger.info("Click on Search button.")
        self.click(*self.btn_search)

        return PageSearch(self.driver, self.logger)
