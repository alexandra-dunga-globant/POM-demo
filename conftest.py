import os
import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options as CHOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager, ChromeType
from webdriver_manager.firefox import GeckoDriverManager

from config.test_data import TestData


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


@pytest.fixture(scope="session")
def credentials(env):
    """
        E.g. https://demoqa.com
        :param env:
        :return: The credentials(username and password) corresponding to the given environment.
        """
    if env == "prod":
        return dict(username=os.environ['USERNAME_PROD'],
                    password=os.environ['PASSWORD_PROD'])
    else:
        return dict(username=os.environ['USERNAME_QA'],
                    password=os.environ['PASSWORD_QA'])


@pytest.fixture(scope="class")
def browser(request, headless):
    """Initialising the browser(s)"""
    # Getting the browser from the command line
    browser = request.config.getoption("browser").lower()
    if browser == "chrome":
        chrome_options = CHOptions()
        chrome_options.headless = headless
        chrome_service = ChromeService(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        options = [
            "--disable-gpu",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
        for option in options:
            chrome_options.add_argument(option)
        web_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    if browser == "firefox":
        ff_options = FFOptions()
        ff_options.headless = headless
        options = [
            "--disable-gpu",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
        for option in options:
            ff_options.add_argument(option)
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=service, options=ff_options)
    web_driver.delete_all_cookies()
    if headless:
        web_driver.set_window_size(1920, 1200)
    else:
        web_driver.maximize_window()
    request.cls.driver = web_driver
    yield web_driver
    web_driver.quit()
