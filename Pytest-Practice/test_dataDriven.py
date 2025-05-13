import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import excelReader
import time

@pytest.mark.parametrize("username,password", excelReader.get_data("ExcelFiles/loginData.xlsx", "Sheet1"))
class TestLogin:
    def test_validlogin(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(5)
        self.driver.find_element(By.ID, value="login2").click()
        time.sleep(5)
        self.driver.find_element(By.ID, value="loginusername").send_keys(username)
        self.driver.find_element(By.ID, value="loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, value="//button[contains(text(),'Log in')]").click()
        time.sleep(5)
        u=username
        if(u!="admi"):
            assert self.driver.find_element(By.ID, value="logout2").is_displayed()
        else:
            exp="Wrong password."
            assert self.driver.switch_to.alert.text.__eq__(exp)
        self.driver.quit()
            
        
