from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestStellarBurgersConstructorSection:

    def test_constructor_section_go_to_sauces_section(self, driver):

        driver.find_element(*Locators.GO_TO_SAUCES).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.TITLE_SAUCES))

    def test_constructor_section_go_to_bread_section(self, driver):

        driver.find_element(*Locators.GO_TO_SAUCES).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.TITLE_SAUCES))
        driver.find_element(*Locators.GO_TO_BREAD).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.TITLE_BREAD))

    def test_constructor_section_go_to_filling_section(self, driver):

        driver.find_element(*Locators.GO_TO_FILLING).click()

        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.TITLE_FILLING))
