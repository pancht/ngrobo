from pages import Page

from selenium.webdriver.common.by import By


class PageSearch(Page):

    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    # Page locators
    linkNroboLink = (By.CSS_SELECTOR, "a[href='/project/nrobo/'] h3 span.package-snippet__name")

    # associated page method
    def nrobo_link_is_present(self) -> bool:
        self.logger.info("Check if nrobo link is available.")
        return self.is_displayed(*self.linkNroboLink)
