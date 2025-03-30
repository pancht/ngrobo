"""Page Search page."""

from pages import Page  # pylint: disable=E0401

from selenium.webdriver.common.by import By


class PageSearch(Page):  # pylint: disable=R0903
    """Page Search."""

    def __init__(self, driver, logger):  # pylint: disable=W0246
        super().__init__(driver, logger)

    # Page locators
    linkNroboLink = (
        By.CSS_SELECTOR,
        "a[href='/project/nrobo/'] h3 span.package-snippet__name",
    )

    # associated page method
    def nrobo_link_is_present(self) -> bool:
        """nrobo_link_is_present."""
        self.logger.info("Check if nrobo link is available.")
        return self.is_displayed(*self.linkNroboLink)
