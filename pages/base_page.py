from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException


class BasePage:

    TIMEOUT_FOR_DISAPPEARANCE = 1

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Simple element without any wait
    # def element(self, locator) -> WebElement:
    #     return self.driver.find_element(*locator)

    def element(self, locator, timeout=10) -> WebElement:
        return WebDriverWait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))

    def elements(self, locator, timeout=10) -> list:
        return WebDriverWait(self.driver, timeout=timeout).until(EC.presence_of_all_elements_located(locator))

    def is_element_not_displayed(self, locator, timeout):
        is_not_displayed = False
        try:
            WebDriverWait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            is_not_displayed = True
        return is_not_displayed

    # TODO: should Expected condition be argument or create several common methods here?
