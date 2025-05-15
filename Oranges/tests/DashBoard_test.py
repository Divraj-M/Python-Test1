import pytest
import time
from pages.LoginPage import LoginPage
from pages.DashBoardPage import DashboardPage
from Utilities.ReadExcel import get_test_data
from Utilities import consolelog

test_data = get_test_data("C:\\Users\\Lenovo\\Desktop\\Python-Test1\\Oranges\\Utilities\\loginData.xlsx", "login")
@pytest.mark.usefixtures("setup_and_teardown")
class TestDashBoard:
    def test_DashBoard(self):
        username,password,exp=test_data[0]
        log=consolelog.get_logger()
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
            
        