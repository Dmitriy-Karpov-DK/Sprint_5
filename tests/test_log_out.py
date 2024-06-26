from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants


class TestStellarBurgersLogOut:

    def test_log_out_using_exit_button_in_pers_acc_succesful(self, driver):
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
            expected_conditions.visibility_of_element_located(Locators.INPUT_ELEMENT))
        driver.find_element(*Locators.EXIT_BUTTON_IN_PERS_ACC).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        assert driver.current_url == Constants.URL_LOGIN
