import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# parent_windowID=driver.current_window_handle

# driver.find_element(By.LINK_TEXT,value="Open a popup window").click()
# WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
# windowID=driver.window_handles
# print(parent_windowID)
# print(windowID)

# for w in windowID:
#     driver.switch_to.window(w)
#     driver.maximize_window()
#     if(driver.title.__eq__("New Window")):
#         time.sleep(5)
#         window_text=driver.find_element(By.XPATH,value="//div[@class='example']//h3").text
#         print(window_text)
#         driver.close()
#         break
# time.sleep(5)
# driver.switch_to.window(parent_windowID)
# a=driver.find_elements(By.XPATH,value="//*[@id='header-inner']//div[1]//h1")
# for j in a:
#     print(j.text)
# driver.get("https://letcode.in/frame")
# time.sleep(5)
# driver.switch_to.frame("firstFr")
# driver.find_element(By.NAME,value="fname").send_keys("Divraj")
# driver.find_element(By.NAME,value="lname").send_keys("M")
# time.sleep(5)

# childframe=driver.find_element(By.XPATH,value="//div[@class='container has-text-centered mb-4 mt-6']//iframe")
# driver.switch_to.frame(childframe)
# driver.find_element(By.NAME,value="email").send_keys("2k21cse022@kiot.ac.in")
# time.sleep(5)

# driver.switch_to.parent_frame()
# driver.find_element(By.NAME,value="lname").clear()
# time.sleep(5)





# driver.get("https://omayo.blogspot.com/")
# # frame1=driver.find_element(By.XPATH,value="//div[@id='navbar-iframe-container'']//iframe")
# driver.switch_to.frame("navbar-iframe")
# time.sleep(5)
# driver.find_element(By.XPATH,value="//input[@name='q' and @class='ENqPLc']").send_keys("Divraj")
# time.sleep(5)
# driver.find_element(By.XPATH,value="//input[@name='q' and @class='ENqPLc']//parent::td//following-sibling::td//span").click()
# time.sleep(5)
# driver.switch_to.default_content()
# t1=driver.find_element(By.CLASS_NAME,value="status-msg-body").text
# print(t1)


# driver.get("https://omayo.blogspot.com/")
# select_element=driver.find_element(By.ID,value="drop1")
# select=Select(select_element)

# dropdownopt=select.options
# print(len(dropdownopt))
# for opt in dropdownopt:
#     print(opt.text)
# select.select_by_visible_text("doc 2")
# # select.select_by_index(3)
# time.sleep(5)
# # select.deselect_by_index(3)
# select_element.send_keys("doc 1")
# time.sleep(5)
# driver.execute_script("arguments[0].value='ghi';",select_element)
# time.sleep(5)
# opt1=driver.find_element(By.ID,value="ironman4")
# actions=ActionChains(driver)
# # actions.key_down(Keys.CONTROL).click(select_element).perform()
# actions.key_down(Keys.CONTROL).click(select_element).key_down(Keys.DOWN).click().key_up(Keys.ENTER).click().perform()
# time.sleep(5)


# driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.XPATH,value="//a[contains(text(),'JavaScript Alerts')]").click()
# driver.find_element(By.XPATH,value="//button[contains(text(),'Click for JS Alert')]").click()
# info_alert=driver.switch_to.alert
# time.sleep(5)
# print(info_alert.text)
# info_alert.accept
# time.sleep(5)
# driver.find_element(By.XPATH,value="//button[contains(text(),'Click for JS Confirm')]").click()
# info_alert=driver.switch_to.alert
# info_alert.accept
# time.sleep(5)
# driver.find_element(By.XPATH,value="//button[contains(text(),'Click for JS Prompt')]").click()
# info_alert=driver.switch_to.alert
# info_alert.send_keys("Hello")
# time.sleep(5)
# info_alert.accept
# time.sleep(5)


# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.find_element(By.XPATH,value="//button[text()='Click for JS Alert']").click()
# alert=driver.switch_to.alert
# time.sleep(5)
# print(alert.text)
# alert.accept()
# driver.find_element(By.XPATH,value="//button[text()='Click for JS Confirm']").click()
# alert=driver.switch_to.alert
# time.sleep(5)
# print(alert.text)
# alert.accept()
# driver.find_element(By.XPATH,value="//button[text()='Click for JS Prompt']").click()
# alert=driver.switch_to.alert
# print(alert.text)
# alert.send_keys("Divraj")
# alert.accept()
# time.sleep(5)


# driver.get("https://omayo.blogspot.com/")
# driver.execute_script("alert('Divraj');")
# time.sleep(5)

# def click_method(driver, by, value, timeout=10):
#     try:
#         element = WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable((by, value)))
#         driver.execute_script("arguments[0].click()", element)
#     except Exception as e:
#         print(f"click failed:{e}")
# driver.get("https://omayo.blogspot.com/")

# click_method(driver, By.ID, "alert1")

# a = driver.switch_to.alert
# time.sleep(5)
# a.accept()
# time.sleep(5)

# driver.quit()

# def flash_element(element):
#     for i in range(1,30):
#         driver.execute_script("arguments[0].style.background='red';", element)
#         time.sleep(0.3)
#         default_color = element.value_of_css_property("background-color")
#         driver.execute_script("arguments[0].style.background='"+default_color+"';", element)
#         time.sleep(0.3)
    


# driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
# element=driver.find_element(By.XPATH,value="//input[@type='submit']")
# flash_element(element)



driver.get("https://omayo.blogspot.com/")
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(5)
driver.execute_script("window.scrollBy(0, -500);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("history.go(0);")
time.sleep(5)