import pytest
import yaml
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config.config import Config


# @pytest.fixture(scope="session")
# def config():
#     with open("C:/Users/Computer HuB/PycharmProjects/selenium_pytest_framework/config/config.yaml") as f:
#         return yaml.safe_load(f)


# @pytest.fixture
# def driver(config):
#     if config["browser"].lower() == "chrome":
#         driver = webdriver.Chrome()
#     elif config["browser"].lower() == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise ValueError(f"Browser {config['browser']} is not supported")
#
#     driver.maximize_window()
#     driver.implicitly_wait(config["implicit_wait"])
#     driver.get(config["url"])
#     yield driver
#     driver.quit()

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    # driver.get(Config.url())
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


