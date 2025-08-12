
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from page_obj_proj.pageObjects.basePage import BasePage

from page_obj_proj.pageObjects.selectFlightPage import SelectFlightPage


class FlightSearchPage(BasePage):
    oneWay = (By.ID, "oneway")
    passengers = (By.ID, "passengers")
    departing = (By.ID, "depart-from")
    arrivin = (By.ID, "arrive-in")
    serviceclass = (By.ID, "service-class3")
    search_button = (By.ID, "search-flights")

    # def __init__(self,driver):
    #     super().__init__(driver)
    #     self.driver = driver

    def searchFlight(self):
        self.waits.wait_and_click(self.oneWay)
        dropdown1 = Select(self.waits.wait_for_visibility(self.passengers))
        dropdown1.select_by_value("2")
        dropdown2 = Select(self.waits.wait_for_visibility(self.departing))
        dropdown2.select_by_value("Frankfurt")
        dropdown3 = Select(self.waits.wait_for_visibility(self.arrivin))
        dropdown3.select_by_value("Paris")
        self.waits.wait_and_click(self.serviceclass)
        self.waits.wait_and_click(self.search_button)

        selectFlightPage = SelectFlightPage(self.driver)
        return selectFlightPage
