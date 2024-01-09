import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://finance.naver.com/sise/lastsearch2.naver"
driver.get(url)
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"} 
response = requests.get(url, headers=header)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
else : 
    print(response.status_code)

rank = []
name = []
now = []
updown = []
per = []
n = []

rank1 = []
name1 = []
now1 = []
updown1 = []
per1 = []
for i in range(3,48):
    rank1.append(driver.find_elements(By.XPATH,f"""//*[@id="contentarea"]/div[3]/table/tbody/tr[{i}]/td[1]"""))
    name1.append(driver.find_elements(By.XPATH,f"""//*[@id="contentarea"]/div[3]/table/tbody/tr[{i}]/td[2]/a"""))
    now1.append(driver.find_elements(By.XPATH,f"""//*[@id="contentarea"]/div[3]/table/tbody/tr[{i}]/td[4]"""))
    updown1.append(driver.find_elements(By.XPATH,f"""//*[@id="contentarea"]/div[3]/table/tbody/tr[{i}]/td[6]/span"""))
    per1.append(driver.find_elements(By.XPATH,f"""//*[@id="contentarea"]/div[3]/table/tbody/tr[{i}]/td[11]"""))

for i in range(len(rank1)):
    try :
        print(f"Rank : {rank1[i][0].text} / name : {name1[i][0].text} / now : {now1[i][0].text} / updown : {updown1[i][0].text} / per : {per1[i][0].text}")
    except:
        pass

for i in soup.select(f'#contentarea > div.box_type_l > table > tr td.no'):
    rank.append(i.text)
for i in soup.select(f'#contentarea > div.box_type_l > table > tr td a'):
    name.append(i.text)
for i in soup.select(f'#contentarea > div.box_type_l > table > tr td:nth-child(4)'):
    now.append(i.text)
for i in soup.select(f'#contentarea > div.box_type_l > table > tr td:nth-child(6)'):
    updown.append(i.text.strip("\n").strip("\t").rstrip("\n"))
for i in soup.select(f'#contentarea > div.box_type_l > table > tr td:nth-child(11)'):
    per.append(i.text)
        

for i in range(len(rank)):
    print(f"Rank : {rank[i]} / name : {name[i]} / now : {now[i]} / updown : {updown[i]} / per : {per[i]}")
