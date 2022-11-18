__author__ = 'Alexandra Dunga'

import pytest

from config.test_data import TestData
from regions.menu_region import MenuRegion


@pytest.mark.usefixtures("browser")
class BaseTest:
    def test_click_menu(self, setup_login_page):
        setup_login_page.menu_region.click_menu_element()
        menu_elem_expand = setup_login_page.get_element_text(MenuRegion.MENU_ELEM_EXPANDED)
        assert menu_elem_expand == TestData.MENU_ELEM_EXPANDED
