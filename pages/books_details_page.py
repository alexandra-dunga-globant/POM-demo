__author__ = 'Alexandra Dunga'

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BooksDetailsPage(BasePage):

    """
    By locators
    """
    BOOK_DETAILS_ISBN = (By.XPATH, "//*/div[@id='ISBN-wrapper']//*[@id='userName-value']")
    BOOK_DETAILS_PAGE_NR = (By.XPATH, "//*/div[@id='pages-wrapper']//*[@id='userName-value']")

    def __init__(self, driver, base_url, env, book_id):
        """Constructor of the page"""
        super().__init__(driver)
        self.base_url = base_url
        self.env = env
        self.browser = driver
        self.path = "/books?book="
        self.id = book_id
        # adding /books to the base_url
        self.driver.get(f"{self.base_url}{self.path}{self.id}")

    '''Page actions for Books Page'''

    def add_book_to_collection(self):
        pass

    def go_to_book_store(self):
        pass
