import os, datetime, sys, shutil, time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from src.common.get_utils import get_cofig_init

config = None
config_info = {'run_path': os.path.abspath(__file__)}
get_cofig_init(config_info)
from src.common.get_utils import config


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
                        url_content = tag.find(class_='tit_wrap')
                        if url_content is not None:
                            if url_content.text.find('flybeach.co.kr') > 0 and iflag:
                                save_json = {'Category': ct, '키워드': key
                                            , '입찰가': int(key_val['입찰가'])
                                            , '평균클릭비용': int(key_val['평균클릭비용'])
                                            , 'idx': loc_idx}
                                iflag = False

                            loc_idx += 1
                if '키워드' not in save_json:
                    save_json['Category'] = ct
                    save_json['키워드'] = key
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

start = datetime.datetime.now()
# print('[Start] ', start)
nv_down_seq()
print('[Start] ', start)
print('[Complete] ', datetime.datetime.now())
print('[Total] ', datetime.datetime.now() - start)