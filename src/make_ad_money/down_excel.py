import os
import time

import pyperclip

from src.common.get_config import get_cofig_init
get_cofig_init()
from src.common.get_config import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''
    크롬창에 url 넣어서 버전 확인 한다. 
    chrome://version
    
    드라이버를 다운받는다. /nMonitering/master/chromedriver에 넣어준다.
    http://chromedriver.storage.googleapis.com/index.html
    
'''
driver_dir = config.dirs.chromedriver_dir
driver_path = os.path.join(driver_dir, 'chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(3)

# 광고 크롬 열기
driver.get('https://searchad.naver.com/login')

# id, pass 입력
driver.find_element(By.NAME, 'id').click()
pyperclip.copy(config.nv_ad_info.id)
driver.find_element(By.NAME, 'id').send_keys(Keys.CONTROL, 'v')
driver.find_element(By.NAME, 'pw').click()
pyperclip.copy(config.nv_ad_info.pw)
driver.find_element(By.NAME, 'pw').send_keys(Keys.CONTROL, 'v')

# 로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="container"]/div/div/fieldset/div/div/button').click()

# 광고 시스템 클릭
driver.find_element(By.XPATH, '//*[@id="container"]/my-screen/div/div[1]/div/my-screen-board/div/div[1]/ul/li[1]/a').click()

# 상세 광고로 이동 하여 excel download
for pc_mb in config.nv_ad_url.__dict__:
    for link in config.nv_ad_url.__dict__[pc_mb]:
        driver.get(link)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button').click()

print('Complete')