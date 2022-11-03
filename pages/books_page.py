__author__ = 'Alexandra Dunga'

from selenium.webdriver.common.by import By

from config.config import TestData
from pages.base_page import BasePage


class BooksPage(BasePage):
    path = TestData.BASE_URL + '/books'
    """
    By locators
    """
    TITLE = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Title')]")
    AUTHOR = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Author')]")
    PUBLISHER = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Publisher')]")

    # // *[ @ id = "see-book-Git Pocket Guide"] / a

    def __init__(self, driver):
        """Constructor of the page"""
        super().__init__(driver)
        self.driver.get(self.path)

    '''Page actions for Books Page'''

    def get_books_table_header_title(self):
        return self.get_element_text(self.TITLE)
