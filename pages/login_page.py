import pytest
from assertpy import assert_that
from playwright.sync_api import Page

from pages.base_page import BasePage
from utils.configs import standard_user, password
from utils.url_enum import URL


#constructor
class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page= page
        self.__username_textfield= page.get_by_placeholder("Username")
        self.__password_textfield= page.get_by_placeholder("Password")
        self.__login_btn= page.get_by_role("button", name="Login")

#Fill in username & password, click Login, verify user is redirected
#to inventory page

    def success_login(self, username: str, passwords:str):
        self.fill_in_field(self.__username_textfield, username)
        self.fill_in_field(self.__password_textfield, passwords)
        self.__login_btn.click()
        assert_that(self.__page.url).is_equal_to(URL.INVENTORY_PAGE_URL.get_url())

