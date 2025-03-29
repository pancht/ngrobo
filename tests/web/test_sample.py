import pytest
from selenium.webdriver.common.by import By

from nrobo.framework.pages import Page


class TestWebSamples:

    @pytest.mark.regression
    def test_pass_url_username_password_from_commandline(
        self, driver, logger, url, username, password
    ):
        driver.get(url)
        logger.info(f"URL={url}, Username={username} and Password={password}")

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip
    def test_sample_1(self, driver, logger):
        """Verify simple test - 1"""
        # driver = webdriver.Chrome()

        logger.info("Open url")
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        driver.implicitly_wait(0.5)

        logger.info("Click on submit button. ")
        text_box = driver.find_element(by=By.NAME, value="my-text")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        text_box.send_keys("Selenium")
        submit_button.click()

    @pytest.mark.sanity
    # @pytest.mark.skip
    def test_sample_2(self, driver, logger):
        """Verify simple test - 2"""
        # driver = webdriver.Chrome()

        logger.info("Open url")
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        driver.implicitly_wait(0.5)

        logger.info("Click on submit button.")
        text_box = driver.find_element(by=By.NAME, value="my-text")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        logger.info("Type selenium")
        text_box.send_keys("Selenium")

        logger.info("Click submit button")
        submit_button.click()

        raise Exception(
            "Forcefully failed test for demonstration of screencapture feature!"
        )

    @pytest.mark.sanity
    # @pytest.mark.skip
    def test_sample_3(self, driver, logger):
        """Verify simple test - 3"""
        # driver = webdriver.Chrome()

        logger.info("Open url")
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        driver.implicitly_wait(0.5)

        logger.info("Click on submit button.")
        text_box = driver.find_element(by=By.NAME, value="my-text")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        logger.info("Type selenium")
        text_box.send_keys("Selenium")

        logger.info("Click submit button")
        submit_button.click()

    def test_take_full_page_screenshot(self, driver, logger):
        page = Page(driver, logger)

        page.get("https://namasteydigitalindia.com/")
