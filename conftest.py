import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options as CHOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from config.config import TestData
from config.setup import SetupData


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        dest="env",
        default="PROD",
        choices=("QA", "PROD"),
        help="The environment for the application under test."
    )
    parser.addoption(
        "--browser",
        action="store",
        dest="browser",
        default="chrome",
        choices=("firefox", "chrome", "all"),
        help="Select your desired browser.",
    )
    parser.addoption(
        "--headless",
        action="store",
        dest="headless",
        default="0",
        choices=("1", "0"),
        help="Select the browser state: 1 = headless (without GUI) or 0 = with GUI."
    )


@pytest.fixture(scope="session")
def env(request):
    """
    E.g.: QA, PROD.
    :param request:
    :return: The environment for the application under test.
    """
    e = request.config.getoption("env")
    return e.upper()

@pytest.fixture(scope="session")
def headless(request):
    """
    E.g.: 1=true, 0=false.
    :param request:
    :return: The headless state for the application under test.
    """
    h = request.config.getoption("headless")
    return bool(int(h))



@pytest.fixture(scope="session")
def base_url(env):
    """
    E.g. https://demoqa.com
    :param env:
    :return: The base URL corresponding to the given environment.
    """
    return TestData.BASE_URL[env]


@pytest.fixture(scope="session")
def browser_from_cmd(request):
    """
    Work in progress
    E.g.: chrome, firefox, all.
    :param request:
    :return: The list of browsers on which to perform the tests. For running on multiple browsers.
    """
    browser_opt = request.config.getoption("browser").lower()
    if browser_opt == "all":
        browsers = ["chrome", "firefox"]
    elif browser_opt == "chrome":
        browsers = ["chrome"]
    elif browser_opt == "firefox":
        browsers = ["firefox"]
    return browsers



@pytest.fixture(scope="class")
def browser(request, browser_from_cmd, headless):
    """Initialising the browser(s)"""
    # Getting the browser from the command line
    browser = request.config.getoption("browser").lower()
    if browser == "chrome":
        options = CHOptions()
        options.headless = headless
        service = ChromeService(executable_path=SetupData.CHROME_EXEC_PATH)
        web_driver = webdriver.Chrome(service=service, options=options)
    if browser == "firefox":
        options = FFOptions()
        options.headless = headless
        service = FirefoxService(executable_path=SetupData.FIREFOX_EXEC_PATH)
        web_driver = webdriver.Firefox(service=service, options=options)
    web_driver.delete_all_cookies()
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield web_driver
    web_driver.quit()
