import pytest
from Config.config import TestData
from Pages.BooksPage import BooksPage
from Pages.LoginPage import LoginPage

# TO DO
#place test files under folders

@pytest.fixture(scope="class")
def setup_login_page(init_driver):
    print("Init_driver driver: ", init_driver)
    loginPage = LoginPage(init_driver)
    yield loginPage

@pytest.fixture(scope="class")
def setup_home_page(init_driver):
    loginPage = LoginPage(init_driver)
    homePage = loginPage.login(TestData.USERNAME, TestData.PASSWORD)
    yield homePage
    homePage.logout()

@pytest.fixture(scope="class")
def setup_books_page(init_driver):
    print("Init_driver driver: ", init_driver)
    booksPage = BooksPage(init_driver)
    yield booksPage
