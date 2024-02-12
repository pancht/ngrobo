"""
@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

import logging

from selenium.webdriver.common.by import By

from nrobo.framework.pages import Page


class PageDemo(Page):
    """Demo page for illustration"""

    def __init__(self, driver, logger):
        """page constructor"""

        # Mandatory call to parent constructor
        # Always place as a first statement in each of your Page Classes
        super().__init__(driver, logger)

        # other initialization may proceed after this

    # Page locators definition should go here
    # ----------------------------------------
    imgGoogleBranding = (By.XPATH, "//img[@alt='Google']")
    txtSearch = (By.XPATH, "//textarea[@title='Search']")
    btnStaySignedOut = (By.XPATH, "//button[@aria-label='Stay signed out']")
    # lnkLogin = (By.ID, 'login2')
    # btnSubmit = (By, Value)
    # txtName = (By, Value)
    # ...

    # Page method specification should go here
    # ----------------------------------------

    def open_home_page(self):
        """Open google home page"""

        self.nprint(f'Open Google Home page')
        self.get("http:\\google.com")

    def exist_branding_image(self) -> bool:
        """
        Check if Google branding image found on the page.

        :return: True if found else return False
        """
        return self.find_element(*self.imgGoogleBranding).is_displayed()


