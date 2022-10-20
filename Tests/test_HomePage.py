__author__ = 'Alexandra Dunga'

import pytest

from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import TestData



class TestHome(BaseTest):
   #move to conftest.py
    @pytest.fixture(scope="class")
    def setup_home_page(self):
        loginPage = LoginPage(self.driver)
        homePage = loginPage.login(TestData.USERNAME, TestData.PASSWORD)
        yield homePage
        homePage.logout()

    def test_home_page_title(self, setup_home_page):
        title = setup_home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self, setup_home_page):
        header = setup_home_page.get_header_value(TestData.HOME_PAGE_HEADER)
        assert header == TestData.HOME_PAGE_HEADER

    def test_home_page_account_name(self, setup_home_page):
        account_name = setup_home_page.get_account_name_value()
        assert account_name == TestData.ACCOUNT_NAME

    def test_home_page_logout_button(self, setup_home_page):
        assert setup_home_page.is_logout()
