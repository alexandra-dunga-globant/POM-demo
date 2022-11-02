__author__ = 'Alexandra Dunga'

from config.config import TestData
from tests.test_base import BaseTest


class TestLogin(BaseTest):

    """Check if the signup link exists"""
    def test_signup_link_visible(self, setup_login_page):
        flag = setup_login_page.is_signup_link()
        assert flag

    '''Check the login page title'''
    def test_login_page_title(self, setup_login_page):
        title = setup_login_page.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    ''' Check the login page header'''
    def test_login_page_header(self, setup_login_page):
        header = setup_login_page.get_header_value(TestData.LOGIN_PAGE_HEADER)
        assert header == TestData.LOGIN_PAGE_HEADER
