import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
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
def base_url(env):
    """
    E.g. https://api.sandbox.paack.app
    :param env:
    :return: The API base URL corresponding to the given environment.
    """
    return TestData.BASE_URL[env]


@pytest.fixture(params=["chrome"], scope="class")
def browser(request):
    """Initialising the browser(s)"""
    if request.param == "chrome":
        service = ChromeService(executable_path=SetupData.CHROME_EXEC_PATH)
        web_driver = webdriver.Chrome(service=service)
    if request.param == "firefox":
        service = FirefoxService(executable_path=SetupData.FIREFOX_EXEC_PATH)
        web_driver = webdriver.Firefox(service=service)
    web_driver.delete_all_cookies()
    # web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield web_driver
    web_driver.quit()
