import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from config.config import TestData
from config.setup import SetupData


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
    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield web_driver
    web_driver.quit()
