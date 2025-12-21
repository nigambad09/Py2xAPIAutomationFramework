from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_product(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    page = ProductPage(driver)
    page.product_page()
