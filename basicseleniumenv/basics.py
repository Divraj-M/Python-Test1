import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
# driver.maximize_window()
# # driver.get("https://www.google.com/")
# url="https://www.google.com/"
# driver.get(url)
# print(driver.title)
# print(driver.current_url)
# # print(driver.page_source)
# time.sleep(5)
# driver.close()
# url="https://www.flipkart.com/"
# driver.get(url)
# print("\npage title:", driver.title,"\npage title length:", len(driver.title))
# link=driver.current_url
# if(link==url):
#     print("\nURL is correct")
# else:
#     print("\nURL is incorrect")
# print("\npage source is",driver.page_source,"page source length is", len(driver.page_source))
# driver.close()


# driver.get("https://www.google.com/")
# time.sleep(5)
# driver.get("https://www.flipkart.com/")
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()

# driver.get("https://www.toolsqa.com/selenium-training/")
# a=driver.find_element(By.XPATH,value= """//a[@class="btn btn-primary-shadow btn-block"]""")
# print(a.size)
# print(a.location)
# a.click()
# driver.save_screenshot("screenshot.png")
# driver.back()
# driver.forward()
# driver.refresh()
# driver.close()


# driver.get("https://www.google.com/")
# act="Google"
# exp=driver.title
# if(act==exp):
#     print("title is same and verified")
# else:
#     print("title is not same ")
# searchbox=driver.find_element(By.XPATH,value= """//div[@class="YacQv"]//following-sibling::textarea""")
# print("search box is enabled :",searchbox.is_enabled())
# searchbox.send_keys("selenium")
# button=driver.find_element(By.XPATH,value= """//input[@value="Google Search"]""")
# print("button is enabled :",button.is_enabled())
# driver.implicitly_wait(10)
# button.click()


# driver.get("https://selenium08.blogspot.com/2019/07/check-box-and-radio-buttons.html")
# red=driver.find_element(By.XPATH,value= """//div[@class="post-body entry-content float-container"]//div//input[@name="color" and @value="red"]""")
# if(red.is_enabled()):
#     print("red checkbox is enabled")
# else:
#     print("red checkbox is not enabled")
# if(red.is_selected()):
#     print("red checkbox is selected")
# else:
#     print("red checkbox is not selected")
# opera=driver.find_element(By.XPATH,value= """//input[@value="Opera"]""").is_selected()
# print("opera is selected:", opera)


import re
# text="Alan Turing was a pioneer of theoretical computer science and artificial intelligence. He was born on 23 June 1912 in Maida vale, London"
# res=re.search("^Alan.*f$",text)
# if(res):
#     print("match found")
# else:
#     print("match not found")
    
# findalll=re.findall("was",text)
# print("findall:", format(findalll))
# res1=re.search("computer",text)
# print("position of start and end of the string:", res1.span())
# splits=re.split("was",text)
# print("splits:", splits)
# res2=re.split("^p.*r$",text)
# print(res2)
# res3=re.sub("^w+s$","practical",text)
# print("replace:", res3)
# text="Alan was born on 23 June 1912 in London"
# res=re.findall("\AAlan",text)
# print("findall:", format(res))
# res1=re.findall(r"\bLon",text)
# print("findall:", format(res1))
# res2=re.findall("\s",text)
# print("findall:", format(res2))
# res2=re.findall("\S",text)
# print("findall:", format(res2))
# res2=re.findall("\W",text)
# print("findall:", format(res2))
# res2=re.findall("London\Z",text)
# print("findall:", format(res2))

# import re
# email=r"\b[A-Za-z0-9_%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
# textemail="2k21cse022@kiot.ac.in"

# email1=re.findall(email,textemail)
# print("email:", format(email1))
