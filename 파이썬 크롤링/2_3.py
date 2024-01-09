import requests
from bs4 import BeautifulSoup
import pyautogui as pg

url = "https://finance.naver.com/sise/lastsearch2.naver"
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
