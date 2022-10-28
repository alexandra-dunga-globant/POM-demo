__author__ = 'Alexandra Dunga'

from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.BooksPage import BooksPage


class TestBooks(BaseTest):

    """Check if the signup link exists"""
    def test_is_header_displayed(self, setup_books_page):
        flag = setup_books_page.is_header_displayed()
        assert flag
