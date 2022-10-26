import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from Config.config import TestData
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService



@pytest.fixture(params=["chrome", "firefox"], scope="class", autouse=True)
def init_driver(request):
    if request.param == "chrome":
        service = ChromeService(executable_path=TestData.CHROME_EXEC_PATH)
        web_driver = webdriver.Chrome(service=service)
    if request.param == "firefox":
        service = FirefoxService(executable_path=TestData.FIREFOX_EXEC_PATH)
        web_driver = webdriver.Firefox(service=service)
    web_driver.delete_all_cookies()
    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield web_driver
    web_driver.quit()
