import pytest
import time
from pages.LoginPage import LoginPage
from Utilities.ReadExcel import get_test_data
from Utilities import consolelog

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    @pytest.mark.parametrize("username,password,expected_result", get_test_data("C:\\Users\\Lenovo\\Desktop\\Python-Test1\\Oranges\\Utilities\\loginData.xlsx", "login"))
    def test_login(self, username, password, expected_result):
        log=consolelog.get_logger()
        login_page = LoginPage(self.driver)
        log.info("login entered")  
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        log.info("login clicked")
        time.sleep(3)
        
        

        if expected_result== "valid":
            url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
            assert url==self.driver.current_url

        else:
            time.sleep(2)
            assert "Invalid credentials" in login_page.error()