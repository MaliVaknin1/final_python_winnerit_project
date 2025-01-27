from playwright.sync_api import Page


class BasePage:
    #constructor
    def __init__(self, page: Page):
        self.__page=page

    #general method of clicking button
    def click_on_button(self, btn):
        self.__page.get_by_role("button", name=btn).click()


    #general method of navigation url
    def navigate_to(self, url: str):
        self.__page.goto(url)

    #general method of fill in field
    def fill_in_field(self, field, txt: str):
        field.fill(txt)

