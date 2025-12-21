from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# class LoginPage(BasePage):
#     USERNAME = (By.ID, "user-name")
#     PASSWORD = (By.ID, "password")
#     LOGIN_BTN = (By.ID, "login-button")
#     LOGO =(By.XPATH,"//div[@class='app_logo']")
#
#     def login(self, username, password):
#         self.type(self.USERNAME, username)
#         self.type(self.PASSWORD, password)
#         self.click(self.LOGIN_BTN)
#         print(self.get_text(self.LOGO))


class LoginPage(BasePage):
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def login(self, usr, pwd):
        self.type(self.username, usr)
        self.type(self.password, pwd)
        print(usr,pwd)
        self.click(self.login_button)
