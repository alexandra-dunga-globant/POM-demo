__author__ = 'Alexandra Dunga'

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.books_details_page import BooksDetailsPage


class BooksPage(BasePage):

    """
    By locators
    """
    TITLE_HEADER = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Title')]")
    AUTHOR_HEADER = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Author')]")
    PUBLISHER_HEADER = (By.XPATH, "//*[@class='rt-resizable-header-content'] [contains(text(),'Publisher')]")

    BOOK_TITLE_LINK = (By.XPATH, "//*[@id='see-book-Learning JavaScript Design Patterns']/a")
    BOOK_AUTHOR = (By.XPATH, "//*[@id='see-book-Learning JavaScript Design Patterns']//parent::div//parent::div//following-sibling::div")
    BOOK_PUBLISHER = (By.XPATH, "//*[@id='see-book-Learning JavaScript Design Patterns']//parent::div//parent::div//following-sibling::div[2]")

    def __init__(self, driver, base_url, env):
        """Constructor of the page"""
        super().__init__(driver, base_url, env)
        self.path = "/books"
        # adding /books to the base_url
        self.browser.get(f"{self.base_url}{self.path}")

    '''Page actions for Books Page'''

    def get_books_table_header_title(self):
        return self.get_element_text(self.TITLE_HEADER)

    def get_book_details_url(self):
        self.click(self.BOOK_TITLE_LINK)
        return str(self.browser.current_url)

    def get_book_details_page(self):
        full_url = self.get_book_details_url()
        book_id = full_url.partition("book=")[2]
        return BooksDetailsPage(self.browser, self.base_url, self.env, book_id)
