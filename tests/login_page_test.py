import pytest
from pages.login_page import LoginPage
from utils.config_parser import STANDARD_USER_USERNAME, STANDARD_USER_PASSWORD, STANDARD_USER_INCORRECT_PASSWORD, \
    NON_EXISTING_USER, NON_EXISTING_USER_PASSWORD, LOCKED_OUT_USER_USERNAME, LOCKED_OUT_USER_PASSWORD
from resources import Resources


@pytest.fixture(scope="function")
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    return login_page


def test_login_form_present(login_page):
    assert login_page.login_logo_image.is_displayed()
    assert login_page.username_input_field.is_displayed()
    assert login_page.password_input_field.is_displayed()
    assert login_page.login_button.is_displayed()
    assert login_page.bot_image.is_displayed()
    assert login_page.is_error_message_not_displayed()
    assert login_page.is_username_error_indicator_not_displayed()
    assert login_page.is_password_error_indicator_not_displayed()


def test_successful_login(login_page):
    inventory_page = login_page.perform_successful_login(STANDARD_USER_USERNAME, STANDARD_USER_PASSWORD)
    assert inventory_page.is_page_displayed()


@pytest.mark.xfail
def test_login_page_text(login_page):
    assert login_page.username_input_field.get_attribute("placeholder") == Resources.LoginPage.USERNAME_FIELD_PLACEHOLDER
    assert login_page.password_input_field.get_attribute("placeholder") == Resources.LoginPage.PASSWORD_FIELD_PLACEHOLDER
    assert login_page.login_button.get_property("value") == "LOGIN"  # TODO: this fails as additional CSS property text-transform is applied


def test_login_with_incorrect_password(login_page):
    login_page.perform_unsuccessful_login(username=STANDARD_USER_USERNAME, password=STANDARD_USER_INCORRECT_PASSWORD)
    assert login_page.username_error_indicator.is_displayed()
    assert login_page.password_error_indicator.is_displayed()
    assert login_page.error_message.is_displayed()
    assert login_page.error_message.text == Resources.LoginPage.NON_EXISTING_USER_ERROR_TEXT
    assert login_page.close_error_button.is_displayed()
    login_page.close_error_button.click()
    assert login_page.is_error_message_not_displayed()
    assert login_page.is_username_error_indicator_not_displayed()
    assert login_page.is_password_error_indicator_not_displayed()


def test_login_as_non_existing_user(login_page):
    login_page.perform_unsuccessful_login(NON_EXISTING_USER, NON_EXISTING_USER_PASSWORD)
    assert login_page.username_error_indicator.is_displayed()
    assert login_page.password_error_indicator.is_displayed()
    assert login_page.error_message.is_displayed()
    assert login_page.error_message.text == Resources.LoginPage.NON_EXISTING_USER_ERROR_TEXT
    assert login_page.close_error_button.is_displayed()
    login_page.close_error_button.click()
    assert login_page.is_error_message_not_displayed()
    assert login_page.is_username_error_indicator_not_displayed()
    assert login_page.is_password_error_indicator_not_displayed()


def test_login_as_locked_out_user(login_page):
    login_page.perform_unsuccessful_login(LOCKED_OUT_USER_USERNAME, LOCKED_OUT_USER_PASSWORD)
    assert login_page.username_error_indicator.is_displayed()
    assert login_page.password_error_indicator.is_displayed()
    assert login_page.error_message.is_displayed()
    assert login_page.error_message.text == Resources.LoginPage.LOCKED_OUT_USER_ERROR_TEXT
    assert login_page.close_error_button.is_displayed()
    login_page.close_error_button.click()
    assert login_page.is_error_message_not_displayed()
    assert login_page.is_username_error_indicator_not_displayed()
    assert login_page.is_password_error_indicator_not_displayed()


def test_login_with_no_username(login_page):
    login_page.perform_unsuccessful_login(username="", password=STANDARD_USER_PASSWORD)
    assert login_page.username_error_indicator.is_displayed()
    assert login_page.password_error_indicator.is_displayed()
    assert login_page.error_message.is_displayed()
    assert login_page.error_message.text == Resources.LoginPage.MISSING_USERNAME_ERROR_TEXT
    assert login_page.close_error_button.is_displayed()
    login_page.close_error_button.click()
    assert login_page.is_error_message_not_displayed()
    assert login_page.is_username_error_indicator_not_displayed()
    assert login_page.is_password_error_indicator_not_displayed()


def test_login_with_no_password(login_page):
    login_page.perform_unsuccessful_login(username=STANDARD_USER_USERNAME, password="")
    assert login_page.username_error_indicator.is_displayed()
    assert login_page.password_error_indicator.is_displayed()
    assert login_page.error_message.is_displayed()
    assert login_page.error_message.text == Resources.LoginPage.MISSING_PASSWORD_ERROR_TEXT
    assert login_page.close_error_button.is_displayed()
    login_page.close_error_button.click()
    assert login_page.is_error_message_not_displayed()
    assert login_page.is_username_error_indicator_not_displayed()
    assert login_page.is_password_error_indicator_not_displayed()
