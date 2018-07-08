from selenium import webdriver
from bs4 import BeautifulSoup
from common import crolling_util as crolling_util
import time

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome(crolling_util.data_path+"\chromedriver")

driver.implicitly_wait(3)

# url에 접근한다.
# driver.get('http://pla.naver.com/pc/product/list.nhn?rank=0&squareEnum=FASHION&kwd=래쉬가드&keyword=래쉬가드&ac=0&aq=0&chnl=&catgSeq=1&rootCatgId=1&bucketId=null')
driver.get('https://m.ad.search.naver.com/search.naver?where=m_expd&query=' + '래쉬가드')
# 스크롤을 가져오자
# element = driver.find_element_by_xpath('//*[@id="scrollbar"]/div[2]/div/div/span[2]')

# print(element.location_once_scrolled_into_view)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

None