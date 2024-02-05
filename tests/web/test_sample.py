import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class TestWebSamples():

    def test_sample_1(self, driver, logger):
        # driver = webdriver.Chrome()

        logger.info("Open url")
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        title = driver.title

        driver.implicitly_wait(0.5)

        logger.info("Click on submit button.")
        text_box = driver.find_element(by=By.NAME, value="my-text")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        text_box.send_keys("Selenium")
        submit_button.click()

        message = driver.find_element(by=By.ID, value="message")
        text = message.text

        logger.info("Quit browser")
        driver.quit()

    def test_sample_2(self, driver, logger):
        # driver = webdriver.Chrome()

        logger.info("Open url")
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        title = driver.title

        driver.implicitly_wait(0.5)

        logger.info("Click on submit button.")
        text_box = driver.find_element(by=By.NAME, value="my-text")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        text_box.send_keys("Selenium")
        submit_button.click()

        message = driver.find_element(by=By.ID, value="message")
        text = message.text

        logger.info("Quit browser")
        driver.quit()
