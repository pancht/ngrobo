"""Browser switches module."""

from nrobo.framework.pages import Page  # pylint: disable=R0801


class TestBrowserSwitches:  # pylint: disable=R0903
    """Browser switches tests."""

    def test_anti_bot_undetected_chrome(self, driver, logger):
        """Anti bot undetected chrome test."""
        page = Page(driver=driver, logger=logger)

        page.get("https://nowsecure.nl")

        page.wait_for_a_while(3)
