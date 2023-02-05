import os, copy, datetime, sys
import time, shutil, getpass
import pandas as pd
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

config_info = {
  "nv_ad_info": {"id" : "flybeach", "pw": "flyhub85!@"}
  , "nv_ad_url": {
      "pc": {
        "자사명": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001628491798",
        "01.수영복": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232606",
        "01.수영복-남자": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000010571064",
        "01.수영복-커플": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001798581417",
        "02.1.경쟁업체": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232790",
        "03-1.허니문_커플": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232784",
        "03-2.허니문": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000001128493",
        "03-3.비치드레스": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232605",
        "03-4.비치웨어": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232608",
        "03-5.비치_가디건탑": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000002188028",
        "04-1.래쉬가드_주요": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629445851",
        "04-2.래쉬가드_여자": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629445833",
        "04-3.래쉬가드_남자": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232865",
        "04-4.래쉬가드_커플": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008552465",
        "04-5.래쉬가드_워터": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008552648",
        "04-6.래쉬가드_하의": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008563121",
        "05-1.비키니(성과)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232674",
        "05-2.비티니(일반1)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232615",
        "05-2.비티니(일반2)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232614",
        "05-4.하이웨스트": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000006865309",
        "05-5.모노키니": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000010488655",
        "05-6.원피스수영복": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000010698531",
        "06.비치용품": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232786",
        "07.남자옷": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232641",
        "08.여름옷": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232604",
        "09.배송키워드": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000019258264",
        "11.긴키워드": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232772",
        "12.신혼여행커플룩": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000004586344",
        "13.비치타올": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000004587199",
        "14.비치타올방수팩": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000005497368",
        "H.래쉬가드(세부)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011077736",
        "H.모노키니(세부)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011077305",
        "H.바캉스(세부)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011078122",
        "H.비키니색상(세부)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011076504",
        "H.수영복(세부)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011077101",
        "H.와이어": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011342874"
      },
      "mb": {
        "자사명": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000001802249",
        "02.1.경쟁업체": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993574",
        "03-1.허니문(성과)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993762",
        "03-2.허니문(일반)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993741",
        "03-3.비치드레스": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994099",
        "03-4.비치웨어": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000002189778",
        "03-5.비치_원피스": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000002196392",
        "03-6.커플수영복": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993874",
        "04-1.래쉬가드_주요": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994341",
        "04-2.래쉬가드_여자": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994256",
        "04-3.래쉬가드_남자": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008553018",
        "04-4.래쉬가드_커플": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008553070",
        "04-5.래쉬가드_워터": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008553077",
        "04-6.래쉬가드_하의": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008556260",
        "05-1.비키니(성과)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994792",
        "05-2.비티니(일반1)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994355",
        "05-3.수영복": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825998258",
        "05-4.하이웨스트": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000006865251",
        "05-5.모노키니": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000010488667",
        "05-6.원피스수영복": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000010698635",
        "06.비치용품": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825995386",
        "07.남자옷": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825995470",
        "08.550원설정키워드": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825995597",
        "09.배송키워드": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994721",
        "11.긴키워드": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994218",
        "12.신혼여행커플룩": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000004586405",
        "13.비치타올방수팩": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000005497491",
        "H.래쉬가드(세부)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011078469",
        "H.모노키니(세부)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011078471",
        "H.바캉스(세부)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011078473",
        "H.비키니색상(세부)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011078474",
        "H.수영복(세부)": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011078475",
        "H.와이어": "https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000011342923"
      }
    }
}

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


def nv_down_excel():
    '''
        크롬창에 url 넣어서 버전 확인 한다.
        chrome://version

        드라이버를 다운받는다. /nMonitering/master/chromedriver에 넣어준다.
        http://chromedriver.storage.googleapis.com/index.html

        config.json에서 nv_ad_info, nv_ad_url 가 작성되어 있어야 한다.

    '''
    get_cofig_init()
    # 기존 다운 받으려는 키워드 파일 삭제
    download_dir = os.path.join('C:Users', getpass.getuser(), 'Downloads')
    print('[Complete] Download Folder keyword list delete.')

    # # 키워드 분석한 결과 money 디렉토리 삭제
    # with open("E:\\0105.python\\nMonitering\\src\\common\\foo.txt", "w") as f:
    #     f.write(config.dirs.data_dir)

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


'''
    1. src/make_ad_money 폴더에서 아래 명령어를 실행한다.
    pyinstaller -w -F make_nv_excel.py # 실행 파일 하나만 만들기
    
    
'''
nv_down_excel()
time.sleep(2)
nv_load_excel()