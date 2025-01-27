from symtable import Class

import pytest
from playwright.sync_api import Page

from utils.configs import password, data

#test login function for 4 users, the users are saved in configs file.
@pytest.mark.parametrize("username",data)
def test_success_login(login_page, base_ui_url, base_page,username):
    base_page.navigate_to(base_ui_url)
    login_page.success_login(username=username, passwords=password)


