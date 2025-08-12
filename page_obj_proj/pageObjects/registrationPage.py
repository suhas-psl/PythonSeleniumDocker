
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page_obj_proj.pageObjects.basePage import BasePage
from page_obj_proj.pageObjects.registrationConfirmationPage import RegistrationConfirmationPage
from page_obj_proj.resources.registrationData import *

class RegistrationPage(BasePage):
    firstname = (By.ID, "firstName")
    lastname = (By.ID, "lastName")
    password = (By.ID, "password")
    email = (By.ID, "email")
    street = (By.XPATH, '//input[@name="street"]')
    city = (By.XPATH, '//input[@name="city"]')
    state = (By.ID, "inputState")
    zip = (By.XPATH, '//input[@name="zip"]')
    register = (By.ID, "register-btn")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def register_user(self):
        self.waits.wait_and_send_keys(self.firstname, get_registration_data("firstname"))
        self.waits.wait_and_send_keys(self.lastname, get_registration_data("lastname"))
        self.waits.wait_and_send_keys(self.password, get_registration_data("password"))
        self.waits.wait_and_send_keys(self.street, get_registration_data("street"))
        self.waits.wait_and_send_keys(self.city, get_registration_data("city"))
        dropdown = Select(self.waits.wait_for_visibility(self.state))
        dropdown.select_by_value(get_registration_data("state"))
        self.waits.wait_and_send_keys(self.zip, get_registration_data("zip"))
        self.waits.wait_and_click(self.register)

        registrationConfirmationPage = RegistrationConfirmationPage(self.driver)
        return registrationConfirmationPage

