import os
import shutil
import time

import pandas as pd
from src.common.get_config import get_cofig_init
get_cofig_init()
from src.common.get_config import config

money_dir = os.path.join(config.dirs.data_dir, 'money_nv')
result_dir = os.path.join(money_dir, 'money_nv_result')
if os.path.exists(result_dir):
    shutil.rmtree(result_dir)
    time.sleep(1)
os.makedirs(result_dir, exist_ok=True)

money_dir_list = [x for x in sorted(os.listdir(money_dir))
                    if x.find('money_') > -1 and x.find('result') < 0]

df_main = None
for md in money_dir_list:
    m_dir = os.path.join(money_dir, md)
    file_list = sorted(os.listdir(m_dir))
    for file in file_list:
        file_path = os.path.join(m_dir, file)
        df = pd.read_excel(file_path, engine='openpyxl')

        # 노출 가능인 데이터만 추출
        str_expr = "상태 == '노출가능'"
        df = df.query(str_expr)

        # 파일 명칭 컬럼 앞에 추가
        df.insert(0, '파일경로', os.path.splitext(file)[0])

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





