from selenium.webdriver.common.by import By
from page_obj_proj.utils.wait_utils import WaitUtils

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.waits = WaitUtils(driver, timeout=15)