__author__ = 'Alexandra Dunga'

import pytest

from config.config import TestData
from pages.books_page import BooksPage
from tests.test_base import BaseTest


class TestBooks(BaseTest):

    """Check if the signup link exists"""

    @pytest.mark.parametrize("header", [BooksPage.TITLE, BooksPage.AUTHOR, BooksPage.PUBLISHER])
    def test_is_header_displayed(self, setup_books_page, header):
        flag = setup_books_page.is_text_element_displayed(header)
        assert flag
