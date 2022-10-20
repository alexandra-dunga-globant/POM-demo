import pytest
from Config.config import TestData
from Pages.LoginPage import LoginPage


# @pytest.fixture(scope="function")
# def setup_home_page(init_driver):
#     if self is None:
#         print("---------------The init_driver is NONE!!! --------------")
#     loginPage = LoginPage(init_driver)
#     homePage = loginPage.login(TestData.USERNAME, TestData.PASSWORD)
#     yield
#     homePage.logout()
#
#
# @pytest.fixture(scope="class")
# def setup_login_page(init_driver):
#     loginPage = LoginPage(init_driver)
#     yield loginPage
