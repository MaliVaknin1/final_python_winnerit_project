from assertpy import assert_that
from playwright.sync_api import Page, Locator, expect

from utils.url_enum import URL


class BasePage:
    #constructor
    def __init__(self, page: Page):
        self.__page=page

    #general method of clicking button
    def click_on_button(self, btn: Locator):
        btn.click()

    #general method of navigation url
    def navigate_to(self, url: str):
        self.__page.goto(url)

    #general method of fill in field
    def fill_in_field(self, field: Locator, txt: str):
        field.fill(txt,timeout= 30000)

    #general method to fill in textfield one by one
    def fill_in_field_sequentialy(self, field: Locator, txt: str):
        field.press_sequentially(txt, delay= 200)

    def validate_page_url(self, expected_url:str):
        expect(self.__page).to_have_url(expected_url)

    def validate_element_has_txt(self, element:Locator, txt: str):
        expect(element).to_have_text(txt)

    def validate_element_is_visible(self, element: Locator):
        expect(element).to_be_visible()
