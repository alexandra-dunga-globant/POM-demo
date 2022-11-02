__author__ = 'Alexandra Dunga'

from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Config.config import TestData


class BooksPage(BasePage):
    """
    By locators
    """
    TITLE = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Title')]")
    AUTHOR = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Author')]")
    PUBLISHER = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Publisher')]")

    # // *[ @ id = "see-book-Git Pocket Guide"] / a

    '''Constructor of the page'''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BOOKS_URL)

    '''Page actions for Books Page'''
    '''Used to get the page title'''

    def get_books_table_header_title(self):
        return self.get_element_text(self.TITLE)

