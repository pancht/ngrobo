import logging
import time

import pytest

from nrobo.framework.pages.PageDemoBlaze import PageDemoBlaze


class TestSample1:

    @pytest.mark.sanity
    def test_one(self, driver, logger):
        # page = Page(driver, logger)
        # page.get("http:\\www.google.com")
        # page.find_element(By.ID, "app")

        pageDemoBlaze = PageDemoBlaze(driver, logger)
        pageDemoBlaze.get("https://www.demoblaze.com/")
        logger.log(logging.INFO, pageDemoBlaze.go_login_page())


