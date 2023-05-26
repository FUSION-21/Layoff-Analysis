from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

options.page_load_strategy = 'normal'
driver=webdriver.Edge(options=options)
driver.get("https://www.linkedin.com/login")
driver.maximize_window()

#Enter the username manually

username=driver.find_element(By.ID,'username')
time.sleep(1)
username.send_keys('1si20cs020@sit.ac.in')

#Enter the password manually

password=driver.find_element(By.ID,'password')
time.sleep(1)
password.send_keys('save@21myPWD')

time.sleep(1)

#Press Enter 
driver.find_element(By.XPATH,'//*[@type="submit"]').click()

time.sleep(2)


#Search for post having keyword 'layoffs'
"""search=driver.find_element(By.XPATH,'//*[@placeholder="Search"]')
search.send_keys('#layoffs')
search.send_keys(u'\ue007')"""

time.sleep(3)


#Scroll the web page
# 5 Post per Scroll
last_height=driver.execute_script("return document.body.scrollHeight")

for scroll in range (10):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    time.sleep(5)

    new_height=driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height=new_height

#r = requests.get('https://www.linkedin.com/feed')

# check status code for response received
# success code - 200
#print(r)

# Parsing the HTML
#soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())






