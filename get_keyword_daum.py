from selenium import webdriver
from bs4 import BeautifulSoup
import crolling
from common import crolling_util as crolling_util
import time, os, shutil
import pymysql

from common import key_value as key_value

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome(crolling_util.data_path+"\chromedriver")

driver.implicitly_wait(3)

# url에 접근한다.
driver.get('https://clix.biz.daum.net/login/login.jsp')

# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys(key_value.du_ad_id)
driver.find_element_by_name('pw').send_keys(key_value.du_ad_pw)

# 로그인 버튼을 눌러주자.//*[@id="loginForm"]/fieldset/button
driver.find_element_by_xpath('//*[@id="loginForm"]/fieldset/button').click()

#######################################################################################################################
# PC
linkArr = [
  'https://clix.biz.daum.net/report/top.do#/ADGROUP/10242684|TYPE=KEYWORD'  # 00. 자사명
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/11227226|TYPE=KEYWORD' # 01-1. 비치드레스
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/12688527|TYPE=KEYWORD' # 01-2. 수영복(커플)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/10242220|TYPE=KEYWORD' # 01-3. 비치웨어(커플)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/12214441|TYPE=KEYWORD' # 02-1. 경쟁사
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/12214478|TYPE=KEYWORD' # 03-1. 여름옷
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/10242318|TYPE=KEYWORD' # 03-2. 가디건/탑
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/12214496|TYPE=KEYWORD' # 04-1. 래쉬가드(여자)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/10242334|TYPE=KEYWORD' # 04-2. 래쉬가드(남자)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/10242361|TYPE=KEYWORD' # 04-3.래쉬가드(커플)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/16130140|TYPE=KEYWORD' # 04-4.래쉬가드(워터레깅스)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/12214500|TYPE=KEYWORD' # 05-1. 비키니(성과)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/10242347|TYPE=KEYWORD' # 05-2. 비키니(일반)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/10242349|TYPE=KEYWORD' # 06. 비치용품
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/10242340|TYPE=KEYWORD' # 07. 남자옷
]

for link in linkArr:
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    time.sleep(4)
    print('PC:'+link)
    driver.find_element_by_xpath('//*[@id="managementConditionReportDownload"]').click()

time.sleep(3)
#######################################################################################################################
# File Delete & move
for file in os.listdir(crolling_util.keyword_pcd_path):
    os.remove(crolling_util.keyword_pcd_path + '/' + file)
filelist = os.listdir(crolling_util.down_path)
for file in filelist:
    if file.find('현황보고서') > -1:
        shutil.move(crolling_util.down_path + '/' + file, crolling_util.keyword_pcd_path + '/' + file)
time.sleep(3)
#######################################################################################################################
# MB
linkArr = [
  'https://clix.biz.daum.net/report/top.do#/ADGROUP/12243276|TYPE=KEYWORD'  # 00. 자사명
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/11248121|TYPE=KEYWORD' # 01-1. 비치드레스
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/11227819|TYPE=KEYWORD' # 01-2. 수영복(커플)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/12214543|TYPE=KEYWORD' # 01-3. 비치웨어(커플)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/12214532|TYPE=KEYWORD' # 02-1. 경쟁사
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/16133285|TYPE=KEYWORD' # 03-2. 가디건/탑
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/12214547|TYPE=KEYWORD' # 04-1. 래쉬가드(여자)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/11227822|TYPE=KEYWORD' # 04-2. 래쉬가드(남자)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/16133101|TYPE=KEYWORD' # 04-3. 래쉬가드(커플)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/16133225|TYPE=KEYWORD' # 04-4. 래쉬가드(워터레깅스)
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/11227824|TYPE=KEYWORD' # 05. 비키니
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/11227825|TYPE=KEYWORD' # 06. 비치용품
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/11227827|TYPE=KEYWORD' # 07. 남자옷
# , 'https://clix.biz.daum.net/report/top.do#/ADGROUP/11227821|TYPE=KEYWORD' # 07-2.남자수영복
]

for link in linkArr:
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    time.sleep(4)
    print('PC:'+link)
    driver.find_element_by_xpath('//*[@id="managementConditionReportDownload"]').click()

time.sleep(3)
#######################################################################################################################
# File Delete & move
for file in os.listdir(crolling_util.keyword_mbd_path):
    os.remove(crolling_util.keyword_mbd_path + '/' + file)
filelist = os.listdir(crolling_util.down_path)
for file in filelist:
    if file.find('현황보고서') > -1:
        shutil.move(crolling_util.down_path + '/' + file, crolling_util.keyword_mbd_path + '/' + file)
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

# PC 키워드를 db에 등록해 주는 역할을 해준다.
keywordPC = crolling_util.get_rank_keyword_daum('pcd')
keywordMB = crolling_util.get_rank_keyword_daum('mbd')
curs = db.cursor()
sql = "delete from flybeach.keyword where pc_mb in('pcd', 'mbd') "
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









