from enum import Enum

from utils.configs import BASE_UI_URL



class URL(Enum):
    PRODUCTS_PAGE_URL= f"{BASE_UI_URL}/inventory.html"
    CART_PAGE_URL= f"{BASE_UI_URL}/cart.html"
    CHECKOUT_PAGE_URL =f"{BASE_UI_URL}/checkout-step-one.html"


    # Private attribute
    def __init__(self, url: str):
        self.__url = url

    # Public getter for the private URL
    def get_url(self) -> str:
        return self.__url