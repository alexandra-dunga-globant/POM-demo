__author__ = 'Alexandra Dunga'

from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage


class LoginPage(BasePage):
    """
    By locators
    """
    EMAIL = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    SIGNUP_LINK = (By.ID, "newUser")

    def __init__(self, driver, base_url, env):
        """Constructor of the page"""
        super().__init__(driver, base_url, env)
        self.path = "/login"
        # adding /login to the base_url
        self.browser.get(f"{self.base_url}{self.path}")

    '''Page actions for Login Page'''

    def get_login_page_title(self, text):
        return self.get_title(text)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def is_signup_link_displayed(self):
        return self.is_visible(self.SIGNUP_LINK)

    def login(self, username, password):
        if self.is_visible(self.LOGIN_BUTTON):
            self.send_keys(self.EMAIL, username)
            self.send_keys(self.PASSWORD, password)
            self.click(self.LOGIN_BUTTON)
            return HomePage(self.browser, self.base_url, self.env)
