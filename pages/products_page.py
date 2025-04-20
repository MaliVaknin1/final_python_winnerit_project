import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from utils.url_enum import URL


# Constructor and elements in products page
class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__add_to_cart_btn = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.__remove_btn = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")
        self.__products_title = page.locator('[data-test="title"]')
        self.__products_img_container = page.locator('[data-test="inventory-container"]')
        self.__product_img = page.locator('[data-test="inventory-item-sauce-labs-backpack-img"]')
        self.__cart_icon = page.locator("[data-test=\"shopping-cart-link\"]")
        self._back_to_products_btn = page.get_by_role("button", name="Back to products")

    # Click on "Add to cart" button, and verify the btn is changed to "remove" and verify the title of page is "Products"
    def validate_add_product_to_cart(self):
        with allure.step(f"validating adding product to cart"):
            self.click_on_button(self.__add_to_cart_btn)
            self.validate_element_is_visible(self.__remove_btn)
            expect(self.__products_title).to_contain_text("Products")

    # Click on a product image and verify the image is displayed and "Back to products" button is displayed
    def validate_product_container_contains_data(self):
        with allure.step(f"validating product container contains data"):
            self.click_on_button(self.__product_img)
            expect(self.__products_img_container).to_match_aria_snapshot(
            "- img \"Sauce Labs Backpack\"\n- text: /Sauce Labs Backpack carry\\.allTheThings\\(\\) with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection\\. \\$\\d+\\.\\d+/\n- button \"Remove\"")
            self.validate_element_is_visible(self._back_to_products_btn)

    # Click on "back to products" button and verify user is navigated to Products page
    def validate_back_to_products_btn(self):
        with allure.step(f"validating clicking on back to products button is navigating to page:{URL.PRODUCTS_PAGE_URL.get_url()}"):
            self.click_on_button(self._back_to_products_btn)
            self.validate_page_url(URL.PRODUCTS_PAGE_URL.get_url())

    # Verify cart icon is displayed
    def validate_shopping_cart_link_is_visible(self):
        with allure.step(f"validating shopping cart link is visible"):
            self.validate_element_is_visible(self.__cart_icon)

    # Click on cart icon and verify user is navigated to cart page
    def validate_clicking_cart_icon_navigate_to_cart_page(self):
        with allure.step(f"validating clicking on cart icon is navigating to page:{URL.CART_PAGE_URL.get_url()}"):
            self.click_on_button(self.__cart_icon)
            self.validate_page_url(URL.CART_PAGE_URL.get_url())
