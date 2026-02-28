from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverFactory:

    @staticmethod
    def create_driver(browser="chrome", headless=False):

        if browser.lower() == "chrome":
            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-infobars")

            driver = webdriver.Chrome(options=options)

        elif browser.lower() == "firefox":
            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Browser '{browser}' no soportado")

        driver.implicitly_wait(5)
        return driver