__author__ = 'Alexandra Dunga'


class TestData:
    BASE_URL = {
        "QA": "https://demoqa.com",
        "PROD": "https://demoqa.com"
    }

    WRONG_PASSWORD = "JustATest"

    # The values against we do ASSERTS in Test classes

    #Login page
    LOGIN_PAGE_TITLE = "ToolsQA"
    LOGIN_PAGE_HEADER = "Login"

    #Home page
    HOME_PAGE_TITLE = "ToolsQA"
    HOME_PAGE_HEADER = "Profile"
    ACCOUNT_NAME = "Alexandra"

    #Books page
    BOOK_TITLE = "Learning JavaScript Design Patterns"
    BOOK_AUTHOR = "Addy Osmani"
    BOOK_PUBLISHER = "O'Reilly Media"
    BOOK_ISBN = "9781449331818"
    BOOK_PAGE_NR = "254"

    #Menu item
    MENU_ELEM_EXPANDED = "Practice Form"
