import pytest
from selenium import webdriver


@pytest.yield_fixture(scope='session')
def driver_fixture():
    path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=path)
    browser.set_window_position(-2000, 0)
    yield browser
    browser.quit()
