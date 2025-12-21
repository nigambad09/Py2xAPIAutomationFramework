import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.logout_page import LogoutPage
from utilities.excel_reader import get_test_data


@pytest.mark.regression
@pytest.mark.parametrize("username,password", get_test_data("C:/Users/Computer HuB/Downloads/acb.xlsx", "Sheet1"))
def test_login_setup(setup,username,password):
    driver = setup

    login = LoginPage(driver)
    login.login(username,password)

    page = ProductPage(driver)
    page.product_page()

    logout = LogoutPage(driver)
    logout.logout_page()
