# from selenium.webdriver.support.relative_locator import locate_with
# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# # def setup_function(function):
# #     global driver
# #     driver = webdriver.Chrome()
# #     driver.maximize_window()
# #     driver.implicitly_wait(10)
# #     driver.get("https://www.google.co.in/")


# # def teardown_function(function):
# #     driver.quit()


# # @pytest.mark.parametrize('search_item', ['selenium', 'pytest', 'selenium locators'])
# # def test_google_search(search_item):
# #     driver.find_element(By.NAME, value="q").send_keys(search_item)
# #     time.sleep(2)
# #     driver.find_element(By.NAME, value="btnK").click()
# #     time.sleep(3)
    


# def setup_function(function):
#     global driver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://parabank.parasoft.com/parabank/index.htm")


# def teardown_function(function):
#     driver.quit()
    
# def test_parabank():
#     driver.find_element(By.LINK_TEXT, value = "Register").click()
#     driver.find_element(By.XPATH,value="//input[@id='customer.firstName']").send_keys("Divraj")
#     driver.find_element(By.NAME, value = "customer.lastName").send_keys("M")
#     driver.find_element(By.NAME, value = "customer.address.street").send_keys("1")
#     driver.find_element(By.NAME, value = "customer.address.city").send_keys("india")
#     driver.find_element(By.NAME, value = "customer.address.state").send_keys("TN")
#     driver.find_element(By.NAME, value = "customer.address.zipCode").send_keys("637505")
#     driver.find_element(By.NAME, value = "customer.phoneNumber").send_keys("1234567890")
#     driver.find_element(By.NAME, value = "customer.ssn").send_keys("12312")
#     driver.find_element(By.NAME, value = "customer.username").send_keys("Div123")
#     driver.find_element(By.NAME, value = "customer.password").send_keys("Divraj@123")
#     driver.find_element(By.NAME, value = "repeatedPassword").send_keys("Divraj@123")
#     driver.find_element(By.XPATH, value = "//input[@value='Register']").click()
#     assert driver.title == "ParaBank | Customer Created"
#     time.sleep(5)

# def test_login_page():
#     driver.find_element(By.NAME, value = "username").send_keys("Div123")
#     driver.find_element(By.NAME, value = "password").send_keys("Divra@123")
#     driver.find_element(By.XPATH, value = "//input[@value='Log In']").click()
#     assert driver.find_element(By.XPATH, value = "//div[@id='showOverview']/h1").is_displayed()
#     time.sleep(5)


    


