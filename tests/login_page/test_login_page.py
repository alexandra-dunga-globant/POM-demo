__author__ = 'Alexandra Dunga'

import pytest

from config.test_data import TestData
from tests.test_base import BaseTest


class TestLogin(BaseTest):
    @pytest.mark.smoke
    def test_signup_link_visible(self, setup_login_page):
        flag = setup_login_page.is_signup_link_displayed()
        assert flag

    @pytest.mark.smoke
    def test_login_page_title(self, setup_login_page):
        title = setup_login_page.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login_page_header(self, setup_login_page):
        header = setup_login_page.get_header_value()
        assert header == TestData.LOGIN_PAGE_HEADER
