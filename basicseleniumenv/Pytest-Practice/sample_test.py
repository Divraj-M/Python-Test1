import pytest

# def test_one():
#     print("in the one method")
# def test_sample1():
#     print("in the sample1 test")
# def test_two():
#     print("in the test two")

# @pytest.mark.xfail(reason="expected pass")
# @pytest.mark.smoke    
# @pytest.mark.regression  
# def test_c():
#     a=10
#     b=10
#     assert a==b
    
# @pytest.mark.regression   
# def test_a():
#     print("hiii")
#     a="Divraj"
#     b="Divraj"
#     assert a.__eq__(b)
# @pytest.mark.xfail(reason="expected fail")
# @pytest.mark.regression   
# def test_d():
#     print("hiii")
#     a="divraj"
#     b="Divraj"
#     assert a.__eq__(b)

# # @pytest.mark.skipif(reason="skipped the a<b metod")
# @pytest.mark.regression 
# @pytest.mark.smoke
# def test_b():
#     a=5
#     b=10
#     assert a<b

# @pytest.mark.parametrize("test_input,expected",[(1,3),(3,6),(5,7)])
# def test_testing1(test_input,expected):
#     assert test_input + 2 == expected


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# @pytest.mark.parametrize('search_item',[('selenium'),('pytest'),('selenium locators')])

# def test_google_search(search_item):
#     # opt=Options()
#     # opt.add_argument("")
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.google.co.in/")
#     driver.find_element(By.NAME,value="q").send_keys(search_item)
#     time.sleep(6)
#     driver.find_element(By.CLASS_NAME,value="gNO89b").click()
#     time.sleep(6)
#     driver.quit()


@pytest.mark.parametrize('browser',[('Chrome'),('FireFox')])
@pytest.mark.parametrize('url',[('https://www.amazon.com/'),('https://www.flipkart.com/')])
def test_prectise(browser,url):
    if(browser.__eq__("Chrome")):
        driver=webdriver.Chrome()
    else:
        driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    print("the title is",driver.title)
    driver.quit()



# @pytest.fixture()
# def test_setup_and_tear_down():
#     global driver
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://tutorialsninja.com/demo/")
#     yield
#     driver.quit()


# def test_HP(test_setup_and_tear_down):
#     driver.find_element(By.XPATH,value="//input[@class='form-control input-lg']").send_keys("HP")
#     driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
#     exp="Search - HP" 
#     assert driver.find_element(By.XPATH,value="//div[@class='col-sm-12']//h1").text.__eq__(exp)

# def test_Honda(test_setup_and_tear_down):
#     driver.find_element(By.XPATH,value="//input[@class='form-control input-lg']").send_keys("Honda")
#     driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
#     exp="There is no product that matches the search criteria."
#     assert driver.find_element(By.XPATH,value="//input[@class='btn btn-primary']//following-sibling::p").text.__eq__(exp)

# def test_empty(test_setup_and_tear_down):
#     driver.find_element(By.XPATH,value="//input[@class='form-control input-lg']").send_keys("")
#     driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
#     exp="There is no product that matches the search criteria."
#     assert driver.find_element(By.XPATH,value="//input[@class='btn btn-primary']//following-sibling::p").text.__eq__(exp)
    
    
    