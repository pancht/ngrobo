from nrobo.framework.pages import Page


class TestSample1():

    def test_one(self, driver, logger):
        page = Page(driver, logger)
        page.get("http:\\www.google.com")


