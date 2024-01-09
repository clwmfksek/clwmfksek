import requests
from bs4 import BeautifulSoup
import re

URL_get = "https://www.melon.com/chart/index.htm"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
header = {'User-Agent':user_agent}

response = requests.get(URL_get, headers=header)
soup = BeautifulSoup(response.text,'html.parser')

p = re.compile('아이.') 

name = []
s = []

for i in soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a'): #css selector 사용
    name.append(i.text)
for i in soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a'): #css selector 사용
    s.append(i.text)

for i,j in zip(name,s):
    if p.search(j):
        print(i,j)