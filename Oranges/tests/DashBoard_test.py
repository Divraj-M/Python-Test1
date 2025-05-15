import pytest
import time
from pages.LoginPage import LoginPage
from pages.DashBoardPage import DashboardPage
from Utilities.ReadExcel import get_test_data
from Utilities import consolelog

@pytest.mark.usefixtures("setup_and_teardown")
class TestDashBoard:
    @pytest.mark.parametrize("username,password,expected_result", get_test_data("C:\\Users\\Lenovo\\Desktop\\Orange-Python\\Oranges\\Utilities\\loginData.xlsx", "login"))
    def test_DashBoard(self, username, password, expected_result):
        if(expected_result == "valid"):
            log=consolelog.get_consolelog()
            login_page = LoginPage(self.driver) 
            log.info("login entered")
            
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login()
            log.info("login clicked")
            time.sleep(3)
        
            dashboard_page = DashboardPage(self.driver)
            log.info("Dashboard page opened")
            assert dashboard_page.is_assign_leave_displayed()
            assert dashboard_page.is_apply_leave_displayed()
            
        