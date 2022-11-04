__author__ = 'Alexandra Dunga'

from selenium.webdriver.common.by import By

from config.config import TestData
from pages.base_page import BasePage
from pages.home_page import HomePage


class LoginPage(BasePage):
    # path = TestData.BASE_URL + '/login'
    """
    By locators
    """
    HEADER = (By.CSS_SELECTOR, "div.main-header")
    EMAIL = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    SIGNUP_LINK = (By.ID, "newUser")

    def __init__(self, driver, base_url, env):
        """Constructor of the page"""
        super().__init__(driver)
        self.base_url = base_url
        self.env = env
        self.browser = driver
        self.path = "/login"
        # adding /login to the base_url
        self.driver.get(f"{self.base_url}{self.path}")

    '''Page actions for Login Page'''

    def get_login_page_title(self, text):
        return self.get_title(text)

    def get_header_value(self, text):
        if self.is_changed(self.HEADER, text):
            return self.get_element_text(self.HEADER)

    def is_signup_link_displayed(self):
        return self.is_visible(self.SIGNUP_LINK)

    def login(self, username, password):
        if self.is_visible(self.LOGIN_BUTTON):
            self.send_keys(self.EMAIL, username)
            self.send_keys(self.PASSWORD, password)
            self.click(self.LOGIN_BUTTON)
            return HomePage(self.driver)
