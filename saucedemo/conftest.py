import pytest
import read_config
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup_and_tear_down(request):
    browser = read_config.get_config("basic info","browser")
    driver = None
    if browser.__eq__("Edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("Firefox"):
        dri
    else:
        print("Invalid browser name")
    driver.maximize_window()
    driver.implicitly_wait(10)
    app_url = read_config.get_config("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
    