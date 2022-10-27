__author__ = 'Alexandra Dunga'
from decouple import config

# TO DO
# to run remote tests on Github actions (including passwords)

class TestData:
    CHROME_EXEC_PATH = "/Users/alexandra.dunga/Downloads/chromedriver"
    FIREFOX_EXEC_PATH = "/Users/alexandra.dunga/Downloads/geckodriver"
    EDGE_EXEC_PATH = "/Users/alexandra.dunga/Downloads/msedgedriver"
    SAFARI_EXEC_PATH = "/Users/alexandra.dunga/Downloads/safaridriver"

    BASE_URL = "https://demoqa.com/login"
    USERNAME = config('USERNAME')
    PASSWORD = config('PASSWORD')

    # The values against we do ASSERTS in Test classes
    LOGIN_PAGE_TITLE = "ToolsQA"
    HOME_PAGE_TITLE = "ToolsQA"
    LOGIN_PAGE_HEADER = "Login"
    HOME_PAGE_HEADER = "Profile"
    ACCOUNT_NAME = "Alexandra"
