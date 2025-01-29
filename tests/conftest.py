import  pytest
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from utils.configs import BASE_UI_URL


#fixture to all useful pages.
@pytest.fixture
def login_page(page:Page):
    return LoginPage(page)

@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

@pytest.fixture
def products_page(page: Page):
    return ProductsPage(page)

@pytest.fixture
def checkout_page(page: Page):
    return CheckoutPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)

#fixture to useful url
@pytest.fixture(scope="session")
def base_ui_url():
    return BASE_UI_URL
