from selenium import webdriver
from bs4 import BeautifulSoup
import crolling
from common import crolling_util as crolling_util
import time, os, shutil
import pymysql

from common import key_value as key_value

# for file in os.listdir(crolling_util.down_path):
#     filefull = crolling_util.down_path + '/' + file
#     if filefull.find('xlsx') > 0 and filefull.find('연관키워드') > 0:
#         os.remove(crolling_util.down_path + '/' + file)
#     if filefull.find('xlsx') > 0 and filefull.find('키워드 목록') > 0:
#         os.remove(crolling_util.down_path + '/' + file)
#
# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome(crolling_util.data_path+"\chromedriver")
# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
# driver = webdriver.PhantomJS('/Users/beomi/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

driver.implicitly_wait(3)

# url에 접근한다.
driver.get('https://searchad.naver.com/login')

# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys(key_value.nv_ad_id)
driver.find_element_by_name('pw').send_keys(key_value.nv_ad_pw)

# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="container"]/div/div/fieldset/span/button').click()

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
  'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001628491798' # 파워링크 광고그룹: 00. 자사명
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232606' # 파워링크 광고그룹: 01. 기본키워드
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232816' # 광고그룹 : 02-1. 경쟁업체(성과)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232790' # 광고그룹 : 02-2. 경쟁업체(일반)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232784' # 광고그룹 : 03-1. 허니문(성과)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000001128493' # 광고그룹 : 03-2. 허니문(추가)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232605' # 광고그룹 : 03-3. 비치드레스
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232608' # 광고그룹 : 03-4. 비치웨어
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000002188028' # 광고그룹 : 03-5. 비치/원피스_가디건
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629445851' # 광고그룹 : 04-1. 래쉬가드_주요
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629445833' # 광고그룹 : 04-2. 래쉬가드_여자
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232865' # 광고그룹 : 04-3. 래쉬가드_남자
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008552465' # 광고그룹 : 04-3. 래쉬가드_커플
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008552648' # 광고그룹 : 04-3. 래쉬가드_워터레깅스
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008563121' # 광고그룹 : 04-3. 래쉬가드_하의
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232674' # 광고그룹 : 05-1. 비키니(성과)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232615' # 광고그룹 : 05-2. 비키니(일반1)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232614' # 광고그룹 : 05-2. 비키니(일반2)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000006865309' # 광고그룹 : 05-4. 하이웨스트
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232786' # 광고그룹 : 06. 비치용품
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232641' # 광고그룹 : 07. 남자옷
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232604' # 광고그룹 : 08. 550원설정키워드
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001798581417' # 광고그룹 : 09. 배송키워드
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001629232772' # 광고그룹 : 11. 긴키워드
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000004586344' # 광고그룹 : 12. 7자키워드(은)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000004587199' # 광고그룹 : 13. 7자키워드(는)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000005497368' # 광고그룹 : 14. 비치타올방수팩
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
  'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000001802249' # 파워링크 광고그룹: 00. 자사명
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993620' # 광고그룹 : 02-1. 경쟁업체(성과)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993574' # 광고그룹 : 02-2. 경쟁업체(일반)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993762' # 광고그룹 : 03-1. 허니문(성과)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993741' # 광고그룹 : 03-2. 허니문(일반)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994099' # 광고그룹 : 03-3. 비치드레스
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000002189778' # 광고그룹 : 03-4. 비치웨어
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000002196392' # 광고그룹 : 03-5. 비치/원피스_가디건
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825993874' # 광고그룹 : 03-6. 커플수영복
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994341' # 광고그룹 : 04-1. 래쉬가드_주요
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994256' # 광고그룹 : 04-1. 래쉬가드_여자
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008553018'  # 광고그룹 : 04-1. 래쉬가드_남자
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008553070'  # 광고그룹 : 04-1. 래쉬가드_커플
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008553077'  # 광고그룹 : 04-1. 래쉬가드_워터레깅스
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000008556260'  # 광고그룹 : 04-1. 래쉬가드_하의
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994792' # 광고그룹 : 05-1. 비키니(성과)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994355' # 광고그룹 : 05-2. 비키니(일반1)
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825998258' # 광고그룹 : 05-3. 원피스수영복
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000006865251' # 광고그룹 : 05-4. 하이웨스트
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825995386' # 광고그룹 : 06. 비치용품
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825995470' # 광고그룹 : 07. 남자옷
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825995597' # 광고그룹 : 08. 550원설정키워드
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994721' # 광고그룹 : 09. 배송키워드
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-m001-01-000001825994218' # 광고그룹 : 11. 긴키워드
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000004586405' # 광고그룹 : 12. 신혼여행커플룩
, 'https://manage.searchad.naver.com/customers/927013/adgroups/grp-a001-01-000000005497491' # 광고그룹 : 13. 비치타올방수팩
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
sql = "delete from flybeach.keyword "
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
