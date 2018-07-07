from selenium import webdriver
from bs4 import BeautifulSoup
import crolling
import time

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome(crolling.data_path+"\chromedriver")

driver.implicitly_wait(3)

# url에 접근한다.
driver.get('https://m.ad.search.naver.com/search.naver?where=m_expd&query=래쉬가드')

# 버튼을 눌러주자.
idx = 0
while True:
    idx += 1
    if idx > 10:
        break
    element = driver.find_element_by_xpath('//*[@id="_get_more"]')
    print(element)
    element.click()



None