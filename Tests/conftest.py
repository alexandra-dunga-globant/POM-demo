import pytest
from Config.config import TestData
from Pages.books_page import BooksPage
from Pages.login_page import LoginPage


@pytest.fixture(scope="class")
def setup_login_page(init_driver):
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
    booksPage = BooksPage(init_driver)
    yield booksPage
