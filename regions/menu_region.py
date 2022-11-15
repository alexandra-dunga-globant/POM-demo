from selenium.webdriver.common.by import By
from regions.base_region import BaseRegion


class MenuRegion(BaseRegion):
    """By locators"""
    MENU = (By.CSS_SELECTOR, "div.left-pannel")
    MENU_ELEMENT = (By.XPATH, "//*[@class='header-wrapper']/div[@class='header-text'][text()='Forms']")
    MENU_ELEM_EXPANDED = (By.XPATH, "//*[@class='element-list collapse show']/ul/li/span[@class='text']")

    _root_locator = MENU_ELEMENT

    def is_menu_visible(self):
        self.wait_for_region_to_load()

    def click_menu_element(self):
        return self.root.click()


