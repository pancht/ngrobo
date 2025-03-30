"""nrobo methods tests."""

import pytest
from selenium.webdriver.common.by import By
from nrobo.framework.pages import Page


class TestNRoBoSeleniumWrapperMethods:  # pylint: disable=R0904
    """Class holding tests for testing selenium wrapper methods."""

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

        lnk_multiple_window = (By.CSS_SELECTOR, "a[href='/windows']")
        page.click(*lnk_multiple_window)

        lnk_click_here = (By.CSS_SELECTOR, "a[href='/windows/new']")
        page.click(*lnk_click_here)
        another_window = "New Window"

        # close the another window
        page.close(another_window)

        page.wait_for_a_while(3)

    @pytest.mark.xfail
    def test_quit_all_windows(self, driver, logger):
        """Example of quiting all open windows"""

        page = Page(driver, logger)

        page.get("https://the-internet.herokuapp.com/")

        lnk_multiple_window = (By.CSS_SELECTOR, "a[href='/windows']")
        page.click(*lnk_multiple_window)

        lnk_click_here = (By.CSS_SELECTOR, "a[href='/windows/new']")
        page.click(*lnk_click_here)

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

        lnk_multiple_window = (By.CSS_SELECTOR, "a[href='/windows']")
        page.click(*lnk_multiple_window)

        lnk_click_here = (By.CSS_SELECTOR, "a[href='/windows/new']")
        page.click(*lnk_click_here)

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

        from nrobo.util.common import Common  # pylint: disable=C0415

        Common.save_as_pdf(result)

    def test_switch_to_active_element(self, driver, logger):
        """Example of switch to element"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")
        result = page.switch_to_active_element()

        logger.info(f"Result={result}")

    @pytest.mark.skip(reason="This test fails in Headless mode")
    def test_accept_alert(self, driver, logger):
        """accept alerts"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_java_script_alert = (By.CSS_SELECTOR, "[href='/javascript_alerts']")
        page.click(*lnk_java_script_alert)

        btn_js_alert = (By.XPATH, "//button[text()='Click for JS Alert']")
        page.click(*btn_js_alert)
        page.accept_alert()

        page.wait_for_a_while(3)

    def test_working_with_frames(self, driver, logger):
        """Example of working with frames"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_frames = (By.CSS_SELECTOR, "[href='/frames']")
        page.click(*lnk_frames)

        lnk_nested_frames = (By.CSS_SELECTOR, "[href='/nested_frames']")
        page.click(*lnk_nested_frames)
        logger.info(f"Title of the landing page={page.title}")

        frm_top = "frame-top"
        page.frame(frm_top)  # Switch to Top level frame

        page.frame("frame-left")  # Switch to Left frame now
        content = page.page_source
        logger.info(f"Left Frame Content\n{content}")

        # Switch back to default content that is to main body
        page.switch_to_default_content()
        logger.info(f"default content title={page.title}")

        frm_top = "frame-top"
        page.frame(frm_top)  # Switch again to Top level frame

        frm_right = "frame-right"
        page.frame(frm_right)  # Switch to Right frame now
        content = page.page_source
        logger.info(f"Right Frame Content\n{content}")

        # Switch back to default content using parent method
        page.switch_to_default_content()

    def test_switch_to_parent_frame(self, driver, logger):
        """Example of switch to parent frame"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_frames = (By.CSS_SELECTOR, "[href='/frames']")
        page.click(*lnk_frames)

        lnk_nested_frames = (By.CSS_SELECTOR, "[href='/nested_frames']")
        page.click(*lnk_nested_frames)
        logger.info(f"Title of the landing page={page.title}")

        frm_top = "frame-top"
        page.frame(frm_top)  # Switch to Top level frame

        page.frame("frame-left")  # Switch to Left frame now
        content = page.page_source
        logger.info(f"Left Frame Content\n{content}")

        # Switch back to default content that is to main body
        page.switch_to_parent_frame()
        logger.info(f"default content title={page.title}")

        frm_right = "frame-right"
        page.frame(frm_right)  # Switch to Right frame now
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
        page.wait_for_a_while(4)

        # open a new window as New Window
        page.switch_to_new_window("window")
        page.wait_for_a_while(5)
        page.get("http://google.com")
        page.wait_for_a_while(4)
        page.close("Google")

        logger.info(f"title={page.title}")
        page.wait_for_a_while(3)

    def test_browser_back_action(self, driver, logger):
        """Example of browser back action"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_frames = (By.CSS_SELECTOR, "[href='/frames']")
        page.click(*lnk_frames)
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

    def test_get_all_cookies(self, driver, logger):
        """Example of working with cookies

        get_cookies()

        get_cookie(name)

        delete_cookie(name)

        delete_all_cookies()

        add_cookie(cookies:{})"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        cookies = page.get_cookies()

        logger.info(f"All cookies= {cookies}")

    def test_add_cookie(self, driver, logger):
        """Example of adding a cookie"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        custom_cookies = {"name": "company", "value": "ndi", "path": "/"}
        page.add_cookie(custom_cookies)

        logger.info(f"updated cookies= {page.get_cookies()}")

        logger.info(f"Cookie value = {page.get_cookie('company')}")

    def test_delete_cookie(self, driver, logger):
        """Example of delete a cookie"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        logger.info(f"All cookies ==> {page.get_cookies()}")

        page.delete_cookie("optimizelyEndUserId")

        logger.info(f"All cookies ==> {page.get_cookies()}")

    def test_delete_all_cookiee(self, driver, logger):
        """Example of delete all cookies"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        logger.info(f"All cookies ==> {page.get_cookies()}")

        page.delete_all_cookies()

        logger.info(f"All cookies after deletion ==> {page.get_cookies()}")

    @pytest.mark.xfail
    def test_implicitly_wait(self, driver, logger):
        """set implicitly wait"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        page.implicitly_wait(10)

        lnk_arbitrary_link = (By.ID, "xxxhhhssjjsjjs")
        page.find_element(*lnk_arbitrary_link)

    def test_set_script_timeout(self, driver, logger):
        """set script timeout"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        page.set_script_timeout(30)

    def test_set_page_load_timeout(self, driver, logger):
        """set page load timeout"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        page.set_page_load_timeout(30)

    def test_get_all_timeouts(self, driver, logger):
        """get all timeouts"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        logger.info(f"Pageload timeout ===> {page.timeouts.page_load}")
        logger.info(f"Script timeout ===> {page.timeouts.script}")
        logger.info(f"Implicit timeout ===> {page.timeouts.implicit_wait}")

    def test_set_all_timeouts(self, driver, logger):
        """set all timeouts"""

        page = Page(driver, logger)
        page.timeouts.page_load = 1
        page.timeouts.script = 2
        page.timeouts.implicit_wait = 3

        page.get("https://the-internet.herokuapp.com/")

        logger.info(f"Page load timeout ===> {page.timeouts.page_load}")
        logger.info(f"Script timeout ===> {page.timeouts.script}")
        logger.info(f"Implicit timeout ===> {page.timeouts.implicit_wait}")

    def test_findelement(self, driver, logger):
        """example of findelement"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_ab_testing = (By.CSS_SELECTOR, '[href="/abtest"]')
        page.find_element(*lnk_ab_testing).click()
        page.wait_for_a_while(5)

    def test_findelementssss(self, driver, logger):
        """example of findelementsss"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        all_links = (By.CSS_SELECTOR, "ul li a")
        elements = page.find_elements(*all_links)
        logger.info(f"Count of all links = {len(elements)}")
        page.wait_for_a_while(2)

        # click on 2nd link
        elements[1].click()
        page.wait_for_a_while(3)

    def test_capabilities(self, driver, logger):
        """example of capabilities"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        logger.info(f"Capabilities ===> {page.capabilities}")

    def test_get_screenshot_as_file(self, driver, logger):
        """example of get_screenshot_as_file"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        page.get_screenshot_as_file("downloads/screenshot.png")

    def test_get_screenshot_as_png(self, driver, logger):
        """example of get_screenshot_as_png"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        bytes = page.get_screenshot_as_png()  # pylint: disable=W0622

        from nrobo.util.common import Common  # pylint: disable=C0415

        Common.save_bytes_to_file(bytes, "downloads/screenshot_as_png.png")

    def test_get_screenshot_as_base64(self, driver, logger):
        """example of get_screenshot_as_base64"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        base64string = page.get_screenshot_as_base64()

        from nrobo.util.common import Common  # pylint: disable=C0415

        Common.save_base64string(
            base64string, "downloads/screenshot_as_base64string.png"
        )

    def test_set_window_size(self, driver, logger):
        """example of get_screenshot_as_base64"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        page.set_window_size(800, 400)
        page.wait_for_a_while(2)

        page.set_window_size(1200, 600)

    def test_get_window_size(self, driver, logger):
        """example of get_window_size"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        logger.info(f"Current window size = {page.get_window_size()}")

    def test_set_window_position(self, driver, logger):
        """example of set_window_position"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        page.set_window_position(200, 300)
        page.wait_for_a_while(3)

    def test_set_window_rect(self, driver, logger):
        """example of set_window_rect"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        page.set_window_rect(200, 300, 600, 100)
        page.wait_for_a_while(3)

    def test_log_types(self, driver, logger):
        """example of log_types"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        logger.info(f"Orientation = {page.log_types}")

    def test_get_log(self, driver, logger):
        """example of get_log"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        logger.info(f"Get Driver Log = {page.get_log('driver')}")
        logger.info(f"Get Driver Log = {page.get_log('browser')}")
