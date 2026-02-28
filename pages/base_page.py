from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, value):
        return self.wait.until(
            EC.presence_of_element_located((by, value))
        )

    def click(self, by, value):
        self.find(by, value).click()

    def write(self, by, value, text):
        element = self.find(by, value)
        element.clear()
        element.send_keys(text)