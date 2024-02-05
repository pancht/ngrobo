from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

class TestWebSamples():

    @allure.title("Test Title for test_sample_1")
    @allure.description(
        "Test description for test_sample_1. \n\n Line 2")
    @allure.tag("Regression", "UI", "Workflow-1")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "John Doe")
    @allure.link("https://dev.example.com/", name="Website")
    @allure.issue("AUTH-123")
    @allure.testcase("TMS-456")
    def test_sample_1(self):
        driver = webdriver.Chrome()

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

    @allure.title("Test Title for test_sample_2")
    @allure.description(
        "Test description for test_sample_2. \n\n Line 2")
    @allure.tag("Regression", "UI", "Workflow-1")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "John Doe")
    @allure.link("https://dev.example.com/", name="Website")
    @allure.issue("AUTH-124")
    @allure.testcase("TMS-454")
    def test_sample_2(self):
        driver = webdriver.Chrome()

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

    @allure.title("Test Title for test_sample_3")
    @allure.description(
        "Test description for test_sample_3. \n\n Line 2")
    @allure.tag("Regression", "UI", "Workflow-2")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "John Doe")
    @allure.link("https://dev.example.com/", name="Website")
    @allure.issue("AUTH-1231")
    @allure.testcase("TMS-4561")
    def test_sample_3(self):
        driver = webdriver.Chrome()

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

    @allure.title("Test Title for test_sample_4")
    @allure.description(
        "Test description for test_sample_4. \n\n Line 2")
    @allure.tag("Sanity", "UI", "Workflow-2")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Panchdev Chauhan")
    @allure.link("https://dev.example.com/", name="Website")
    @allure.issue("AUTH-1232")
    @allure.testcase("TMS-4562")
    def test_sample_4(self):
        driver = webdriver.Chrome()

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