from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from utils.url_enum import URL


#Constructor and elements in cart page
class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page= page
        self.__checkout_btn=page.locator("[data-test=\"checkout\"]")
        self.__continue_shopping_btn=page.locator("[data-test=\"continue-shopping\"]")
        self.__remove_btn=page.get_by_test_id("remove-sauce-labs-backpack")
        self.__your_cart_title=page.locator("[data-test=\"title\"]")
        self.__cart_icon = page.locator("[data-test=\"shopping-cart-link\"]")
        self.__empty_cart_page_wrapper=page.locator("#page_wrapper")



#Click on cart icon and verify the title is 'Your Cart', 'remove', 'checkout' and 'continue shopping' buttons are displayed.
    def validate_cart_page_contains_title_and_buttons(self):
        self.click_on_button(self.__cart_icon)
        self.validate_element_has_txt(self.__your_cart_title,"Your Cart")
        self.validate_element_is_visible(self.__checkout_btn)
        self.validate_element_is_visible(self.__remove_btn)
        self.validate_element_is_visible(self.__continue_shopping_btn)

#Click on 'Remove' and verify the product page is empty
    def validate_removing_product_from_cart(self):
        self.click_on_button(self.__remove_btn)
        expect(self.__empty_cart_page_wrapper).to_match_aria_snapshot("- button \"Open Menu\"\n- img \"Open Menu\"\n- text: Swag Labs Your Cart QTY Description\n- button \"Go back Continue Shopping\":\n  - img \"Go back\"\n- button \"Checkout\"\n- contentinfo:\n  - list:\n    - listitem:\n      - link \"Twitter\"\n    - listitem:\n      - link \"Facebook\"\n    - listitem:\n      - link \"LinkedIn\"\n  - text: /© \\d+ Sauce Labs\\. All Rights Reserved\\. Terms of Service \\| Privacy Policy/")


#Click on Checkout button and validate user is navigated to checkout page
    def validate_checkout_btn(self):
        self.click_on_button(self.__checkout_btn)
        self.validate_page_url(URL.CHECKOUT_PAGE_URL.get_url())

#Click on continue shopping and verify user is navigated to products page
    def validate_continue_shopping_btn(self):
        self.click_on_button(self.__continue_shopping_btn)
        self.validate_page_url(URL.PRODUCTS_PAGE_URL.get_url())