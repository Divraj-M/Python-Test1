import pytest
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from Utilities import consolelog

class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

        self.username = (By.XPATH, "//input[@placeholder='Username']")
        self.password = (By.XPATH, "//input[@placeholder='Password']")
        self.btn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
        self.error_message = (By.XPATH, "//p[contains(@class,'oxd-text oxd-text--p oxd-alert-content-text')]")
        self.dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.logout = (By.XPATH, "//a[contains(@href,'logout')]")

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.btn).click()

    def error(self):
        return self.driver.find_element(*self.error_message).text
    def click_dropdown(self):
        self.driver.find_element(*self.dropdown).click()
    def click_logout(self):
        self.driver.find_element(*self.logout).click()

    
