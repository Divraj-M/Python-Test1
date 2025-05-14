from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory
# from seleniumpagefactory.pagefactory import PageFactory
# 


class SearchPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver


    locators = {
        'display_status_of_valid_products': ('xpath', "//a[contains(text(),'HP LP3065')]")
    }
    
        
    def display_status_of_valid_product(self):
        display_product = self.display_status_of_valid_products.get_text()
        assert display_product == "HP LP3065"