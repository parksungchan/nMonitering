from selenium import webdriver
from bs4 import BeautifulSoup

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('/home/dev/chromedriver')
# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
# driver = webdriver.PhantomJS('/Users/beomi/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

driver.implicitly_wait(3)

# url에 접근한다.
# driver.get('https://google.com')



driver.get('https://nid.naver.com/nidlogin.login')

# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys('naver_id')
driver.find_element_by_name('pw').send_keys('mypassword1234')

# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# Naver 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())