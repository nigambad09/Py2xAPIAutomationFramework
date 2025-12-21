from selenium.webdriver.common.by import By
from .base_page import BasePage


# class ProductPage(BasePage):
#     ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')]")
#     CART_ICON = (By.ID, "cart")
#
#     def add_product_to_cart(self):
#         self.click(self.ADD_TO_CART_BTN)
#
#     def go_to_cart(self):
#         self.click(self.CART_ICON)

class ProductPage(BasePage):
    add_to_cart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    cart_button = (By.XPATH, "//a[@class='shopping_cart_link']")

    def product_page(self):
        self.click(self.add_to_cart)
        self.click(self.cart_button)
        self.title()
