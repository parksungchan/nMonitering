import os, copy
import time, shutil

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
    
    config.json에서 nv_ad_info, nv_ad_url 가 작성되어 있어야 한다.
    
'''
# 기존 다운 받으려는 키워드 파일 삭제
rootdir = 'C:Users'
download_dir = ''
for rootdir, dirs, files in os.walk(rootdir):
    if os.path.split(rootdir)[1] == 'Downloads':
        download_dir = copy.deepcopy(rootdir)
        for file in files:
            if file.find('키워드') > -1:
                file_path = os.path.join(rootdir, file)
                os.remove(file_path)
        break
print('[Complete] Download Folder keyword list delete.')

# 키워드 분석한 결과 money 디렉토리 삭제
for dr in os.listdir(config.dirs.data_dir):
    if dr.find('money_') > -1:
        shutil.rmtree(os.path.join(config.dirs.data_dir, dr))
print('[Complete] Money Folder delete.')

# Load Chrome Driver
driver_dir = config.dirs.chromedriver_dir
driver_path = os.path.join(driver_dir, 'chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(3)
print('[Complete] Driever Load.')

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
        
# 상세 광고로 이동 하여 pc, mobile excel 을 구분 해서 저장해 주어야 한다
for pc_mb in config.nv_ad_url.__dict__:
    print('[Connect Start] ' + pc_mb)
    for link in config.nv_ad_url.__dict__[pc_mb].__dict__:
        lk = config.nv_ad_url.__dict__[pc_mb].__dict__[link]
        if lk == '':
            continue
        print(link, lk)

        # download page로 이동
        driver.get(lk)
        time.sleep(2)

        # excel download button 클릭
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button').click()
        time.sleep(2)

        # download에 있는 파일을 data 폴더의 money로 옮겨준다.
        money_dir = os.path.join(config.dirs.data_dir, 'money_' + pc_mb)
        os.makedirs(money_dir, exist_ok=True)
        move_list = [x for x in os.listdir(download_dir) if x.find('키워드') > -1]
        for move in move_list:
            src_path = os.path.join(download_dir, move)
            trg_path = os.path.join(money_dir, link + '.xlsx')
            shutil.move(src_path, trg_path)

    print('[Connect Complete] ' + pc_mb)
    print('')
    time.sleep(2)

print('[Complete] Download Excel.')