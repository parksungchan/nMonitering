from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome('E:\\0105.python\\chromedriver.exe') #크롬 드라이버
# url에 접근한다.
driver.get('https://camfit.co.kr/login')

# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys('aaaa')
driver.find_element_by_name('password').send_keys('bbb')

#driver.find_element(by=By.NAME, value='id').send_keys('soul8085')
#driver.find_element_by_name('password').send_keys('Posdata10!')

# driver.find_element_by_id('sc-caiLqq').send_keys('soul8085')
#
# xpath = "//input[@value='Y']" #테그+속성+속성값
# xpath = '//*[@id="root"]/div/section/div/div/div[2]/input[1]'
#driver.find_element_by_xpath(xpath).send_keys('soul8085')
#

# driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/section/div/div/div[2]/input[1]').send_keys('soul8085')
# driver.get('https://camfit.co.kr/camp/60dc100a9516e4001e681373/60dc1b1f0c9d29001efb7020') #접속할 url


# driver.find_element_by_xpath('//*[@id="root"]/div/section/div/div/ul/li[2]/a').click()
# driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/section/div/div[8]/div/button').click()
print('a')


