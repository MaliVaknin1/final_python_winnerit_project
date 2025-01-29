from symtable import Class

import pytest
from playwright.sync_api import Page

from utils import configs
from utils.configs import PASSWORD, DATA

#Go to sauce.com, test login function for 4 users.
#the users are saved in configs file. and verify user is navigated to product page.
@pytest.mark.parametrize("username",DATA)
def test_success_login(login_page, base_ui_url, base_page,username):
    base_page.navigate_to(base_ui_url)
    login_page.validate_success_login(username=username, passwords=PASSWORD)

#Go to sauce.com, test fail login without insert password
#and verify property error message is displayed.
def test_login_without_password_display_error(login_page, base_ui_url,base_page):
    base_page.navigate_to(base_ui_url)
    login_page.fail_login_without_password()

#Go to sauce.com, test fail login with locked out user
#and verify property error message is displayed
def test_login_with_locked_out_user_display_error(login_page, base_ui_url,base_page):
    base_page.navigate_to(base_ui_url)
    login_page.fail_login_locked_out_user()

#Go to sauce.com, test fail login with locked out user
#and verify property error message is displayed
def test_login_with_incorrect_user_display_error(login_page, base_ui_url,base_page):
    base_page.navigate_to(base_ui_url)
    login_page.fail_login_incorrect_user()

#Go to sauce.com , test fail login without inserting username or password
# and verify that the value still empty and an error message is displayed.
def test_login_without_user_and_pass_display_error(login_page, base_ui_url,base_page):
    base_page.navigate_to(base_ui_url)
    login_page.fail_login_empty_user_and_pass()