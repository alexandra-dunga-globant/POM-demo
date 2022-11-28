import pytest

from config.test_data import TestData
from pages.books_page import BooksPage
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def setup_login_page(browser, base_url, env):
    yield LoginPage(browser, base_url, env)


@pytest.fixture(scope="class")
def setup_home_page(browser, base_url, env):
    loginPage = LoginPage(browser, base_url, env)
    print("USERNAME + PASSWORD : ", TestData.USERNAME, " + ", TestData.PASSWORD)
    homePage = loginPage.login(TestData.USERNAME, TestData.PASSWORD)
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
