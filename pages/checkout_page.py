from playwright.sync_api import Page

from pages.base_page import BasePage

#Constructor and elements in checkout page
class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page= page

#