from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory
# from seleniumpagefactory.pagefactory import PageFactory



class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        
    locators = {
        'username':('CSS',"#username input"),
        'password':('CSS',"#password input"),
        'login_btn':('ID',"login-btn")
    }
    locators={
        'search_box_filed': ('name', "search"),
        'search_button': ('xpath', "//button[@class='btn btn-default btn-lg']")
    }
    def enter_product_into_search_box(self, product_name):
        self.search_box_filed.click()
        self.search_box_filed.clear()
        self.search_box_filed.set_text(product_name)
        
    def click_search_button(self):
        self.search_button.click()
        