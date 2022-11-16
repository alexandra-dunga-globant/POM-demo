__author__ = 'Alexandra Dunga'

import pytest

from config.config import TestData
from pages.base_page import BasePage
from pages.books_details_page import BooksDetailsPage
from pages.books_page import BooksPage
from tests.test_base import BaseTest


class TestBooks(BaseTest):

    @pytest.mark.parametrize("header", [BooksPage.TITLE_HEADER, BooksPage.AUTHOR_HEADER, BooksPage.PUBLISHER_HEADER])
    def test_is_header_displayed(self, setup_books_page, header):
        flag = setup_books_page.is_visible(header)
        assert flag

    @pytest.mark.parametrize("by_locator,expected_text",
                             [(BooksPage.BOOK_TITLE_LINK, TestData.BOOK_TITLE),
                              (BooksPage.BOOK_AUTHOR, TestData.BOOK_AUTHOR),
                              (BooksPage.BOOK_PUBLISHER, TestData.BOOK_PUBLISHER)])
    def test_book_text(self, setup_books_page, by_locator, expected_text):
        """ Check book title, author and publisher """
        book_element_text = setup_books_page.get_element_text(by_locator)
        assert book_element_text == expected_text

    def test_book_details_url(self, setup_books_page):
        """ Check that the url contains the ISBN code of the book """
        book_url = setup_books_page.get_book_details_url()
        check_ISBN = book_url.find(TestData.BOOK_ISBN)
        assert check_ISBN
