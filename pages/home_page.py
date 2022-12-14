__author__ = 'Alexandra Dunga'

from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    """ By locators """

    ACCOUNT_NAME = (By.ID, "userName-value")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(text(),'Log out')]")

    def __init__(self, driver, base_url, env):
        ''' Constructor of the page '''
        super().__init__(driver, base_url, env)

    '''Page actions for Login Page'''

    def get_home_page_title(self, text):
        return self.get_title(text)

    def is_logout_displayed(self):
        return self.is_visible(self.LOGOUT_BUTTON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            # wait for loading to finish
            sleep(10)
            return self.get_element_text(self.HEADER)

    def get_account_name_value(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)

    def logout(self):
        if self.is_visible(self.LOGOUT_BUTTON):
            self.click(self.LOGOUT_BUTTON)
