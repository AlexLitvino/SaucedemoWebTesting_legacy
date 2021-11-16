from selenium import webdriver
import pytest
from utils.config_parser import BROWSER_NAME


@pytest.fixture
def driver():
    if BROWSER_NAME == "chrome":
        driver = webdriver.Chrome()
    elif BROWSER_NAME == "firefox":
        driver = webdriver.Firefox()
    elif BROWSER_NAME == "edge":
        driver = webdriver.Edge()
    else:
        raise UnsupportedBrowserException(f"Browser '{BROWSER_NAME}' is not supported by framework. "
                                          f"Please add it if you need this browser.")
    # TODO: add other browsers if required
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


class UnsupportedBrowserException(Exception):
    pass
