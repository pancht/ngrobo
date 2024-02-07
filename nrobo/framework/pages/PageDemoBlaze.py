import logging

from selenium.webdriver.common.by import By

from nrobo.framework.pages import Page


class PageDemoBlaze(Page):
    """Google Home page locators and page methods"""

    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    # locators
    # --------
    lnkLogin = (By.ID, 'login2')

    # Page methods
    # ------------

    def go_login_page(self):
        # return self.find_element(*self.linkLogin).tag_name
        return self.tag_name(*self.lnkLogin)



