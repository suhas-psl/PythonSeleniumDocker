import pytest
from selenium import webdriver
from page_obj_proj.pageObjects.registrationPage import RegistrationPage
from page_obj_proj.resources.configurations import *

def test_registration1(browserInstance):
    driver = browserInstance
    url = get_url("url1")
    driver.get(url)
    registrationPage = RegistrationPage(driver)
    registrationConfirmationPage = registrationPage.register_user()
    flightSearchPage = registrationConfirmationPage.confirmRegistration()

    selectFlightPage = flightSearchPage.searchFlight()

    flightConfirmationPage = selectFlightPage.flightSelect()
    flightConfirmationPage.getTotalPrice()

def test_registration2(browserInstance):
    driver = browserInstance
    url = get_url("url1")
    driver.get(url)
    registrationPage = RegistrationPage(driver)
    registrationConfirmationPage = registrationPage.register_user()
    flightSearchPage = registrationConfirmationPage.confirmRegistration()

    selectFlightPage = flightSearchPage.searchFlight()

    flightConfirmationPage = selectFlightPage.flightSelect()
    flightConfirmationPage.getTotalPrice()




