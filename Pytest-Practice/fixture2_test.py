# import pytest
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions

# @pytest.mark.usefixtures("setup_and_tear_down")
# class TestSearch:
    
#     @pytest.mark.parametrize('search_item',[('selenium'),('pytest'),('selenium locators')])
#     def test_google_search(self,search_item):
#         self.driver.find_element(By.NAME,value="q").send_keys(search_item)
#         time.sleep(3)
#         # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "gNO89b"))).click()
#         self.driver.find_element(By.CLASS_NAME,value="gNO89b").click()
#         time.sleep(3)



