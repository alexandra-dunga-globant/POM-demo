__author__ = 'Alexandra Dunga'

import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from regions.menu_region import MenuRegion


class BasePage:
    """
    This class is the parent of all pages. It contains the generic methods and utilities for all pages.
    """
    path = ""
    """ By locators"""
    HEADER = (By.CSS_SELECTOR, "div.main-header")
    """ Class composition for Menu"""
    MenuLocator = MenuRegion.MENU_ELEMENT

    def __init__(self, driver, base_url, env):
        self.browser = driver
        self.base_url = base_url
        self.env = env

    def click(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, text):
        WebDriverWait(self.browser, 10).until(EC.title_is(text))
        return self.browser.title

    def find_element(self, by_locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    @property
    def menu_region(self):
        locator = self.find_element(self.MenuLocator)
        return MenuRegion(self, root_element=locator)
