__author__ = 'Alexandra Dunga'

from decouple import config


# TO DO
# to run remote tests on Github actions (including passwords)

class TestData:
    BASE_URL = "https://demoqa.com/login"
    USERNAME = config('USERNAME')
    PASSWORD = config('PASSWORD')

    # The values against we do ASSERTS in Test classes
    # TO DO
    # take dynamically these values
    # and to add them into a dictionary inside a fixture
    LOGIN_PAGE_TITLE = "ToolsQA"
    HOME_PAGE_TITLE = "ToolsQA"
    LOGIN_PAGE_HEADER = "Login"
    HOME_PAGE_HEADER = "Profile"
    ACCOUNT_NAME = "Alexandra"
