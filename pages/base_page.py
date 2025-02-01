from assertpy import assert_that
from playwright.sync_api import Page, Locator, expect

from utils.url_enum import URL


class BasePage:
    # constructor
    def __init__(self, page: Page):
        self.__page = page

    # general method of clicking button
    def click_on_button(self, btn: Locator):
        btn.click()

    # general method of navigation url
    def navigate_to(self, url: str):
        self.__page.goto(url)

    # general method of fill in field
    def fill_in_field(self, field: Locator, txt: str):
        field.fill(txt, timeout=30000)

    # general method to fill in textfield one by one
    def fill_in_field_sequentialy(self, field: Locator, txt: str):
        field.press_sequentially(txt, delay=200)

    # general method to validate the url of page
    def validate_page_url(self, expected_url: str):
        expect(self.__page).to_have_url(expected_url)

    # general method to validate that the element has specific text
    def validate_element_has_txt(self, element: Locator, txt: str):
        expect(element).to_have_text(txt)

    # general method t validate that element is visible in the page
    def validate_element_is_visible(self, element: Locator):
        expect(element).to_be_visible()

    # general method to validate that specific text isn't populated in the field.
    def validate_field_not_has_value(self, field: Locator, txt: str):
        expect(field).not_to_have_value(txt)
