from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page_obj_proj.pageObjects.flightsConfirmationPage import FlightsConfirmationPage
from page_obj_proj.pageObjects.basePage import BasePage

class SelectFlightPage(BasePage):
    departure = (By.ID, "dep-emirates-first")
    arrival = (By.ID, "arr-ba-business")
    confirm_button = (By.ID, "confirm-flights")

    def flightSelect(self):
        self.waits.wait_and_click(self.departure)
        self.waits.wait_and_click(self.arrival)
        self.waits.wait_and_click(self.confirm_button)

        flightConfirmationPage = FlightsConfirmationPage(self.driver)
        return flightConfirmationPage