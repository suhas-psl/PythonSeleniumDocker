from selenium.webdriver.common.by import By
from page_obj_proj.utils.browserUtils import BrowserUtils

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.waits = BrowserUtils(driver, timeout=15)