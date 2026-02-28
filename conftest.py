import pytest
import os
import time
from utils.driver_factory import DriverFactory

SCREENSHOTS_DIR = "reports/screenshots"

@pytest.fixture
def driver():
    driver = DriverFactory.create_driver(
        browser="chrome",
        headless=False
    )
    driver.get("https://prueba-jd-022026.dev-jdoutstanding.com/")
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace(" ", "_")
            screenshot_path = f"{SCREENSHOTS_DIR}/{test_name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)

            extras = getattr(report, "extras", [])
            try:
                import pytest_html
                extras.append(pytest_html.extras.image(screenshot_path))
                report.extras = extras
            except Exception:
                pass