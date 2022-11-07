from decouple import config
import sys

class SetupData:
    # to have a separate setup.py file only for exec path ( for ex browsers in incognito, specific states)

    CHROME_EXEC_PATH = "./resources/webdrivers/MacOS/chromedriver"
    FIREFOX_EXEC_PATH = "./resources/webdrivers/MacOS/geckodriver"
    EDGE_EXEC_PATH = "./resources/webdrivers/MacOS//msedgedriver"
    SAFARI_EXEC_PATH = "./resources/webdrivers/MacOS/safaridriver"
