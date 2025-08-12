
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_obj_proj.pageObjects.basePage import BasePage

class FlightsConfirmationPage(BasePage):

    totalPrice = (By.XPATH, "//form[@class='row g-3']//div[contains(text(),'Total Price')]/following-sibling::div/p")

    def getTotalPrice(self):
        print("##%$%$%$%#$%$@%$#@%@%%$@$%@##@$#@%#@%!%$!#$!#$#!#$#")
        print(self.waits.wait_for_visibility(self.totalPrice).text)
        print("##%$%$%$%#$%$@%$#@%@%%$@$%@##@$#@%#@%!%$!#$!#$#!#$#")
