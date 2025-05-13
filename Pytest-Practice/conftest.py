import pytest
import read_config
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup_and_tear_down(request):
    browser = read_config.get_config("basic info","browser")
    driver = None
    if browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    else:
        print("Invalid browser name")
    driver.maximize_window()
    driver.implicitly_wait(10)
    app_url = read_config.get_config("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
    
    


# @pytest.fixture(params=["chrome","firefox","edge"],scope="class")
# def setup_and_tear_down(request):
#     if request.param=="chrome":
#         driver=webdriver.Chrome()
#     elif request.param=="firefox":
#         driver=webdriver.Firefox()
#     elif request.param=="edge":
#         driver=webdriver.Edge()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://www.google.co.in/")
#     request.cls.driver = driver
#     def teardown():
#         driver.quit()

#     request.addfinalizer(teardown)