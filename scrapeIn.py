from selenium import webdriver
import random
from parsel import Selector
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

options.page_load_strategy = 'normal'
driver=webdriver.Chrome(options=options)


def login():
    driver.get("https://www.linkedin.com/login")
    driver.maximize_window()

    #Enter the username manually

    username=driver.find_element(By.ID,'username')
    #time.sleep(1)
    username.send_keys('1si20cs020@sit.ac.in')

    #Enter the password manually

    password=driver.find_element(By.ID,'password')
    #time.sleep(1)
    password.send_keys('save@21myPWD')


    #Press Enter 
    driver.find_element(By.XPATH,'//*[@type="submit"]').click()

    time.sleep(3)


"""def getEmployeeUrl():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source)

    visibleEmployeesLink = []
    visibleEmployees = soup.find_all('a', class_='app-aware-link')
    for profile in visibleEmployees:
        if profile.get('href').split('/')[3] ==  'in':
            visibleEmployeesLink.append(profile.get('href'))
    return visibleEmployeesLink"""

def posts():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(2.5,4.5))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(2.5,4.5))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(2.5,4.5))
    soup=BeautifulSoup(driver.page_source,features='lxml')


    all_post=soup.find_all('div',class_='update-components-text relative feed-shared-update-v2__commentary')
    #all_post=soup.find_all('span',class_='break-words')
    for post in all_post:
        print(post.text.rstrip())
    
    
    print("\n")


"""def returnProfileInfo(employeeLink):
    url = employeeLink
    driver.get(url)
    time.sleep(2)
    source = BeautifulSoup(driver.page_source, "html.parser")
    profile = []
    info = source.find('div', class_='mt2 relative')
    name = info.find('h1', class_='text-heading-xlarge inline t-24 v-align-middle break-words').get_text().strip()
    title = info.find('div', class_='text-body-medium break-words').get_text().lstrip().strip()
    profile.append(name)
    profile.append(title)
    return profile"""
    







if __name__ == "__main__":
    login()

    posts()
    """employees = {}
    searchable = getEmployeeUrl()
    for employee in searchable:
        time.sleep(random.uniform(2.5,4.5))
        employees[employee] = returnProfileInfo(employee)"""
    print("\n")
    print("\n")

    #print(employees)



















"""driver.get("https://www.linkedin.com/search/results/all/?keywords=%23layoffs&origin=GLOBAL_SEARCH_HEADER&sid=ox)")

page=Selector(text=driver.page_source)

name=driver.find_element(By.XPATH,'//*[starts-with(@class,"app-aware-link")]/text()').text()
name=name.strip()
print(name)
"""

#Search for post having keyword 'layoffs'

"""search=driver.find_element(By.XPATH,'//*[@placeholder="Search"]')
search.send_keys('#layoffs')
search.send_keys(u'\ue007')

time.sleep(random.uniform(2.5,4.5))"""




#r = requests.get('https://www.linkedin.com/search/results/all/?keywords=%23layoffs&origin=GLOBAL_SEARCH_HEADER&sid=pFq')
"""r=requests.get('https://www.linkedin.com/feed/hashtag/layoffs/')

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.prettify())"""



"""
posts=soup.find_all('div',class_="relative")

for post in posts:
    name=post.find('span',dir="ltr")
    print(name)"""






































"""time.sleep(10)

r = requests.get('https://www.linkedin.com/search/results/all/?keywords=%23layoffs&origin=GLOBAL_SEARCH_HEADER&sid=pFq')


# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

#print(soup.prettify())


print(soup.find('div',class_="page"))"""





"""for row in table.find('span',attrs={'aria-hidden':'true'}):
    print(row.span.text)"""




#Scroll the web page
# 5 Post per Scroll
"""last_height=driver.execute_script("return document.body.scrollHeight")

for scroll in range (10):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    time.sleep(5)

    new_height=driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height=new_height"""