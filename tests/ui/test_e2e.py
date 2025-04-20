import allure

from tests.conftest import random_checkout_user_data
from utils import configs


# Full flow-login to system, clicking on Add to cart and, clicking on the image, Clicking on Back to products
# Clicking on cart icon, Clicking on Checkout btn, Fill in checkout fields, Clicking on Continue btn,
# Clicking on Finish btn
def test_successfully_order_process(login_page, base_ui_url, base_page, products_page, checkout_page,
                                    cart_page, random_checkout_user_data):
    base_page.navigate_to(base_ui_url)
    login_page.validate_success_login(configs.STANDARD_USER, configs.PASSWORD)
    products_page.validate_add_product_to_cart()
    products_page.validate_product_container_contains_data()
    products_page.validate_back_to_products_btn()
    cart_page.validate_cart_page_contains_title_and_buttons()
    cart_page.validate_checkout_btn()
    checkout_page.validate_checkout_textfield(random_checkout_user_data["first_name"],
                                              random_checkout_user_data["last_name"],
                                              random_checkout_user_data["zip_code"]
                                              )
    checkout_page.validate_second_checkout_flow()
    checkout_page.validate_confirmation_page_of_checkout()


# Full flow-login to system, clicking on Add to cart and, Verify cart icon displays, Clicking on cart icon,
# Clicking on Remove product btn,Clicking on Continue shopping btn,re-clicking on Add to cart, Re-clicking on cart icon
# Clicking on checkout btn, Clicking on Cancel btn
def test_fail_order_proces(login_page, base_ui_url, base_page, products_page, checkout_page,
                           cart_page, random_checkout_user_data):
    base_page.navigate_to(base_ui_url)
    login_page.validate_success_login(configs.STANDARD_USER, configs.PASSWORD)
    products_page.validate_add_product_to_cart()
    products_page.validate_shopping_cart_link_is_visible()
    products_page.validate_clicking_cart_icon_navigate_to_cart_page()
    cart_page.validate_removing_product_from_cart()
    cart_page.validate_continue_shopping_btn()
    products_page.validate_add_product_to_cart()
    cart_page.validate_cart_page_contains_title_and_buttons()
    cart_page.validate_checkout_btn()
    checkout_page.cancel_checkout_and_verify_navigation()
