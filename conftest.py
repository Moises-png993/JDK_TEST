import pytest
from utils.driver_factory import DriverFactory


@pytest.fixture
def driver():
    driver = DriverFactory.create_driver(
        browser="chrome",
        headless=False
    )
    driver.get("https://prueba-jd-022026.dev-jdoutstanding.com/") 
    yield driver
    driver.quit()