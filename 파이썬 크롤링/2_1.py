import requests
from bs4 import BeautifulSoup
import pyautogui as pg

url = "https://www.melon.com/chart/index.htm"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"} 
response = requests.get(url, headers=header)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
else : 
    print(response.status_code)

m = pg.prompt("검색어를 입력하세요")

a = soup.select('#lst50 > td:nth-child(2) > div > span.rank')
b = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
c = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a')

a1 = soup.select('#lst100 > td:nth-child(2) > div > span.rank')
b1 = soup.select('#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
c1 = soup.select('#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
for i,j,k in zip(a,b,c):
    if m == i.text:
        print(f"Rank : {i.text} / title : {j.text} / name : {k.text}")
for i,j,k in zip(a1,b1,c1):
    if m == i.text:
        print(f"Rank : {i.text} / title : {j.text} / name : {k.text}")