__author__ = 'Alexandra Dunga'

import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    This class is the parent of all pages. It contains the generic methods and utilities for all pages.
    """

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_changed(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(by_locator, text))
        return bool(element)

    def get_title(self, text):
        WebDriverWait(self.driver, 10).until(EC.title_is(text))
        return self.driver.title

    def is_text_element_displayed(self, text_item):
        return self.is_visible(text_item)
