import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options as CHOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from config.test_data import TestData
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


def pytest_configure(config):
    """ Add new markers """
    config.addinivalue_line("markers", "env(name): mark test to run only on named environment")
    config.addinivalue_line("markers", "smoke: mark test to run as smoke")
    config.addinivalue_line("markers", "dependency(depends): mark test to run as smoke")


def pytest_runtest_setup(item):
    envnames = [mark.args[0] for mark in item.iter_markers(name="env")]
    if envnames:
        if item.config.getoption("--env") not in envnames:
            pytest.skip("Test requires env in {!r}".format(envnames))


@pytest.fixture(scope="session")
def headless(request):
    """
    E.g.: 1=true, 0=false.
    :param request:
    :return: The headless state for the browser application under test.
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


@pytest.fixture(scope="class")
def browser(request, headless):
    """Initialising the browser(s)"""
    # Getting the browser from the command line
    browser = request.config.getoption("browser").lower()
    if browser == "chrome":
        options = CHOptions()
        options.headless = headless
        chrome_service = ChromeService(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        # service = ChromeService(executable_path=SetupData.CHROME_EXEC_PATH)
        web_driver = webdriver.Chrome(service=chrome_service, options=options)
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
