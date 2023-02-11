import requests
from bs4 import BeautifulSoup
import pandas as pd


url_json = {'pc': 'https://ad.search.naver.com/search.naver?where=ad&query='
        , 'mb': 'https://m.ad.search.naver.com/search.naver?where=m_expd&query='}

key = '플라이비치'

url = url_json['mb'] + key + '&pagingIndex=' + str(1)
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

idx = 1
for tag in soup.select('li'):
    url_content = tag.find(class_='url')
    if url_content is not None:
        if url_content.text.find('flybeach.co.kr') > 0:
            print('---------------------------------------------------------------------------------------------------------')
            print(idx, url_content.text)
        idx += 1
