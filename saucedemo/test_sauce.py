import read_config
import pytest
import time
import excelReader
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_tear_down")
@pytest.mark.parametrize("username,password", excelReader.get_data("C:\\Users\\Lenovo\\Desktop\\Python-Test1\\saucedemo\\sauceBook.xlsx", "Sheet1"))
class TestLogin:
    def test_validlogin(self,username,password):
        self.driver.find_element(By.ID,"user-name").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID,"password").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        if(username=="locked_out_user"):
            exp="Sorry, this user has been locked out."
            assert exp in self.driver.find_element(By.XPATH,value="//h3[@data-test='error']").text   
        else:
            exp="Products"
            assert self.driver.find_element(By.XPATH,value="//div[@class='product_label']").text.__eq__(exp)
        self.driver.quit()