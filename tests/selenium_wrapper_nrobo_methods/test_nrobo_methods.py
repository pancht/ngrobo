import time

import pytest

from nrobo.framework.pages import Page

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

    @pytest.mark.xfail
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

    def test_print_page_and_save_as_pdf(self, driver, logger):
        """Print and save page as pdf"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")
        result = page.print_page()

        from nrobo.util.common import Common
        Common.save_as_pdf(result)

    def test_switch_to_active_element(self, driver, logger):
        """Example of switch to element"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")
        result = page.switch_to_active_element()

        logger.info(f"Result={result}")

    def test_accept_alert(self, driver, logger):
        """accept alerts"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnkJavaScriptAlert = (By.CSS_SELECTOR, "[href='/javascript_alerts']")
        page.click(*lnkJavaScriptAlert)

        btnJSAlert = (By.XPATH, "//button[text()='Click for JS Alert']")
        page.click(*btnJSAlert)

        page.wait_for_a_while(3)

    def test_working_with_frames(self, driver, logger):
        """Example of working with frames"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnkFrames = (By.CSS_SELECTOR, "[href='/frames']")
        page.click(*lnkFrames)

        lnkNestedFrames = (By.CSS_SELECTOR, "[href='/nested_frames']")
        page.click(*lnkNestedFrames)
        logger.info(f"Title of the landing page={page.title}")

        frmTop = "frame-top"
        page.frame(frmTop)  # Switch to Top level frame

        frmLeft = "frame-left"
        page.frame("frame-left")  # Switch to Left frame now
        content = page.page_source
        logger.info(f"Left Frame Content\n{content}")

        # Switch back to default content that is to main body
        page.switch_to_default_content()
        logger.info(f"default content title={page.title}")

        frmTop = "frame-top"
        page.frame(frmTop)  # Switch again to Top level frame

        frmRight = "frame-right"
        page.frame(frmRight) # Switch to Right frame now
        content = page.page_source
        logger.info(f"Right Frame Content\n{content}")

        # Switch back to default content using parent method
        page.switch_to_default_content()

    def test_switch_to_parent_frame(self, driver, logger):
        """Example of switch to parent frame"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnkFrames = (By.CSS_SELECTOR, "[href='/frames']")
        page.click(*lnkFrames)

        lnkNestedFrames = (By.CSS_SELECTOR, "[href='/nested_frames']")
        page.click(*lnkNestedFrames)
        logger.info(f"Title of the landing page={page.title}")

        frmTop = "frame-top"
        page.frame(frmTop)  # Switch to Top level frame

        frmLeft = "frame-left"
        page.frame("frame-left")  # Switch to Left frame now
        content = page.page_source
        logger.info(f"Left Frame Content\n{content}")

        # Switch back to default content that is to main body
        page.switch_to_parent_frame()
        logger.info(f"default content title={page.title}")

        frmRight = "frame-right"
        page.frame(frmRight) # Switch to Right frame now
        content = page.page_source
        logger.info(f"Right Frame Content\n{content}")

    def test_switch_to_new_window(self, driver, logger):
        """Example of switch to new window"""

        page = Page(driver, logger)

        page.get("https://the-internet.herokuapp.com/")

        # open a new window as Tab
        page.switch_to_new_window("tab")
        page.get("http://google.com")
        page.wait_for_a_while(4)
        page.close("Google")

        # open a new window as New Window
        page.switch_to_new_window("window")
        page.get("http://google.com")
        page.wait_for_a_while(4)
        page.close("Google")

        logger.info(f"title={page.title}")
        page.wait_for_a_while(3)

    def test_browser_back_action(self, driver, logger):
        """Example of browser back action"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnkFrames = (By.CSS_SELECTOR, "[href='/frames']")
        page.click(*lnkFrames)
        page.wait_for_a_while(2)

        # Perform browser back action
        page.back()
        page.wait_for_a_while(3)

    def test_browser_forward_action(self, driver, logger):
        """Example of browser forward action"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        page.get("http://google.com")

        # Perform browser back action
        page.back()
        page.wait_for_a_while(1)

        # Perform browser back action
        page.forward()
        page.wait_for_a_while(2)

    def test_browser_refresh_action(self, driver, logger):
        """Example of browser refresh action"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        # perform browser refresh action
        page.refresh()
        page.wait_for_a_while(2)

        # once again
        page.refresh()
        page.wait_for_a_while(2)