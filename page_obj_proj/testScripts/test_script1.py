import pytest
from selenium import webdriver
from page_obj_proj.pageObjects.registrationPage import RegistrationPage
from page_obj_proj.resources.configurations import *
from page_obj_proj.utils.log_utils import setup_logger


logger = setup_logger(__name__)

def test_registration1(driver_instance):
    driver = driver_instance
    url = get_url("url1")
    driver.get(url)
    logger.info("Create Registration Page object")
    registrationPage = RegistrationPage(driver)
    registrationConfirmationPage = registrationPage.register_user()
    logger.info("Create Flight Search Page object")
    flightSearchPage = registrationConfirmationPage.confirmRegistration()
    logger.info("Create Select Flight  Page object")
    selectFlightPage = flightSearchPage.searchFlight()
    logger.info("Create Flight Confirmation  Page object")
    flightConfirmationPage = selectFlightPage.flightSelect()
    flightConfirmationPage.getTotalPrice()

def test_registration2(driver_instance):
    driver = driver_instance
    url = get_url("url1")
    driver.get(url)
    logger.info("Create Registration Page object")
    registrationPage = RegistrationPage(driver)
    registrationConfirmationPage = registrationPage.register_user()
    logger.info("Create Flight Search Page object")
    flightSearchPage = registrationConfirmationPage.confirmRegistration()
    logger.info("Create Select Flight  Page object")
    selectFlightPage = flightSearchPage.searchFlight()
    logger.info("Create Flight Confirmation  Page object")
    flightConfirmationPage = selectFlightPage.flightSelect()
    flightConfirmationPage.getTotalPrice()




