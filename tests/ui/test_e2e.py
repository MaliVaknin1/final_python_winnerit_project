from utils import configs


def test_full_flow(login_page, base_ui_url, base_page, products_page):
    base_page.navigate_to(base_ui_url)
    login_page.success_login(configs.standard_user, configs.password)
    products_page.add_product_to_cart()