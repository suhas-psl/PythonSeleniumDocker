from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WaitUtils:

    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    # def get_title(self):
    #     return self.driver.title

    def wait_for_visibility(self, locator):
        """Wait for element to be visible."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"[ERROR] Element not visible: {locator}")
            return None

    def wait_for_clickable(self, locator):
        """Wait for element to be clickable."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            print(f"[ERROR] Element not clickable: {locator}")
            return None

    def wait_for_presence(self, locator):
        """Wait for element to be present in DOM (not necessarily visible)."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"[ERROR] Element not present: {locator}")
            return None

    def wait_for_invisibility(self, locator):
        """Wait until element is invisible or not present."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"[ERROR] Element did not disappear: {locator}")
            return False

    def wait_for_alert(self):
        """Wait until alert appears."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
        except TimeoutException:
            print("[ERROR] Alert did not appear")
            return None

    def wait_and_click(self, locator):
        """Wait for element to be clickable and click it."""
        element = self.wait_for_clickable(locator)
        if element:
            element.click()

    def wait_and_send_keys(self, locator, text):
        """Wait for element to be visible and send keys."""
        element = self.wait_for_visibility(locator)
        if element:
            element.clear()
            element.send_keys(text)