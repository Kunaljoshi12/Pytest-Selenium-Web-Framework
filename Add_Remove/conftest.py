import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import CHROME_DRIVER_PATH, IMPLICIT_WAIT

@pytest.fixture
def driver():
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT)
    yield driver
    driver.quit()