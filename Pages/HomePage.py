__author__ = 'Alexandra Dunga'

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    """ By locators """

    HEADER = (By.CSS_SELECTOR, "div.main-header")
    ACCOUNT_NAME = (By.ID, "userName-value")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(text(),'Log out')]")

    ''' Constructor of the page '''

    def __init__(self, driver):
        super().__init__(driver)

    '''Page actions for Login Page'''
    '''Used to get the page title'''

    def get_home_page_title(self, text):
        return self.get_title(text)

    '''Used to check if the logout button is displayed'''

    def is_logout(self):
        return self.is_enabled(self.LOGOUT_BUTTON)

    '''Used to check the header value'''

    def get_header_value(self, text):
        if self.is_changed(self.HEADER, text):
            return self.get_element_text(self.HEADER)

    '''Used to check the account name value'''

    def get_account_name_value(self):
        if self.is_enabled(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)

    '''Used to logout'''

    def logout(self):
        if self.is_enabled(self.LOGOUT_BUTTON):
            self.click(self.LOGOUT_BUTTON)
