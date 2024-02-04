from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWebSamples():

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