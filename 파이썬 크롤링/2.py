import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"} 
response = requests.get(url, headers=header)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
else : 
    print(response.status_code)

for j in soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a'):
    print(j.text)
for j in soup.select('#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a'):
    print(j.text)