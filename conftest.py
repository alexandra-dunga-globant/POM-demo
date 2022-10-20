import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from Config.config import TestData
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from Pages.LoginPage import LoginPage


@pytest.fixture(params=["chrome"], scope="class", autouse=True)
def init_driver(request):
    if request.param == "chrome":
        service = ChromeService(executable_path=TestData.CHROME_EXEC_PATH)
        web_driver = webdriver.Chrome(service=service)
    if request.param == "firefox":
        service = FirefoxService(executable_path=TestData.FIREFOX_EXEC_PATH)
        web_driver = webdriver.Firefox(service=service)
    web_driver.delete_all_cookies()
    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.quit()

# To fix : The init_driver is always None if I have this fixture defined here
# @pytest.fixture(scope="class")
# def setup_home_page(init_driver):
#     if init_driver is None:
#         print("---------------The init_driver is NONE!!! --------------")
#     loginPage = LoginPage(init_driver)
#     homePage = loginPage.login(TestData.USERNAME, TestData.PASSWORD)
#     yield
#     homePage.logout()


