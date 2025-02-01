from playwright.sync_api import Page

from pages.base_page import BasePage
from utils.url_enum import URL


# Constructor and elements in checkout page
class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__first_name_textfield = page.get_by_placeholder("First Name")
        self.__last_name_textfield = page.get_by_placeholder("Last Name")
        self.__zip_code_textfield = page.get_by_placeholder("Zip/Postal Code")
        self.__continue_btn = page.get_by_role("button", name="Continue")
        self.__finish_btn = page.get_by_role("button", name="Finish")
        self.__cancel_btn = page.locator("[data-test=\"cancel\"]")
        self.__back_home_btn = page.get_by_role("button", name="Back Home")
        self.__confirmation_header = page.locator("[data-test=\"complete-header\"]")

    # Fill in first name ,last name and zip code fields and validate the fields aren't empty
    def validate_checkout_textfield(self, first_name: str, last_name: str, zip_code: str):
        self.fill_in_field(self.__first_name_textfield, first_name)
        self.fill_in_field(self.__last_name_textfield, last_name)
        self.fill_in_field(self.__zip_code_textfield, zip_code)
        self.validate_field_not_has_value(self.__first_name_textfield, "")
        self.validate_field_not_has_value(self.__last_name_textfield, "")
        self.validate_field_not_has_value(self.__zip_code_textfield, "")

    # Click on continue btn and validate user is navigated to overview page
    def validate_second_checkout_flow(self):
        self.click_on_button(self.__continue_btn)
        self.validate_page_url(URL.OVERVIEW_CHECKOUT_PAGE_URL.get_url())

    # Click on finish button in overview page and verify: -user is navigated to approval page, -Back Home page
    # button is displayed, -"Thank you for your order " text is displayed
    def validate_confirmation_page_of_checkout(self):
        self.click_on_button(self.__finish_btn)
        self.validate_page_url(URL.CHECKOUT_COMPLETE_PAGE_URL.get_url())
        self.validate_element_is_visible(self.__back_home_btn)
        self.validate_element_has_txt(self.__confirmation_header, "Thank you for your order!")

    # Click on Cancel button and verify user is navigated to cart page
    def cancel_checkout_and_verify_navigation(self):
        self.click_on_button(self.__cancel_btn)
        self.validate_page_url(URL.CART_PAGE_URL.get_url())
