import  pytest
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.login_page import LoginPage

#fixture to all useful pages.
@pytest.fixture
def login_page(page:Page):
    return LoginPage(page)

@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

#fixture to useful url
@pytest.fixture(scope="session")
def base_ui_url():
    return 'https://www.saucedemo.com/'
