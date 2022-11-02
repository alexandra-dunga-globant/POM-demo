__author__ = 'Alexandra Dunga'

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page import HomePage


class LoginPage(BasePage):
    """
    By locators
    """
    HEADER = (By.CSS_SELECTOR, "div.main-header")
    EMAIL = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    SIGNUP_LINK = (By.ID, "newUser")

    '''Constructor of the page'''

    def __init__(self, driver):
        super().__init__(driver)

    '''Page actions for Login Page'''
    '''Used to get the page title'''

    def get_login_page_title(self, text):
        return self.get_title(text)

    '''Used to check the header value'''

    def get_header_value(self, text):
        if self.is_changed(self.HEADER, text):
            return self.get_element_text(self.HEADER)

    '''Used to check signup link'''

    def is_signup_link(self):
        return self.is_visible(self.SIGNUP_LINK)

    '''Used to login to app'''

    def login(self, username, password):
        if self.is_visible(self.LOGIN_BUTTON):
            self.send_keys(self.EMAIL, username)
            self.send_keys(self.PASSWORD, password)
            self.click(self.LOGIN_BUTTON)
            return HomePage(self.driver)
