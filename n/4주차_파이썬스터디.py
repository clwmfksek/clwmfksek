# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

# 실행경로와 드라이버 객체 생성

driver = webdriver.Chrome()
driver.get("http://capszzang.gq/")
while True :
    name_ = pyautogui.prompt("이름을 입력해 주세요 : ",title="입력")
    driver.find_element(By.XPATH,'//*[@id="top-bar"]/div/nav/div/ul/li[1]/a').click()
    driver.find_element(By.XPATH,'//*[@id="top-bar"]/div/nav/div/ul/li[1]/div/ul/li[4]/a').click()
    time.sleep(2)
    try :
        driver.find_element(By.LINK_TEXT,name_).click()
        tex = driver.find_element(By.XPATH,'/html/body/section[3]/div').text
        print(tex)
        break
    except : continue