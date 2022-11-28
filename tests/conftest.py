import pytest

from config.test_data import TestData
from pages.books_page import BooksPage
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def setup_login_page(browser, base_url, env):
    yield LoginPage(browser, base_url, env)


@pytest.fixture(scope="class")
def setup_home_page(browser, base_url, env, get_username, get_password):
    loginPage = LoginPage(browser, base_url, env)
    homePage = loginPage.login(get_username, get_password)
    yield homePage
    homePage.logout()

@pytest.fixture(scope="class")
def setup_books_page(browser, base_url, env):
    yield BooksPage(browser, base_url, env)

@pytest.fixture(scope="class")
def setup_books_details_page(browser, base_url, env):
    booksPage = BooksPage(browser, base_url, env)
    books_details_page = booksPage.get_book_details_page()
    yield books_details_page
