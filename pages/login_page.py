from utils import configs
from utils.error_msg_enum import ERRORS

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from utils.configs import STANDARD_USER, PASSWORD
from utils.url_enum import URL


# Constructor and elements in login page
class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__username_textfield = page.get_by_placeholder("Username")
        self.__password_textfield = page.get_by_placeholder("Password")
        self.__login_btn = page.get_by_role("button", name="Login")
        self.__error_msg_container = page.locator(".error-message-container")

    # Insert username & password, click on Login btn , verify the user is redirected to inventory page

    def validate_success_login(self, username: str, passwords: str):
        self.fill_in_field(self.__username_textfield, username)
        self.fill_in_field_sequentialy(self.__password_textfield, passwords)
        self.__login_btn.click()
        self.validate_page_url(URL.PRODUCTS_PAGE_URL.get_url())

    # Insert username without password, click on Login btn and verify error message is displayed
    def fail_login_without_password(self):
        self.fill_in_field(self.__username_textfield, configs.STANDARD_USER)
        self.__login_btn.click()
        self.validate_element_has_txt(self.__error_msg_container, ERRORS.EMPTY_PASSWORD_FIELD_ERROR.value)

    # Insert locked out username and correct password, click on Login btn ,and verify an error of locked out user is displayed
    def fail_login_locked_out_user(self):
        self.fill_in_field(self.__username_textfield, configs.LOCKED_OUT_USER)
        self.fill_in_field_sequentialy(self.__password_textfield, PASSWORD)
        self.__login_btn.click()
        self.validate_element_has_txt(self.__error_msg_container, ERRORS.LOCKED_OUT_USER_ERROR.value)

    # Insert incorrect username and correct password, click on Login btn ,and verify an error of incorrect user is displayed
    def fail_login_incorrect_user(self):
        self.fill_in_field(self.__username_textfield, configs.INVALID_USERNAME)
        self.fill_in_field_sequentialy(self.__password_textfield, PASSWORD)
        self.__login_btn.click()
        self.validate_element_has_txt(self.__error_msg_container, ERRORS.INCORRECT_USERNAME_ERROR.value)

    # Click on Login btn without inserting username or password and verify that the value still empty and an error message is displayed.
    def fail_login_empty_user_and_pass(self):
        self.click_on_button(self.__login_btn)
        input_username = self.__username_textfield.input_value()
        input_password = self.__password_textfield.input_value()
        assert input_username == ""
        assert input_password == ""
        self.validate_element_has_txt(self.__error_msg_container, ERRORS.EMPTY_USERNAME_FIELD_ERROR.value)
