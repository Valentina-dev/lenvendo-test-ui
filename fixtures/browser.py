import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import DOMAIN, CHROMEDRIVER_PATH


@pytest.fixture
def browser():
    service = Service(CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=service)
    browser.get(url=DOMAIN)
    browser.set_window_size(1920, 1080)
    browser.maximize_window()
    yield browser
    browser.quit()
