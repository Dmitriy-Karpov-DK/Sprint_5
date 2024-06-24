import random

import pytest
from selenium import webdriver

from constants import Constants


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)
    yield driver
    driver.quit()


@pytest.fixture
def login_generation():
    login = f"dmitriy_karpov_07_{random.randint(1000, 9999)}@yandex.ru"

    return login
