# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

l = []
# 실행경로와 드라이버 객체 생성
driver = webdriver.Chrome()
for i in range(1,21):
    driver.get(f"https://wikidocs.net/{i}")
    l.append({'url':driver.current_url,'title':driver.title})

print(l)