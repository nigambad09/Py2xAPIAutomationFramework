from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def find(self, locator):
#         return self.driver.find_element(*locator)
#
#     def click(self, locator):
#          self.find(locator).click()
#
#     def type(self, locator, text):
#          self.find(locator).send_keys(text)
#
#     def wait_for_visible(self, locator, timeout=10):
#         WebDriverWait(self.driver, timeout).until(
#             EC.visibility_of_element_located(locator)
#         )
#
#     def get_text(self, locator):
#         return self.find(locator).text
#

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def type(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def title(self):
        return self.driver.title
