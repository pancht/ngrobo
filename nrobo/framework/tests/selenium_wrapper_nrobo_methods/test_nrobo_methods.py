import time

from pages import Page

from selenium.webdriver.common.by import By


class TestNRoBoSeleniumWrapperMethods:

    def test_open_an_url(self, driver, logger):
        """Example to see how to open an URL"""

        page = Page(driver, logger)

        page.get("https://pypi.org/")

    def test_get_browser_name(self, driver, logger):
        """Get driver/browser name"""

        page = Page(driver, logger)
        logger.info(f"Browser={page.name}")

    def test_get_title_of_the_current_page(self, driver, logger):
        """Get title of the current _page"""

        page = Page(driver, logger)
        page.get("http://pypi.org")
        logger.info(f"Title of the _page={page.title}")

    def test_get_url_of_the_current_page(self, driver, logger):
        """Get url of the current _page"""

        page = Page(driver, logger)
        page.get("http://pypi.org")
        logger.info(f"URL of the current _page={page.current_url}")

    def test_get_page_source_of_the_current_page(self, driver, logger):
        """Get _page source of the current _page"""

        page = Page(driver, logger)
        page.get("http://pypi.org")
        logger.info(f"Page source of the current _page\n\n{page.page_source}")

    def test_close_a_window_from_several_open_windows(self, driver, logger):
        """Example of closing a window"""

        page = Page(driver, logger)

        page.get("https://the-internet.herokuapp.com/")
        main_window = "The Internet"

        lnkMultipleWindow = (By.CSS_SELECTOR, "a[href='/windows']")
        page.click(*lnkMultipleWindow)

        lnkClickHere = (By.CSS_SELECTOR, "a[href='/windows/new']")
        page.click(*lnkClickHere)
        another_window = "New Window"

        # close the another window
        page.close(another_window)

        page.wait_for_a_while(3)

    def test_quit_all_windows(self, driver, logger):
        """Example of quiting all open windows"""

        page = Page(driver, logger)

        page.get("https://the-internet.herokuapp.com/")

        lnkMultipleWindow = (By.CSS_SELECTOR, "a[href='/windows']")
        page.click(*lnkMultipleWindow)

        lnkClickHere = (By.CSS_SELECTOR, "a[href='/windows/new']")
        page.click(*lnkClickHere)

        page.quit()

    def test_get_current_window_handle(self, driver, logger):
        """Get current window handle"""

        page = Page(driver, logger)

        page.get("https://the-internet.herokuapp.com/")

        logger.info(f"Current window handle={page.current_window_handle}")
        logger.info(f"Current window handle={page.windows['The Internet']}")

    def test_get_all_window_handles(self, driver, logger):
        """List out all the window handles"""

        page = Page(driver, logger)

        page.get("https://the-internet.herokuapp.com/")
        main_window_title = "The Internet"

        lnkMultipleWindow = (By.CSS_SELECTOR, "a[href='/windows']")
        page.click(*lnkMultipleWindow)

        lnkClickHere = (By.CSS_SELECTOR, "a[href='/windows/new']")
        page.click(*lnkClickHere)
        another_window_title = "New Window"

        logger.info(f"all handles = {page.window_handles}")
        logger.info(f"all handles = {page.windows}")

    def test_maximize_window(self, driver, logger):
        """Example of maximize window"""
        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")
        page.maximize_window()

    def test_fullscreen_mode(self, driver, logger):
        """Example of fullscreen mode"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")
        page.fullscreen_window()
        page.wait_for_a_while(5)

    def test_minimize_window(self, driver, logger):
        """Example of minimize a window"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")
        page.minimize_window()
        page.wait_for_a_while(3)

    def test_print_a_page_as_pdf(self, driver, logger):
        """Example of print a page as pdf"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")
        pdf = page.print_page()

        logger.info(f"{type(pdf)}")
        logger.info(f"{pdf}")
