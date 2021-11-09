from selenium import webdriver
import pytest
from utils.config_parser import CHROME_DRIVER_PATH

@pytest.fixture
def driver():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)  # TODO: make browser configurable
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
