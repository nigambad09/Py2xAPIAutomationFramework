from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogoutPage(BasePage):

    button = (By.XPATH,"//button[text()='Open Menu']")
    logout = (By.XPATH,"//a[text()='Logout']")

    def logout_page(self):
        self.click(self.button)
        self.click(self.logout)
