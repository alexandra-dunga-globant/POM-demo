__author__ = 'Alexandra Dunga'

import pytest

from config.config import TestData
from pages.base_page import BasePage
from pages.books_details_page import BooksDetailsPage
from pages.books_page import BooksPage
from tests.test_base import BaseTest


class TestBooksDetails(BaseTest):



    @pytest.mark.parametrize("by_locator,expected_text",
                             [(BooksDetailsPage.BOOK_DETAILS_ISBN, TestData.BOOK_ISBN),
                              (BooksDetailsPage.BOOK_DETAILS_PAGE_NR, TestData.BOOK_PAGE_NR)])
    def test_book_details_elements(self, setup_books_details_page, by_locator, expected_text):
        """ Check book ISBN, page nr on book details page """
        book_element_text = setup_books_details_page.get_element_text(by_locator)
        assert book_element_text == expected_text
