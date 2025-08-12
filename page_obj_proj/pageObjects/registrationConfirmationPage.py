from selenium import webdriver
from selenium.webdriver.common.by import By
from page_obj_proj.pageObjects.basePage import BasePage
from page_obj_proj.pageObjects.flightSearchPage import FlightSearchPage

class RegistrationConfirmationPage(BasePage):

    register_button = (By.ID, "go-to-flights-search")


    # def __init__(self,driver):
    #     super().__init__(driver)
    #     self.driver = driver

    def confirmRegistration(self):
        self.waits.wait_and_click(self.register_button)
        flightSearchPage = FlightSearchPage(self.driver)
        return flightSearchPage
