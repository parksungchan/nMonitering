import os, copy, datetime, sys, shutil, time
import requests
import pyperclip
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

config = None
config_info = {}

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
        dirs['cur_dir'] = os.path.split(os.path.dirname(os.path.abspath(sys.executable)))[0]
    else:
        dirs['cur_dir'] = os.path.split(os.path.realpath(__file__))[0]
    dirs['src_dir'] = os.path.dirname(dirs['cur_dir'])
    dirs['pjt_dir'] = os.path.dirname(dirs['src_dir'])
    dirs['config_dir'] = os.path.join(dirs['pjt_dir'], 'config')
    dirs['data_dir'] = os.path.join(dirs['pjt_dir'], 'data')
    dirs['master_dir'] = os.path.join(dirs['pjt_dir'], 'master')
    dirs['chromedriver_dir'] = os.path.join(dirs['master_dir'], 'chromedriver')

    os.makedirs(dirs['data_dir'], exist_ok=True)

    config = CustomClass(config_info)

    config.__setattr__('dirs', CustomClass({}))
    for ds in dirs:
        config.dirs.__setattr__(ds, dirs[ds])


def get_key_list():
    key_list = []
    for dr in os.listdir(config.dirs.data_dir):
        if dr.find('pc_key.txt') > -1:
            file_path = os.path.join(config.dirs.data_dir, dr)
            with open(file_path, 'r', encoding='UTF8') as f:
                lines = f.readlines()[1:]

            for line in lines:
                if line not in key_list:
                    key_list.append(line.replace('\n', ''))
    return key_list


def nv_down_seq():
    pl_dir = os.path.join(config.dirs.data_dir, 'power_link_nv')
    if os.path.exists(pl_dir):
        shutil.rmtree(pl_dir)
        time.sleep(1)
    os.makedirs(pl_dir, exist_ok=True)

    key_list = get_key_list()

    # key_list = ['검정색이쁜모노키니,130.0', '플라이비치,150.0']
    time.sleep(1)
    key_pd = []
    key_idx = 0
    total_idx = len(key_list)
    for strTxt_cnt in range(total_idx):
        strTxt, cost = key_list[strTxt_cnt].split(',')
        pg_list = [1, 2]
        idx = 1
        key_json = {}
        for pg in pg_list:
            url = 'https://ad.search.naver.com/search.naver?where=ad&query=' + strTxt + '&pagingIndex=' + str(pg)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")

            for tag in soup.select('li'):
                tagImg = tag.find(class_='tit_wrap') # lnk_tit
                if tagImg is not None:
                    sub_tagImg = tagImg.find(class_='lnk_tit')
                    if str(sub_tagImg).find('플라이비치') > -1:
                        # print(idx, sub_tagImg)
                        key_json = {'tag': strTxt, 'cost': int(float(cost)), 'val': idx}

                    idx += 1
        key_json['TotalIdx'] = idx - 1
        key_pd.append(key_json)
        key_idx += 1
        print('[Progrss]', str(key_idx) + '/' + str(total_idx))

    df = pd.DataFrame(key_pd)
    df_main = df.sort_values(by=df.columns[2], ascending=True)
    save_path = os.path.join(pl_dir, 'pc_power_link' + '.xlsx')
    with pd.ExcelWriter(save_path) as writer:
        df_main.to_excel(writer, sheet_name='sheet1')
    print('[Download]', save_path)
    time.sleep(1)



'''
    1. src/make_ad_seq 폴더에서 아래 명령어를 실행한다.
    pyinstaller -w -F make_ad_seq.py # 실행 파일 하나만 만들기
'''
print('[Start] ', datetime.datetime.now())
get_cofig_init()
time.sleep(1)
nv_down_seq()
print('[Complete] ', datetime.datetime.now())
