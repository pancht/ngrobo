from nrobo.framework.pages import Page


class TestBrowserSwitches:

    def test_anti_bot_undetected_chrome(self, driver, logger):
        page = Page(driver=driver, logger=logger)

        page.get("https://nowsecure.nl")

        page.wait_for_a_while(3)
