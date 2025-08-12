import pytest
from selenium import webdriver
from page_obj_proj.utils.browserUtils import BrowserUtils
from page_obj_proj.resources.configurations import *


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run: chrome or firefox")


# THIS ALLOWS TO RUN TESTS PARALLELY IN ONLY ONE BROWSER AT A TIME.
# NEED TO FIND HOW WE CAN RUN TESTS PARALLELY ON MULTIPLE BROWSERS
@pytest.fixture()
def browserInstance(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver=webdriver.Remote(command_executor=get_selgridurl("selurl"), options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def waits(browserInstance):
    """Initialize WaitUtils for the test session."""
    return BrowserUtils(browserInstance, timeout=15)

