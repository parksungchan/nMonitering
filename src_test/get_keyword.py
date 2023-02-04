from selenium import webdriver
from bs4 import BeautifulSoup
from src_test.common import crolling_util as crolling_util, key_value as key_value
import time, os, shutil
import pymysql

# for file in os.listdir(crolling_util.down_path):
#     filefull = crolling_util.down_path + '/' + file
#     if filefull.find('xlsx') > 0 and filefull.find('연관키워드') > 0:
#         os.remove(crolling_util.down_path + '/' + file)
#     if filefull.find('xlsx') > 0 and filefull.find('키워드 목록') > 0:
#         os.remove(crolling_util.down_path + '/' + file)
#
# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome(crolling_util.data_path + "\chromedriver")
# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
# driver = webdriver.PhantomJS('/Users/beomi/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

driver.implicitly_wait(3)

# url에 접근한다.
driver.get('https://searchad.naver.com/login')

# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys(key_value.nv_ad_id)
driver.find_element_by_name('pw').send_keys(key_value.nv_ad_pw)

# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="container"]/div/div/fieldset/div/span/button').click()

#######################################################################################################################
# 키워드연관 다운로드
driver.get('https://manage.searchad.naver.com/customers/927013/tool/keyword-planner')

keyword_arr =['래쉬가드', '모노키니', '비키니', '비치웨어', '비치원피스', '신혼여행커플룩', '방수팩', '비치타올']

for keyword in keyword_arr:
    driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/form/div[1]/div/div/textarea').send_keys(keyword)
    driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/form/div[4]/div/div/ul/li/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/button').click()
    driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/form/div[1]/div/div/textarea').clear()
    time.sleep(3)

time.sleep(3)
#######################################################################################################################
# File Move
for file in os.listdir(crolling_util.keyword_r_path):
    os.remove(crolling_util.keyword_r_path + '/' + file)
filelist = os.listdir(crolling_util.down_path)
for file in filelist:
    if file.find('연관키워드') > -1:
        shutil.move(crolling_util.down_path + '/' + file, crolling_util.keyword_r_path + '/' + file)
#######################################################################################################################
# PC
linkArr = [
  'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001628491798' # 00. 자사명
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232606' # 01. 수영복
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000010571064' # 01. 수영복 - 남자
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001798581417' # 01.수영복-커플
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232790' # 02-1. 경쟁업체
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232784' # 03-1. 허니문_커플
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000001128493' # 03-2. 허니문
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232605' # 03-3. 비치드레스
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232608' # 03-4. 비치웨어
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000002188028' # 03-5. 비치_가디건탑
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629445851' # 04-1. 래쉬가드_주요
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629445833' # 04-2. 래쉬가드_여자
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232865' # 04-3. 래쉬가드_남자
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008552465' # 04-4. 래쉬가드_커플
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008552648' # 04-5. 래쉬가드_워터래깅스
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008563121' # 04-5. 래쉬가드_하의
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232674' # 05-1. 비키니(성과)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232615' # 05-2. 비키니(일반1)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232614' # 05-2. 비키니(일반2)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000006865309' # 05-4. 하이웨스트
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000010488655' # 05-5. 모노키니
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232786' # 06. 비치용품
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232641' # 07. 남자옷
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232604' # 08. 여름옷
# , '' # 11.
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000004586344' # 12. 신혼여행커플룩
# , '' # 13.
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000005497368' # 14. 비치타올방수팩
]
for link in linkArr:
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    time.sleep(4)
    print('PC:'+link)
    driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[4]/div/div[1]/div/div/div/div[1]/div[2]/button').click()

time.sleep(3)
#######################################################################################################################
# File Move
for file in os.listdir(crolling_util.keyword_pc_path):
    os.remove(crolling_util.keyword_pc_path + '/' + file)
filelist = os.listdir(crolling_util.down_path)
for file in filelist:
    if file.find('키워드 목록') > -1:
        shutil.move(crolling_util.down_path + '/' + file, crolling_util.keyword_pc_path + '/' + file)
time.sleep(3)
#######################################################################################################################
# Mobile
linkArr = [
'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000001802249' # 00. 자사명
# , '' # 02-1.
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993574' # 02-1. 경쟁업체
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993762' # 03-1. 허니문(성과)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993741' # 3-2. 허니문(일반)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994099' # 03-3. 비치드레스
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000002189778' # 03-4. 비치웨어
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000002196392' # 03-5. 비치/원피스_가디건탑
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993874' # 03-6. 커플수영복
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994341' # 04-1. 래쉬가드_주요
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994256' # 04-2. 래쉬가드-여자
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008553018' # 04-3. 래쉬가드_남자
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008553070' # 04-4. 래쉬가드-커플
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008553077' # 04-5. 래쉬가드-워터래깅스
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008556260' # 04-6. 래쉬가드-하의
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994792' # 05-1. 비키니(성과)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994355' # 05-2. 비키니(일반1)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825998258' # 05-3. 원피스수영복
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000006865251' # 05-4. 하이웨스트
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000010488667' # 05-5. 모노키니
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825995386' # 06. 비치용품
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825995470' # 07. 남자옷
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825995597' # 08. 550원설정키워드
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994721' # 09. 배송키워드
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994218' # 11. 긴키워드
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000004586405' # 12. 신혼여행커플룩
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000005497491' # 13. 비치타올방수팩
]
for link in linkArr:
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    time.sleep(4)
    print('MB:'+link)
    driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[4]/div/div[1]/div/div/div/div[1]/div[2]/button').click()

time.sleep(3)
#######################################################################################################################
# File Move
for file in os.listdir(crolling_util.keyword_mb_path):
    os.remove(crolling_util.keyword_mb_path + '/' + file)
filelist = os.listdir(crolling_util.down_path)
for file in filelist:
    if file.find('키워드 목록') > -1:
        shutil.move(crolling_util.down_path + '/' + file, crolling_util.keyword_mb_path + '/' + file)
time.sleep(3)
#######################################################################################################################
try:
    db = pymysql.connect(host=key_value.host
                         , port=key_value.port
                         , user=key_value.user
                         , passwd=key_value.password
                         , db=key_value.db
                         , charset=key_value.charset
                         , autocommit=True)
except:
    print('db connection error............................................')
    db = None

print('연관 키워드 등록 Start .........')
# 연관 키워드를 db에 등록해 주는 역할을 해준다.
keywordR = crolling_util.get_rank_keywordR()

curs = db.cursor()
sql = "delete from flybeach.keywordR "
curs.execute(sql)
db.commit()

pIdx = 1
print('Total Cnt:'+str(len(keywordR.keys())))
for input_data in keywordR:
    pc_cnt = keywordR[input_data]['pc']
    mb_cnt = keywordR[input_data]['mb']
    sql = "insert into flybeach.keywordR(find_key, pc_cnt, mb_cnt) "
    sql += "values (%s, %s, %s)"
    curs.execute(sql, (input_data, pc_cnt, mb_cnt))
    if pIdx%500 == 0:
        print('Process:'+str(pIdx))
    pIdx += 1
db.commit()

# PC 키워드를 db에 등록해 주는 역할을 해준다.
keywordPC = crolling_util.get_rank_keyword('pc')
keywordMB = crolling_util.get_rank_keyword('mb')
curs = db.cursor()
sql = "delete from flybeach.keyword where pc_mb in('pc', 'mb') "
curs.execute(sql)
db.commit()

print('PC 키워드 등록 Start .........')
pIdx = 1
print('Total Cnt:'+str(len(keywordPC.keys())))
for input_data in keywordPC:
    cost = keywordPC[input_data]['cost']
    view = keywordPC[input_data]['view']
    click = keywordPC[input_data]['click']
    total_cost = keywordPC[input_data]['total_cost']
    file_name = keywordPC[input_data]['file_name']
    sql = "insert into flybeach.keyword(pc_mb, find_key, cost, view, click, total_cost, file_name) "
    sql += "values (%s, %s, %s, %s, %s, %s, %s)"
    curs.execute(sql, ('pc', input_data, cost, view, click, total_cost, file_name))
    if pIdx%500 == 0:
        print('Process:' + str(pIdx))
    pIdx += 1
db.commit()

print('MB 키워드 등록 Start .........')
pIdx = 1
print('Total Cnt:'+str(len(keywordMB.keys())))
for input_data in keywordMB:
    cost = keywordMB[input_data]['cost']
    view = keywordMB[input_data]['view']
    click = keywordMB[input_data]['click']
    total_cost = keywordMB[input_data]['total_cost']
    sql = "insert into flybeach.keyword(pc_mb, find_key, cost, view, click, total_cost) "
    sql += "values (%s, %s, %s, %s, %s, %s)"
    curs.execute(sql, ('mb', input_data, cost, view, click, total_cost))
    if pIdx%500 == 0:
        print('Process:' + str(pIdx))
    pIdx += 1
db.commit()

print('')
