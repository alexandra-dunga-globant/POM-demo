__author__ = 'Alexandra Dunga'

import pytest

from config.config import TestData
from tests.test_base import BaseTest


@pytest.mark.env("QA")
class TestHome(BaseTest):

    @pytest.mark.dependency()
    @pytest.mark.xfail(reason="deliberate fail")
    def test_unsuccessfull_login(self, setup_login_page):
        setup_login_page.login(TestData.USERNAME, TestData.WRONG_PASSWORD)
        assert False

    @pytest.mark.smoke
    def test_home_page_title(self, setup_home_page):
        title = setup_home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    @pytest.mark.env("PROD")
    def test_home_page_header(self, setup_home_page):
        header = setup_home_page.get_header_value(TestData.HOME_PAGE_HEADER)
        assert header == TestData.HOME_PAGE_HEADER

    @pytest.mark.dependency(depends=['test_unsuccessfull_login'])
    @pytest.mark.skip(reason="deliberate skip due to test_unsuccessfull_login")
    def test_home_page_account_name(self, setup_home_page):
        account_name = setup_home_page.get_account_name_value()
        assert account_name == TestData.ACCOUNT_NAME

    @pytest.mark.dependency(depends=['test_unsuccessfull_login'])
    @pytest.mark.skip(reason="deliberate skip due to test_unsuccessfull_login")
    def test_home_page_logout_button(self, setup_home_page):
        assert setup_home_page.is_logout_displayed()
