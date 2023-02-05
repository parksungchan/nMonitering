import os, copy, datetime
import time, shutil
import pandas as pd
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

pjt_dir = os.path.dirname(os.path.abspath(__file__))

from src.common.get_config import get_cofig_init
get_cofig_init()
from src.common.get_config import config


def nv_down_excel():
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
        if dr.find('money_nv') > -1:
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
    driver.find_element(By.XPATH,
                        '//*[@id="container"]/my-screen/div/div[1]/div/my-screen-board/div/div[1]/ul/li[1]/a').click()

    # 상세 광고로 이동 하여 pc, mobile excel 을 구분 해서 저장해 주어야 한다
    now = datetime.datetime.now()
    now7 = (now - datetime.timedelta(days=7)).strftime("%Y.%m.%d")
    now1 = (now - datetime.timedelta(days=1)).strftime("%Y.%m.%d")
    for pc_mb in config.nv_ad_url.__dict__:
        print('[Connect Start] ' + pc_mb)
        for link in config.nv_ad_url.__dict__[pc_mb].__dict__:
            lk = config.nv_ad_url.__dict__[pc_mb].__dict__[link]
            if lk == '':
                continue
            print(pc_mb, link, lk)

            # download page로 이동
            driver.get(lk)
            time.sleep(2)

            # excel download button 클릭
            driver.find_element(By.XPATH,
                                '//*[@id="root"]/div/div[2]/div/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button').click()
            time.sleep(2)

            # download에 있는 파일을 data 폴더의 money로 옮겨준다.
            money_dir = os.path.join(config.dirs.data_dir, 'money_nv', 'money_nv_' + pc_mb)
            os.makedirs(money_dir, exist_ok=True)
            move_list = [x for x in os.listdir(download_dir) if x.find('키워드') > -1]
            for move in move_list:
                src_path = os.path.join(download_dir, move)
                trg_path = os.path.join(money_dir, link + '$' + now7 + '$' + now1 + '.xlsx')
                shutil.move(src_path, trg_path)

        print('[Connect Complete] ' + pc_mb)
        print('')
        time.sleep(2)

    print('[Complete] Download Excel.')


def nv_load_excel():
    money_dir = os.path.join(config.dirs.data_dir, 'money_nv')
    result_dir = os.path.join(money_dir, 'money_nv_result')
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
        time.sleep(1)
    os.makedirs(result_dir, exist_ok=True)

    money_dir_list = [x for x in sorted(os.listdir(money_dir))
                      if x.find('money_') > -1 and x.find('result') < 0]

    for md in money_dir_list:
        df_main = None
        m_dir = os.path.join(money_dir, md)
        file_list = sorted(os.listdir(m_dir))
        for file in file_list:
            file_path = os.path.join(m_dir, file)
            df = pd.read_excel(file_path, engine='openpyxl')

            # 노출 가능인 데이터만 추출
            str_expr = "상태 == '노출가능'"
            df = df.query(str_expr)

            # data 앞에 파일경로, 수집 날짜 추가
            file_s = file.split('$')
            df.insert(0, '파일경로', file_s[0])
            df.insert(0, 'End', file_s[2])
            df.insert(0, 'Start', file_s[1])

            # 불필요 컬럼 앞에 삭제
            df = df.drop(['키워드 ID'], axis=1)
            df = df.drop(['상태'], axis=1)
            df = df.drop(['입찰가 유형'], axis=1)

            if df_main is None:
                df_main = df
            else:
                df_main = pd.concat([df_main, df])
        df_main = df_main.sort_values(by=['입찰가'], axis=0, ascending=False)

        save_path = os.path.join(result_dir, md + '.xlsx')
        with pd.ExcelWriter(save_path) as writer:
            df_main.to_excel(writer, sheet_name='sheet1')

        print('[Complete] Make Excel File: ' + save_path)
