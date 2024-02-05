import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class TestWebSamples():

    def test_sample_1(self, driver):
        # driver = webdriver.Chrome()

        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        title = driver.title

        driver.implicitly_wait(0.5)

        text_box = driver.find_element(by=By.NAME, value="my-text")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        text_box.send_keys("Selenium")
        submit_button.click()

        message = driver.find_element(by=By.ID, value="message")
        text = message.text

        driver.quit()

    def test_sample_2(self, driver):
        # driver = webdriver.Chrome()

        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        title = driver.title

        driver.implicitly_wait(0.5)

        text_box = driver.find_element(by=By.NAME, value="my-text")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        text_box.send_keys("Selenium")
        submit_button.click()

        message = driver.find_element(by=By.ID, value="message")
        text = message.text

        driver.quit()

    def test_keep_browser_open(self):
        options = webdriver.ChromeOptions()

        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)
        driver.get('http://selenium.dev')

        driver.quit()

    def test_log_to_file(self):
        log_path = "log.log"
        service = webdriver.ChromeService(log_output=log_path)

        driver = webdriver.Chrome(service=service)

        with open(log_path, 'r') as fp:
            assert "Starting ChromeDriver" in fp.readline()

        driver.quit()
