"""Element wrapper methods."""

from selenium.webdriver.common.by import By

from nrobo.framework.pages import Page


class TestWebElementWrapperMethods:
    """Class holding web element wrapper method tests."""

    def test_get_tag_name_of_element(self, driver, logger):
        """example of get tag name of element"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_ab_test = (By.CSS_SELECTOR, "[href='/abtest']")
        logger.info(f"Tag name => {page.find_element(*lnk_ab_test).tag_name}")
        logger.info(f"Tag name => {page.tag_name(*lnk_ab_test)}")

    def test_get_text_of_element(self, driver, logger):
        """example of text of element"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_ab_test = (By.CSS_SELECTOR, "[href='/abtest']")
        logger.info(f"Link Text => {page.find_element(*lnk_ab_test).text}")
        logger.info(f"Link Text => {page.text(*lnk_ab_test)}")

    def test_click_method(self, driver, logger):
        """example of click method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_ab_test = (By.CSS_SELECTOR, "[href='/abtest']")
        page.find_element(*lnk_ab_test).click()
        page.wait_for_a_while(2)

        page.back()
        page.wait_for_a_while(2)
        page.click(*lnk_ab_test)
        page.wait_for_a_while(2)

    def test_click_and_wait_method(self, driver, logger):
        """example of click and wait method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_ab_test = (By.CSS_SELECTOR, "[href='/abtest']")
        page.click_and_wait(*lnk_ab_test, 5)

    def test_element_to_be_clickable(self, driver, logger):
        """example of element_to_be_clickable method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_ab_test = (By.CSS_SELECTOR, "[href='/abtest']")
        page.element_to_be_clickable(*lnk_ab_test)

    def test_submit(self, driver, logger):
        """example of submit form method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        page.click(*lnk_login)

        txt_username = (By.NAME, "username")
        page.send_keys(*txt_username, "tomsmith")

        txt_password = (By.NAME, "password")
        page.send_keys(*txt_password, "SuperSecretPassword!")

        btn_login = (By.CSS_SELECTOR, "button.radius")
        page.submit(*btn_login)

        page.wait_for_a_while(4)

    def test_is_displayed(self, driver, logger):
        """example of is_displayed method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        logger.info(f"Is login link displayed? A. {page.is_displayed(*lnk_login)}")

    def test_location_once_scrolled_into_view(self, driver, logger):
        """example of location_once_scrolled_into_view method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")
        page.wait_for_a_while(2)

        lnk_wysiwyg = (By.CSS_SELECTOR, "[href='/tinymce']")
        page.location_once_scrolled_into_view(*lnk_wysiwyg)

        page.wait_for_a_while(2)

    def test_size(self, driver, logger):
        """example of size method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        logger.info(f"Size of element = {page.size(*lnk_login)}")

    def test_value_of_css_property(self, driver, logger):
        """example of value_of_css_property method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        logger.info(
            f"Size of element = {page.value_of_css_property('color', *lnk_login)}"
        )

    def test_location_(self, driver, logger):
        """example of location method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        logger.info(f"location of element = {page.location(*lnk_login)}")

    def test_rect_(self, driver, logger):
        """example of rect method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        logger.info(f"rect of element = {page.rect(*lnk_login)}")

    def test_aria_role(self, driver, logger):
        """example of aria_role method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        logger.info(f"aria_role of element = {page.aria_role(*lnk_login)}")

    def test_accessible_name(self, driver, logger):
        """example of accessible_name method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        logger.info(f"accessible_name of element = {page.accessible_name(*lnk_login)}")

    def test_screenshot_as_base64(self, driver, logger):
        """example of screenshot_as_base64 method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        screenshot = page.screenshot_as_base64(*lnk_login)

        from nrobo.util.common import Common  # pylint: disable=C0415

        Common.save_base64string(screenshot, "downloads/element_screenshot.png")

    def test_screenshot_as_png(self, driver, logger):
        """example of screenshot_as_png method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        screenshot_as_binary_data = page.screenshot_as_png(*lnk_login)

        from nrobo.util.common import Common  # pylint: disable=C0415

        Common.save_bytes_to_file(
            screenshot_as_binary_data, "downloads/element_screenshot_as_binary.png"
        )

    def test_screenshot_as_file(self, driver, logger):
        """example of screenshot method"""

        page = Page(driver, logger)
        page.get("https://the-internet.herokuapp.com/")

        lnk_login = (By.CSS_SELECTOR, "[href='/login']")
        page.screenshot("downloads/element_screenshot_as_file.png", *lnk_login)

    def test_uploads(self, driver, logger):
        """Example of file upload"""

        page = Page(driver, logger)
        page.maximize_window()
        page.get("https://the-internet.herokuapp.com/upload")

        from nrobo import NroboPaths  # pylint: disable=C0415

        upload_file = (
            NroboPaths.NROBO
            / NroboPaths.FRAMEWORK
            / NroboPaths.TEST_DATA
            / "nRoBo-Logo.png"
        )

        file_input = (By.CSS_SELECTOR, "input[type='file']")
        btn_upload = (By.ID, "file-submit")

        page.file_upload(*file_input, upload_file, *btn_upload)

        file_name_element = page.find_element(By.ID, "uploaded-files")
        file_name = file_name_element.text

        assert file_name == "nRoBo-Logo.png"
