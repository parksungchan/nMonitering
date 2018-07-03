# parser.py
import requests, os
from bs4 import BeautifulSoup as bs
import time
import datetime
from multiprocessing import Pool # Pool import하기
# import crolling_util as crolling_util
logPath = 'logKey'
sIdx = 1
eIdx = 1

def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir

def get_soup(strTxt, pg):
    url = 'https://search.shopping.naver.com/search/all.nhn?origQuery=' + strTxt
    url += '&pagingIndex=' + str(pg) + '&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=' + strTxt
    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    return soup

def get_links(): # 블로그의 게시글 링크들을 가져옵니다.
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = bs(html, 'html.parser')
    my_titles = soup.select(
        'h3 > a'
        )
    data = []

    for title in my_titles:
        data.append(title.get('href'))
    return data

def get_content(link):
    abs_link = 'https://beomi.github.io'+link
    req = requests.get(abs_link)
    html = req.text
    soup = bs(html, 'html.parser')
    # 가져온 데이터로 뭔가 할 수 있겠죠?
    # 하지만 일단 여기서는 시간만 확인해봅시다.
    print(soup.select('h1')[0].text) # 첫 h1 태그를 봅시다.

if __name__=='__main__':
    now = datetime.datetime.now()
    nowStr = str(now).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
    file_path = os.path.dirname(os.path.abspath(__file__))
    dirlist = sorted(os.listdir(file_path), reverse=True)
    # crolling_util.make_dir(file_path + '/' + logPath)
    now = datetime.datetime.now()
    nowStr = str(now).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
    print('Start:' + nowStr)
    print('')

    for i in range(1, 3):
        pool = Pool(processes=16) # 4개의 프로세스를 사용합니다.
        pool.map(get_content, get_links()) # get_contetn 함수를 넣어줍시다.

        # for link in get_links():
        #     get_content(link)

    print('')
    end = datetime.datetime.now()
    endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
    print('End:' + endStr)
    print('Sub:' + str(end - now))