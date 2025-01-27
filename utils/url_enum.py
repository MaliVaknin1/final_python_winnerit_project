from enum import Enum

class URL(Enum):
    INVENTORY_PAGE_URL= "https://www.saucedemo.com/inventory.html"

    # Private attribute
    def __init__(self, url: str):
        self.__url = url

    # Public getter for the private URL
    def get_url(self) -> str:
        return self.__url