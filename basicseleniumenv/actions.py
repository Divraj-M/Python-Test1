import time
import requests
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Chrome()
driver.maximize_window()
# actions=ActionChains(driver)
# driver.get("https://tutorialsninja.com/demo/index.php?route=account/login");
# driver.get("https://omayo.blogspot.com/");
# actions=ActionChains(driver);
# blogs=driver.find_element(By.ID,value='blogsmenu')
# actions.move_to_element(blogs).click().perform()
# option2=driver.find_element(By.ID,"//span[text()='SeleniumByArun']")
# actions.click(option2).perform()
# driver.find_element(By.ID,value="input-email").send_keys("abc@gmail.com")
# time.sleep(5)
# driver.find_element(By.ID,value="input-password").send_keys("Divraj@123")
# actions.send_keys(Keys.ENTER).perform()
# time.sleep(5)

# links=driver.find_elements(By.XPATH,value="//div[@id='LinkList1']//a")
# print(len(links))

# for link in links:
#     print(link.get_attribute("href"))
    
# for link in links:
#     actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

# tableplace=driver.find_elements(By.XPATH,value="//table[@id='table1']//td[3]")
# print("the place are:")
# for place in tableplace:
#     print(place.text)
# noofrows=driver.find_elements(By.XPATH,"//table[@id='table1']//tr")
# print("no of rows in table:",len(noofrows))
# noofcols=driver.find_elements(By.XPATH,value="//table[@id='table1']//th")
# print("no of cols in table:",len(noofcols))

# def verifyurl(links):
    
#     try:
#         response=requests.head(links,timeout=5)
#         if (response.status_code==301 or response.status_code==302 or response.status_code==503):
#             print(f"{links} - {response.reason}")
#         else:
#             print(f"{links} - is a broken link")
#     except Exception as e:
#         print(f"{links}- is broken link")

        

# links=driver.find_elements(By.XPATH,value="//div[@id='LinkList1']//a")
# print(len(links))

# for link in links:
#     links1=link.get_attribute("href")
#     verifyurl(links1)
     
# for link in links:
#     actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()


# noofrows=driver.find_elements(By.XPATH,"//table[@id='table1']//tr")
# print("no of rows in table:",len(noofrows))
# rows=len(noofrows)
# noofcols=driver.find_elements(By.XPATH,value="//table[@id='table1']//th")
# print("no of cols in table:",len(noofcols))
# cols=len(noofcols)

# for r in range(1,rows+1):
#     for c in range(1,cols+1):
#         if r==1:
#             data=driver.find_element(By.XPATH,value="//table[@id='table1']//tr["+str(r)+"]//th["+str(c)+"]").text
#             print(data,end=" ")
#         else:
#             data=driver.find_element(By.XPATH,value="//table[@id='table1']//tr["+str(r-1)+"]//td["+str(c)+"]").text
#             print(data,end=" ")
#     print()



driver.get("https://thinking-tester-contact-list.herokuapp.com/")
driver.find_element(By.ID,value="email").send_keys("2k21cse021@kiot.ac.in")
driver.find_element(By.ID,value="password").send_keys("Divraj@123")
driver.find_element(By.ID,value="submit").click()

time.sleep(5)
exp_name="Raj K"
contact_names=driver.find_elements(By.XPATH,value="//table[@id='myTable']//tr/td[2]")
print(len(contact_names))

# for names in contact_names:
#     print(names.text)
# i=1  
# for name in contact_names:
#     if name.text.__eq__(exp_name):
#         act_rowdata=driver.find_elements(By.XPATH,value="//table[@id='myTable']//tr["+str(i)+"]")
#         for actname in act_rowdata:
#             print(actname.text)
#     i=i+1