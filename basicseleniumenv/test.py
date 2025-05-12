from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
opt=Options()
opt.add_argument("--headless")
driver=webdriver.Chrome(options=opt);
driver.maximize_window()
driver.get("https://google.co.in")
driver.implicitly_wait(10)




