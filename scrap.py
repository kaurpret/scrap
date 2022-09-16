from selenium import webdriver  
from bs4 import *
import time  
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import pandas as pd
e=[]
e1=[]
e2=[]
e3=[]
e4=[]
e5=[]
e6=[]
e7=[]
e8=[]
e9=[]
n=int(input('Enter the no. of pages that yu want to scrap : '))
print("sample test case started") 
ser = Service("E:\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get_cookies()
# driver.get('https://www.upwork.com/nx/jobs/search/?q=all&sort=recency')
for page in range(n):
   driver.get('https://www.upwork.com/nx/jobs/search/?from_recent_search=true&q=all%20jobs&sort=recency&page='+str(page))
   cookie=driver.find_element('xpath','//button[@id="onetrust-pc-btn-handler"]')
   time.sleep(2)
   cookie.click()
   cookie1=driver.find_element('xpath','//button[@id="accept-recommended-btn-handler"]')
   time.sleep(2)
   cookie1.click()
   content = driver.page_source
   soup = BeautifulSoup(content)
   a=soup.find_all('h4',class_='my-0 p-sm-right job-tile-title')
   b=soup.find_all('div',class_='up-line-clamp-v2 clamped')
   c=soup.find_all('div',class_='up-skill-wrapper')
   d=soup.find_all('small',class_='d-none d-lg-inline-flex text-muted')
   e=soup.find_all('strong',class_='text-muted')
   f=soup.find_all('span', attrs={'data-test' : 'budget'})
   g=soup.find_all('span', attrs={'data-test' : 'contractor-tier'})
   h=soup.find_all('span', attrs={'data-test' : 'posted-on'})
   i=soup.find_all('span', attrs={'data-test' : 'proposals'})
   j=soup.find_all('span', attrs={'data-test' : 'connect-price'})
   
   for i in a:
      e.append(i.text)
   for j in b:
      e1.append(j.text)
   for j in c:
      e2.append(j.text)
   for j in d:
      e3.append(j.text)
   for j in e:
      e4.append(j)
   for j in f:
      e5.append(j.text)
   for j in g:
      e6.append(j.text)
   for j in h:
      e7.append(j.text)
   for j in i:
      e8.append(j.text)
   for k in j:
      e9.append(k.text)
   
   time.sleep(1)  
driver.close()  

data={'Job title':e,'Budget':e5,'Skills':e2,'Experience':e6,'Posted on':e7,'Proposals':e8,'Payment sttaus':e4,'Client country':e3,'Connects':e9,' Job description':e1}
df=pd.DataFrame(data)
# print(df)
df.to_csv('data.csv')
print("****** sample test case successfully completed ********")  