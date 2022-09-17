from selenium import webdriver  
from bs4 import *
import time  
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import pandas as pd
n=int(input('Enter the no. of pages that you want to scrap : '))
print("sample test case started") 
with open('data.csv','w') as file:
    file.write('Job_title ; Rate ; Experience ; Duration ; Posted_on ; Description ; Skills ; Proposals ; Connects ; Country_name \n')
ser = Service("E:\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get('https://www.upwork.com/nx/jobs/search/?from_recent_search=true&q=all%20jobs&sort=recency')
cookie=driver.find_element('xpath','//*[@id="onetrust-pc-btn-handler"]')
cookie.click()
cookie1=driver.find_element('xpath','//*[@id="onetrust-pc-sdk"]/div[3]/div[1]/button[2]')
cookie1.click()
for i in range(n):
    title=driver.find_element('xpath','//*[@id="job-1570995802078752768"]/div[1]/div[1]/h4"]')
    rate=driver.find_element('xpath','//*[@id="job-1570977202223652864"]/div[2]/div[1]/small/strong')
    ex=driver.find_element('xpath','//*[@id="job-1570977202223652864"]/div[2]/div[1]/small/span[1]/span')
    dur=driver.find_element('xpath','//*[@id="job-1570977202223652864"]/div[2]/div[1]/small/span[2]/span/span[2]')
    post=driver.find_element('xpath','//*[@id="job-1570977202223652864"]/div[2]/div[1]/small/span[3]/span/span')
    desc=driver.find_element('xpath','//*[@id="up-line-clamp-v2-21"]/span')
    skill=driver.find_element('xpath','//*[@id="job-1570977202223652864"]/div[2]/div[3]/div/div[2]')
    prop=driver.find_element('xpath','//*[@id="job-1570977202223652864"]/div[2]/div[4]/small/strong')
    con=driver.find_element('xpath','//*[@id="job-1570977202223652864"]/div[2]/div[5]/small[4]/strong')
    coun=driver.find_element('xpath','//*[@id="job-1570977202223652864"]/div[2]/div[5]/small[3]/strong')
    with open('data.csv','a') as file:
        for i in range(len(title)):
           file.write(title[i].text + ';' + rate[i].text + ';' + ex[i].text + ';' + dur[i].text + ';'+ post[i].text + ';'+ desc[i].text + ';'+ skill[i].text + ';'+ prop[i].text + ';'+ con[i].text + ';'+ coun[i].text + "\n"  )
        next=driver.find_element('xpath','//*[@id="main"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/nav/ul/li[9]/button')
        next.click()
    file.close()
driver.close()
print("****** sample test case successfully completed ********")  