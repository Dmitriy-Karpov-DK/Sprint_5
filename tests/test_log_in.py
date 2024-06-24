from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants


class TestStellarBurgersLogIn:

    def test_log_in_button_acc_log_in_successful_acc(self, driver):

        driver.find_element(*Locators.ACCOUNT_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.NAME_EMAIL).send_keys(Constants.LOGIN)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_ELEMENT))

        driver.find_element(*Locators.TITLE_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ELEMENT_PERSONAL_ACCOUNT))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.AUTH_LOGIN_ELEMENT))

    def test_log_in_button_pers_acc_successful_acc(self, driver):

        driver.find_element(*Locators.TITLE_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.NAME_EMAIL).send_keys(Constants.LOGIN)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_ELEMENT))

        driver.find_element(*Locators.TITLE_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ELEMENT_PERSONAL_ACCOUNT))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.AUTH_LOGIN_ELEMENT))

    def test_log_in_button_registration_form_successful_acc(self, driver):

        driver.find_element(*Locators.TITLE_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.REGISTER_BUTTON_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.LOGIN_BUTTON_IN_REGISTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.NAME_EMAIL).send_keys(Constants.LOGIN)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_ELEMENT))

        driver.find_element(*Locators.TITLE_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.ELEMENT_PERSONAL_ACCOUNT))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.AUTH_LOGIN_ELEMENT))

    def test_log_in_button_password_recovery_form_successful_acc(self, driver):

        driver.find_element(*Locators.TITLE_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.RECOVER_PASSWORD_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.LOGIN_BUTTON_IN_RECOVER_PASSWORD).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.NAME_EMAIL).send_keys(Constants.LOGIN)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_ELEMENT))

        driver.find_element(*Locators.TITLE_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.ELEMENT_PERSONAL_ACCOUNT))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.AUTH_LOGIN_ELEMENT))
