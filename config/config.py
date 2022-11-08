__author__ = 'Alexandra Dunga'

from decouple import config


# TO DO
# to run remote tests on Github actions (including passwords)

class TestData:
    BASE_URL = {
        "QA": "https://demoqa.com",
        "PROD": "https://demoqa.com"
    }

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

    #Books page
    BOOK_TITLE = "Learning JavaScript Design Patterns"
    BOOK_AUTHOR = "Addy Osmani"
    BOOK_PUBLISHER = "O'Reilly Media"
    BOOK_ISBN = "9781449331818"
    BOOK_URL = ""
    BOOK_PAGE_NR = "254"
