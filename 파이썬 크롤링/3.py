# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# 실행경로와 드라이버 객체 생성
driver = webdriver.Chrome()
driver.get('http://capszzang.gq/')
time.sleep(2)
driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[6]/a').click() #로그인 창 클릭
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="user_id"]').send_keys('test1234') #아이디 입력
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('12345678') #패스워드 입력
driver.find_element(
    By.XPATH, '/html/body/section[2]/div/div/div/form/div[3]/button').click()  # 로그인 버튼 클릭
time.sleep(1)
try: #예외처리
    result = driver.switch_to.alert #alert창으로 전환
    result.accept() #alert 확인 버튼 클릭
except:
    pass
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[1]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="top-bar"]/div/nav/div/ul/li[1]/div/ul/li[4]/a').click()
time.sleep(1)
a = driver.find_element(By.XPATH,'/html/body/section[2]/div').text.split("1. 현재 36.5기 집행부 소개")
for i in a[2].split("\n"):
    if i == "2. 집행부가 하는 일":
        break
    print(i)