import os, shutil, datetime, sys
import time, shutil, getpass
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import pandas as pd
from config.config import config_info
config = None


class CustomClass:
    def __init__(self, config_dict):
        for con in config_dict:
            if type(config_dict[con]) is dict:
                self.__setattr__(con, CustomClass(config_dict[con]))
            else:
                self.__setattr__(con, config_dict[con])


def get_cofig_init():
    global config
    config = CustomClass({})

    # dir list
    dirs = {}
    if getattr(sys, 'frozen', False):
        # .exe로 실행한 경우,.exe를 보관한 디렉토리의 full path를 취득
        dirs['common_dir'] = os.path.split(os.path.dirname(os.path.abspath(sys.executable)))[0]
    else:
        dirs['common_dir'] = os.path.split(os.path.realpath(__file__))[0]

    dirs['src_dir'] = os.path.dirname(dirs['common_dir'])
    dirs['pjt_dir'] = os.path.dirname(dirs['src_dir'])
    dirs['config_dir'] = os.path.join(dirs['pjt_dir'], 'config')
    dirs['data_dir'] = os.path.join(dirs['pjt_dir'], 'data')
    dirs['master_dir'] = os.path.join(dirs['pjt_dir'], 'master')
    dirs['chromedriver_dir'] = os.path.join(dirs['master_dir'], 'chromedriver')
    dirs['data_nv_key_dir'] = os.path.join(dirs['data_dir'], '01.nv_key')
    dirs['result_nv_key'] = os.path.join(dirs['data_dir'], '10.result_nv_key')
    dirs['result_nv_seq'] = os.path.join(dirs['data_dir'], '20.result_nv_seq')
    os.makedirs(dirs['data_dir'], exist_ok=True)

    config = CustomClass(config_info)

    config.__setattr__('dirs', CustomClass({}))
    for ds in dirs:
        config.dirs.__setattr__(ds, dirs[ds])


def nv_down_excel():
    '''
        크롬창에 url 넣어서 버전 확인 한다.
        chrome://version

        드라이버를 다운받는다. /nMonitering/master/chromedriver에 넣어준다.
        http://chromedriver.storage.googleapis.com/index.html

        config.json에서 nv_ad_info, nv_ad_url 가 작성되어 있어야 한다.

    '''
    print('[Complete] Download Folder keyword list delete.')
    # 기존 다운 받으려는 키워드 파일 삭제
    for dr in os.listdir(config.dirs.data_dir):
        if dr.find(os.path.basename(config.dirs.data_nv_key_dir)) > -1:
            d = os.path.join(config.dirs.data_dir, dr)
            if os.path.isdir(d):
                shutil.rmtree(d)
    print('[Complete] Key Folder delete.')

    # Load Chrome Driver
    driver_path = os.path.join(config.dirs.common_dir, 'chromedriver.exe')
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
    now = datetime.datetime.now()
    now7 = (now - datetime.timedelta(days=7)).strftime("%Y.%m.%d")
    now1 = (now - datetime.timedelta(days=1)).strftime("%Y.%m.%d")
    download_dir = os.path.join('C:Users', getpass.getuser(), 'Downloads')
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
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button').click()
            time.sleep(2)

            # download에 있는 파일을 data 폴더의 money로 옮겨준다.
            key_dir = os.path.join(config.dirs.data_nv_key_dir, pc_mb)
            os.makedirs(key_dir, exist_ok=True)
            move_list = [x for x in os.listdir(download_dir) if x.find('키워드') > -1]
            for move in move_list:
                src_path = os.path.join(download_dir, move)
                trg_path = os.path.join(key_dir, link + '$' + now7 + '$' + now1 + '.xlsx')
                shutil.move(src_path, trg_path)

        print('[Connect Complete] ' + pc_mb)
        print('')
        time.sleep(2)

    print('[Complete] Download Excel.')


def nv_load_excel():
    result_dir = config.dirs.result_nv_key
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
        time.sleep(1)
    os.makedirs(result_dir, exist_ok=True)

    key_dir_list = [x for x in sorted(os.listdir(config.dirs.data_nv_key_dir))]

    for mp in key_dir_list:
        df_main = None
        mp_dir = os.path.join(config.dirs.data_nv_key_dir, mp)
        file_list = sorted(os.listdir(mp_dir))
        for file in file_list:
            file_path = os.path.join(mp_dir, file)
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

        save_path = os.path.join(result_dir, mp + '.xlsx')
        with pd.ExcelWriter(save_path) as writer:
            df_main.to_excel(writer, sheet_name='sheet1')

        print('[Complete] Make Excel File: ' + save_path)


def get_key_json():
    key_json = {}
    key_cnt_json = {'total': 0}
    for dr in os.listdir(config.dirs.result_nv_key):
        file_path = os.path.join(config.dirs.result_nv_key, dr)
        df = pd.read_excel(file_path, engine='openpyxl')
        key_name = dr.split('.')[0]
        key_json[key_name] = {}
        key_cnt_json[key_name] = len(df)
        key_cnt_json['total'] += len(df)
        for index, row in df.iterrows():
            if row['파일경로'] not in key_json[key_name]:
                key_json[key_name][row['파일경로']] = {}
            key_json[key_name][row['파일경로']][row['키워드']] = {'입찰가': row['입찰가']
                , '노출수': row['노출수']
                , '클릭수': row['클릭수']
                , '평균클릭비용': row['평균클릭비용(VAT포함,원)']
                , '총비용': row['총비용(VAT포함,원)']
                , '노출가능광고개수': row['노출가능 광고개수(PC)']
                , 'start': row['Start']
                , 'end': row['End']
                                                           }

    return key_json, key_cnt_json


def nv_down_seq():
    if os.path.exists(config.dirs.result_nv_seq):
        shutil.rmtree(config.dirs.result_nv_seq)
        time.sleep(1)
    os.makedirs(config.dirs.result_nv_seq, exist_ok=True)

    key_json, key_cnt_json = get_key_json()
    '''
    key_json = {'mb':
                    {'02.1.경쟁업체':
                           {'고고비치':{'입찰가': 300, '노출수': 6, '클릭수': 2, '평균클릭비용': 264
                               , '총비용': 528, '노출가능광고개수': 15,'start':'2023.02.04','end':'2023.02.10'}}
                    }
                }
    '''
    url_json = {'pc': 'https://ad.search.naver.com/search.naver?where=ad&query='
        , 'mb': 'https://m.ad.search.naver.com/search.naver?where=m_expd&query='}

    key_idx = 0
    down_list = []
    for mp in key_json:
        key_pd = []
        ct_json = key_json[mp]
        pg_list = [1, 2]  # 총 2page 의 50건에 대해서만 체크 한다.
        if mp == 'mb':
            pg_list = [1]
        for ct in ct_json:
            k_json = ct_json[ct]
            for key in k_json:
                key_val = k_json[key]
                loc_idx = 1
                save_json = {}
                iflag = True

                for pg_cnt in pg_list:
                    url = url_json[mp] + key + '&pagingIndex=' + str(pg_cnt)
                    page = requests.get(url)
                    soup = BeautifulSoup(page.content, "html.parser")

                    for tag in soup.select('li'):
                        url_content = tag.find(class_='url')
                        if url_content is not None:
                            if url_content.text.find('flybeach.co.kr') > -1 and iflag:
                                save_json = {'Category': ct, '키워드': key
                                    , '입찰가': int(key_val['입찰가'])
                                    , '평균클릭비용': int(key_val['평균클릭비용'])
                                    , '총비용': int(key_val['총비용'])
                                    , 'idx': loc_idx}
                                iflag = False

                            loc_idx += 1
                if '키워드' not in save_json or 'idx' not in save_json or '입찰가' not in save_json:
                    save_json['키워드'] = key
                    save_json['Category'] = ct
                    save_json['idx'] = 0
                    save_json['입찰가'] = 0
                save_json['TotalIdx'] = loc_idx - 1
                key_pd.append(save_json)
                key_idx += 1
                print('[Progrss]', mp, str(key_idx) + '/' + str(key_cnt_json['total']), save_json)

        df = pd.DataFrame(key_pd)
        df_main = df.sort_values(by=['Category', 'idx', 'TotalIdx', '입찰가'], ascending=[True, True, True, True])
        save_path = os.path.join(config.dirs.result_nv_seq, mp + '.xlsx')
        with pd.ExcelWriter(save_path) as writer:
            df_main.to_excel(writer, sheet_name='sheet1')
        down_list.append(save_path)

        time.sleep(1)

    print('')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    for down in down_list:
        print('[Download]', down)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('')