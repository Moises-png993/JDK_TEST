from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "login_username")
    PASSWORD = (By.ID, "login_password")  
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.write(*self.USERNAME, username)
        self.write(*self.PASSWORD, password)
        self.click(*self.LOGIN_BUTTON)