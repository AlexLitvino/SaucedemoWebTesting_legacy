from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from utils.config_parser import BASE_URL
from allure_commons._allure import step


class LoginPage(BasePage):

    # Locators of Login page elements
    LOGIN_LOGO_IMAGE = (By.CLASS_NAME, "login_logo")
    USERNAME_INPUT_FIELD = (By.ID, "user-name")
    PASSWORD_INPUT_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    BOT_IMAGE = (By.CLASS_NAME, "bot_column")
    USERNAME_ERROR_INDICATOR = (By.XPATH, '//input[@id="user-name"]/following-sibling::*[name()="svg"]')
    PASSWORD_ERROR_INDICATOR = (By.XPATH, '//input[@id="password"]/following-sibling::*[name()="svg"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@class="error-message-container error"]/h3')
    CLOSE_ERROR_BUTTON = (By.CLASS_NAME, "error-button")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def login_logo_image(self):
        return self.element(LoginPage.LOGIN_LOGO_IMAGE)

    @property
    def username_input_field(self):
        return self.element(LoginPage.USERNAME_INPUT_FIELD)

    @property
    def password_input_field(self):
        return self.element(LoginPage.PASSWORD_INPUT_FIELD)

    @property
    def login_button(self):
        return self.element(LoginPage.LOGIN_BUTTON)

    @property
    def bot_image(self):
        return self.element(LoginPage.BOT_IMAGE)

    @property
    def username_error_indicator(self):
        return self.element(LoginPage.USERNAME_ERROR_INDICATOR)

    @property
    def password_error_indicator(self):
        return self.element(LoginPage.PASSWORD_ERROR_INDICATOR)

    @property
    def error_message(self):
        return self.element(LoginPage.ERROR_MESSAGE)

    @property
    def close_error_button(self):
        return self.element(LoginPage.CLOSE_ERROR_BUTTON)

    def navigate(self):
        with step(f"Navigate to '{BASE_URL}'."):
            self.driver.get(BASE_URL)

    def enter_username(self, username):
        with step(f"Enter '{username}' to username text field."):
            self.username_input_field.send_keys(username)

    def enter_password(self, password):
        with step(f"Enter '{password}' to password text field."):
            self.password_input_field.send_keys(password)

    def click_login_button(self):
        with step("Click Login button."):
            self.login_button.click()

    def fill_login_form_and_click_login_button(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self

    def perform_successful_login(self, username, password):
        self.fill_login_form_and_click_login_button(username, password)
        return InventoryPage(self.driver)

    def perform_unsuccessful_login(self, username, password):
        self.fill_login_form_and_click_login_button(username, password)
        return self

    def is_error_message_not_displayed(self):
        return self.is_element_not_displayed(self.ERROR_MESSAGE, timeout=1)

    def is_username_error_indicator_not_displayed(self):
        return self.is_element_not_displayed(self.USERNAME_ERROR_INDICATOR, timeout=1)

    def is_password_error_indicator_not_displayed(self):
        return self.is_element_not_displayed(self.PASSWORD_ERROR_INDICATOR, timeout=1)

    def is_page_displayed(self):
        return self.login_button.is_displayed()
