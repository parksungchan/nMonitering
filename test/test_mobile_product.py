from selenium import webdriver
from bs4 import BeautifulSoup
from common import crolling_util as crolling_util
import time
SCROLL_PAUSE_TIME = 0.5

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome(crolling_util.data_path+"\chromedriver")

driver.implicitly_wait(3)
findKeyArr = ['래쉬가드', '비키니']
driver.get('https://m.ad.search.naver.com/search.naver?where=m_expd&query=') # url에 접근한다.

for findKey in findKeyArr:
    # 텍스트 입력
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(findKey)
    # 버튼을 눌러주자.
    driver.find_element_by_xpath('//*[@id="search"]/button').click()

    idx = 0
    while True:
        idx += 1
        if idx > 10:
            break
        try:
            element = driver.find_element_by_xpath('//*[@id="_get_more"]')
        except:
            break
        print(element)
        element.click()

    print('')