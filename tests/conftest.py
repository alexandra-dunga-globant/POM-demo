import pytest

from pages.books_page import BooksPage
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def setup_login_page(browser, base_url, env):
    yield LoginPage(browser, base_url, env)


@pytest.fixture(scope="class")
def setup_home_page(browser, base_url, env, credentials):
    loginPage = LoginPage(browser, base_url, env)
    homePage = loginPage.login(credentials['username'], credentials['password'])
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
