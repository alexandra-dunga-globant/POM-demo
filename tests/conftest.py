import pytest

from config.config import TestData
from pages.books_page import BooksPage
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def setup_login_page(browser):
    yield LoginPage(browser)


@pytest.fixture(scope="class")
def setup_home_page(browser):
    loginPage = LoginPage(browser)
    homePage = loginPage.login(TestData.USERNAME, TestData.PASSWORD)
    yield homePage
    homePage.logout()

@pytest.fixture(scope="class")
def setup_books_page(browser):
    yield BooksPage(browser)
