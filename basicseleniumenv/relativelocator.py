# import time
# ct # type: ignore
 # type: ignore
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.relative_locator import locate_with
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.hyrtutorials.com/p/css-selectors-practice.html")
# lastname=driver.find_element(By.XPATH,value="//input[@class='gender']//preceding-sibling::input[@id='lastName']")
# f_name=driver.find_element(locate_with(By.TAG_NAME,"input").above(lastname))
# f_name.send_keys("Divraj")
# gender=driver.find_element(By.XPATH,value="//input[@class='city']//preceding-sibling::input[@class='gender']")
# l_name=driver.find_element(locate_with(By.TAG_NAME,"input").above(gender))
# l_name.send_keys("M")
# g_ender=driver.find_element(locate_with(By.TAG_NAME,"input").below(l_name))
# g_ender.send_keys("M")
# city=driver.find_element(locate_with(By.TAG_NAME,"input").below(gender))
# city.send_keys("india")
# security_answer=driver.find_element(By.XPATH,value="//form[@style='height: auto !important;']//child::input[7]")
# s_question=driver.find_element(locate_with(By.TAG_NAME,"input").above(security_answer))
# s_question.send_keys("where are you from")
# personaldetail=driver.find_element(By.XPATH,value="//select//preceding-sibling::input[@placeholder='Verify your personal details']")
# s_answer=driver.find_element(locate_with(By.TAG_NAME,"input").above(personaldetail))
# s_answer.send_keys("Namakkal")
# p_details=driver.find_element(locate_with(By.TAG_NAME,"input").below(s_answer))
# p_details.send_keys("9025861027")
# button2=driver.find_element(By.XPATH,value="//button[@id='button3']//following-sibling::input[2]")
# time.sleep(5)
# buttonmid=driver.find_element(locate_with(By.TAG_NAME,"input").to_left_of(button2))
# buttonmid.click()
# time.sleep(5)
# button1=driver.find_element(locate_with(By.TAG_NAME,"button").to_right_of(button2))
# button1.click()

import pytesseract
from PIL import Image
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Firefox()
driver.maximize_window()
# driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
# # driver.implicitly_wait(10)
# addtextbox1=driver.find_element(By.ID,"btn1")
# addtextbox1.click()
# # textField1=driver.find_element(By.ID,"txt1")
# textField1=WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.ID,"txt1")))
# textField1.send_keys("Python")

# addtextbox1=driver.find_element(By.ID,"btn2")
# addtextbox1.click()
# # textField=driver.find_element(By.ID,"txt2")
# textField=WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.ID,"txt2")))
# textField.send_keys("selenium")
# textField2=driver.find
# driver.implicitly_wait(10)
driver.get("https://www.zoho.com/signup.html")
driver.delete_all_cookies()
email=driver.find_element(By.XPATH,value="//input[@id='email']")
email.send_keys("Sabra62@gmail.com")
password=driver.find_element(By.XPATH,value="//input[@id='password']")
password.send_keys("Divraj@85233")
phone=driver.find_element(By.XPATH,value="//input[@id='rmobile']")
phone.send_keys("7428580614")
image_path = r"C:\Users\Lenovo\Desktop\Python-Selenium\basicseleniumenv\screenshot1.png"
image = Image.open(image_path)
text = pytesseract.image_to_string(image, lang='eng', config='--psm 3')
print(text)
terms=driver.find_element(By.CLASS_NAME,value="unchecked")
terms.click()
capcha=driver.find_element(By.CLASS_NAME,value="za-captcha")
capcha.screenshot_as_png("screenshot1.png")

signup=driver.find_element(By.XPATH,value="//input[@id='signupbtn']")
signup.click()
time.sleep(5)