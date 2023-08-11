# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import sys
# 실행경로와 드라이버 객체 생성

a = int(input("1 : 글에서 검색하기, 2 : 댓글에서 검색하기"))
b = input("어떤 걸 검색하실 건가요? : ")
driver = webdriver.Chrome()
driver.get("https://cafe.naver.com/joonggonara/1005170350")

def read(t):
    c = t.split("\n")
    for i in c :
        d=i.split()
        for j in d:
            if j == b: print(i)

time.sleep(3)
if a == 1 :
    driver.switch_to.frame('cafe_main')
    tex = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div').text
    read(tex)
    driver.switch_to.default_content()
elif a == 2 :
    driver.switch_to.frame('cafe_main')
    tex = driver.find_element(
        By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[6]').text
    read(tex)