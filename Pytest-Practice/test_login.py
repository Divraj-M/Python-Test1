import read_config
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_tear_down")
class TestLogin:
    def test_validlogin(self):
        self.driver.find_element(By.ID, value="login2").click()
        username = read_config.get_config("login cred", "user")
        password = read_config.get_config("login cred", "pass")
        self.driver.find_element(By.ID, value="loginusername").send_keys(username)
        self.driver.find_element(By.ID, value="loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, value="//button[contains(text(),'Log in')]").click()
        time.sleep(5)
        assert self.driver.find_element(By.ID, value="logout2").is_displayed()
        