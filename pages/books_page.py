__author__ = 'Alexandra Dunga'

from selenium.webdriver.common.by import By

from config.config import TestData
from pages.base_page import BasePage


class BooksPage(BasePage):

    """
    By locators
    """
    TITLE = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Title')]")
    AUTHOR = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Author')]")
    PUBLISHER = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Publisher')]")

    def __init__(self, driver, base_url, env):
        """Constructor of the page"""
        super().__init__(driver)
        self.base_url = base_url
        self.env = env
        self.browser = driver
        self.path = "/books"
        # adding /books to the base_url
        self.driver.get(f"{self.base_url}{self.path}")

    '''Page actions for Books Page'''

    def get_books_table_header_title(self):
        return self.get_element_text(self.TITLE)
