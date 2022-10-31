__author__ = 'Alexandra Dunga'

import pytest

from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.BooksPage import BooksPage


# @pytest.mark.usefixtures("setup_books_page")
# How to use a class fixture without passing it as a parameter in the test methods?
class TestBooks(BaseTest):

    """Check if the signup link exists"""

    @pytest.mark.parametrize("header", [BooksPage.TITLE, BooksPage.AUTHOR, BooksPage.PUBLISHER])
    def test_is_header_displayed(self, setup_books_page, header):
        flag = setup_books_page.is_text_element_displayed(header)
        assert flag
