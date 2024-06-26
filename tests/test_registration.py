import time
import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants


class TestStellarBurgersRegistration:

    @staticmethod
    def login_generation():
        login = f"dmitriy_karpov_07_{random.randint(1000, 9999)}@yandex.ru"

        return login

    def test_registration_positive_input_successful(self, driver):

        driver.find_element(*Locators.ACCOUNT_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.REGISTER_BUTTON_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        login = self.login_generation
        driver.find_element(*Locators.NAME_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.NAME_EMAIL).send_keys(login)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.AUTH_LOGIN_ELEMENT))
        time.sleep(1)
        driver.find_element(*Locators.NAME_EMAIL).send_keys(login)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_ELEMENT))
        driver.find_element(*Locators.TITLE_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ELEMENT_PERSONAL_ACCOUNT))
        user_name = driver.find_element(*Locators.FIELD_USER_NAME).get_attribute("value")
        user_email = driver.find_element(*Locators.FIELD_USER_EMAIL).get_attribute("value")
        user_password = driver.find_element(*Locators.FIELD_USER_PASSWORD).get_attribute("value")

        assert user_name == Constants.NAME
        assert user_email == login
        assert len(user_password) != 0

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.AUTH_LOGIN_ELEMENT))

    def test_enter_incorrect_pass_show_error(self, driver):
        driver.find_element(*Locators.ACCOUNT_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.REGISTER_BUTTON_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.NAME_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.NAME_EMAIL).send_keys(Constants.LOGIN)
        driver.find_element(*Locators.PASSWORD).send_keys('12345')
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        error = driver.find_element(*Locators.POP_UP_TEXT_ERROR).text

        assert error == 'Некорректный пароль'
