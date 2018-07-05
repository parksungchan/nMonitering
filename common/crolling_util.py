import datetime
import requests
from bs4 import BeautifulSoup
import openpyxl
import os
import crolling as crolling

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/log'
rank_path = prj_path
rank_list = sorted(os.listdir(rank_path), reverse=True)

def println(strTxt, cnt):
    if len(strTxt) > cnt:
        cnt = len(strTxt)+1
    return (strTxt + " " * cnt)[:cnt]

def printS(strTxt):
    print(strTxt)
    crolling.searchArrList.dict['list'].append(strTxt)

def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir

def get_strArr(strArr, strArrKey):
    for strStr in strArrKey:
        strArr.append(strStr)
    return strArr

def get_strArr_sub(strArr, strArrKey, strArrKeySub):
    for strR in strArrKey:
        for strRS in strArrKeySub:
            strArr.append(strR + strRS)
    return strArr

def get_rank_key_count():
    rankData = {}
    for dir in rank_list:
        file = rank_path + '/' + dir
        if file.find('xlsx') > 0:
            wb = openpyxl.load_workbook(file)
            ws = wb.active
            for row in ws.rows:
                name = row[0].value
                pc = row[1].value
                mb = row[2].value
                if name in rankData:
                    continue
                rankData[name] = {'pc': pc, 'mb': mb}
    return rankData

rankData = get_rank_key_count()

def get_soup(strTxt, pg):
    url = 'https://search.shopping.naver.com/search/all.nhn?origQuery=' + strTxt
    url += '&pagingIndex=' + str(pg) + '&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=' + strTxt
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml') # 'html.parser''lxml'
    return soup

def get_soup_pwlinkMain(strTxt):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + strTxt
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_soup_pwlinkSub(strTxt):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = 'https://ad.search.naver.com/search.naver?where=ad&query=' + strTxt
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    return soup

def print_find_text(strKey, myfile):
    pStr1 = '============================================================================================'
    pStr2 = str(strKey)
    pStr3 = '--------------------------------------------------------------------------------------------'
    print(pStr1)
    print(pStr2)
    print(pStr3)
    myfile.write(pStr1 + '\n')
    myfile.write(pStr2 + '\n')
    myfile.write(pStr3 + '\n')

def find_page(strTxt, pg, myfile, searchArr, itemKeyArr, logPath):
    idx = 0
    soup = get_soup(strTxt, pg)
    for tag in soup.select('li'):
        tagImg = tag.find(class_='img')
        if tagImg:
            idx += 1
            ct = tagImg.contents[1]
            imgName = ct.get('alt')
            pageurl = tagImg.attrs['href']
            fbIdx = tag.text.find('FLYBEACH')
            fbsIdxH = tag.text.find('플라이비치')
            adIdx = str(tag).find('ad _itemSection')
            site = None
            if fbIdx > -1:
                site = 'FLYBEACH    '
            elif fbsIdxH > -1:
                site = '플라이비치  '

            if site is not None and adIdx > 0:
                site = '(광고)' + site
                if logPath == 'logNv' or logPath == 'logSum':
                    site = None

            itemFlag = 'Y'
            for itemKey in itemKeyArr:
                itemFlag = 'N'
                if tag.attrs['data-nv-mid'].find(itemKey) > -1:
                    itemFlag = 'Y'
                    break

            if site is not None and itemFlag == 'Y':
                pStr = site
                pStr += println(str(imgName),25)
                pStr += 'Page:' + println(str(pg), 5)
                pStr += 'INDEX:' + println(str(idx), 5)
                pStr += 'MID:' + println(tag.attrs['data-nv-mid'], 20)
                pStr += '      ' + pageurl
                searchArr.append({'item':imgName, 'contents':pStr})
                print(pStr)
                myfile.write(pStr + '\n')

    if pg % crolling.pagePrintCnt == 0:
        print('Process Page:' + str(pg))

def get_rank_common(sIdx, eIdx, findKeyArr, itemKeyArr = None, logPath = 'logKey'):
    now = datetime.datetime.now()
    nowStr = str(now).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
    make_dir(log_path + '/' + logPath)

    with open(log_path + '/' + logPath + '/' + nowStr + ".txt", "a") as myfile:
        searchArr = []
        for findKey in findKeyArr:
            rd = ''
            if findKey in rankData.keys():
                rd = str(rankData[findKey])
            strTxtPrint = findKey + '( ' + rd + ')'
            print_find_text(str(strTxtPrint), myfile)
            for pg in range(sIdx, eIdx + 1):
                find_page(findKey, pg, myfile, searchArr, itemKeyArr, logPath)

            print('')
            myfile.write('\n')

def get_rank_pwlink(findKeyArr, itemKeyArr = None, logPath = 'logPw'):
    now = datetime.datetime.now()
    nowStr = str(now).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
    make_dir(log_path + '/' + logPath)

    with open(log_path + '/' + logPath + '/' + nowStr + ".txt", "a") as myfile:
        searchArr = []
        for findKey in findKeyArr:
            rd = ''
            if findKey in rankData.keys():
                rd = str(rankData[findKey])
            strTxtPrint = findKey + '( ' + rd + ')'
            print_find_text(str(strTxtPrint), myfile)

            idx = 1
            findFlag = 'N'
            soup = get_soup_pwlinkMain(findKey)
            for tag in soup.select('li'):
                tagInner = tag.find(class_='inner')
                tagTit = tag.find(class_='lnk_tit')
                tagdsc = tag.find(class_='ad_dsc')
                if tagTit:
                    id = tagTit.parent.parent.parent.parent.attrs['id']
                    if id == 'power_link_body' or id == 'biz_site_body':
                        if tagTit.attrs['onclick'].find('www.flybeach.co.kr') > -1:
                            pStr = 'INDEX:' + println(str(idx), 10)
                            pStr += println(tagTit.contents[0], 60)
                            pStr += println(tagdsc.text,90)
                            site = tagTit.attrs['onclick']
                            pStr += site[site.find('urlencode'):]
                            print(pStr)
                            myfile.write(pStr + '\n')
                            findFlag = 'Y'
                            break
                        idx += 1

            if findFlag == 'N':
                get_rank_pwlink_sub(findKey, myfile)

def get_rank_pwlink_sub(findKey, myfile):
    pStr = ' - Sub Add Page...........................................................................................'
    print(pStr)
    myfile.write(pStr + '\n')
    soup = get_soup_pwlinkSub(findKey)

    idx = 1
    for tag in soup.select('li'):
        tagTit = tag.find(class_='lnk_tit')
        tagUrl = tag.find(class_='url')
        tagdsc = tag.find(class_='ad_dsc')
        if tagTit:
            if tagUrl.text.find('www.flybeach.co.kr') > -1:
                pStr = println('  '+tag.find(class_='no').text, 5)
                pStr += println(' '+tagTit.text, 60)
                pStr += println(tagdsc.text, 90)
                pStr += println(tagUrl.text, 90)
                print(pStr)
                myfile.write(pStr + '\n')
        idx += 1


# def find_page_multi(strTxt, sIdx, eIdx): # 블로그의 게시글 링크들을 가져옵니다.
#     data = []
#     for pg in range(sIdx, eIdx + 1):
#         url = 'https://search.shopping.naver.com/search/all.nhn?origQuery=' + strTxt
#         url += '&pagingIndex=' + str(pg) + '&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=' + strTxt
#         data.append(url)
#     return data
#
# def get_content(url):
#     pg1 = url.find('&pagingIndex=')+len('&pagingIndex=')
#     pg2 = url.find('&pagingSize=')
#     pg = url[pg1:pg2]
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'html.parser')
#     idx = 0
#     for tag in soup.select('li'):
#         tagImg = tag.find(class_='img')
#         if tagImg:
#             idx += 1
#             ct = tagImg.contents[1]
#             imgName = ct.get('alt')
#             pageurl = tagImg.attrs['href']
#             fbIdx = tag.text.find('FLYBEACH')
#             fbsIdxH = tag.text.find('플라이비치')
#             adIdx = str(tag).find('ad _itemSection')
#
#             site = None
#             if fbIdx > -1:
#                 site = 'FLYBEACH    '
#             elif fbsIdxH > -1:
#                 site = '플라이비치  '
#
#             if site is not None and adIdx > 0:
#                 site = '(광고)' + site
#
#             if site is not None:
#                 pStr = site
#                 pStr += println(str(imgName), 25)
#                 pStr += 'Page:' + println(str(pg), 5)
#                 pStr += 'INDEX:' + println(str(idx), 5)
#                 pStr += 'MID:' + println(tag.attrs['data-nv-mid'], 20)
#                 pStr += '      ' + pageurl
#
#                 print(pStr)
#                 crolling.searchArrList.dict['list'].append(pStr)
#
# def get_rank_multi(sIdx, eIdx, findKeyArr, itemKeyArr = None, logPath = 'logKey'):
#     for findKey in findKeyArr:
#         printS('')
#         pStr1 = '============================================================================================'
#         pStr2 = str(findKey)
#         pStr3 = '--------------------------------------------------------------------------------------------'
#         printS(pStr1)
#         printS(pStr2)
#         printS(pStr3)
#
#         if crolling.multi:
#             pool = Pool(processes=32) # 4개의 프로세스를 사용합니다.
#             pool.map(get_content, find_page_multi(findKey, sIdx, eIdx)) # get_contetn 함수를 넣어줍시다.
#         else:
#             for link in find_page_multi(findKey, sIdx, eIdx):
#                 get_content(link)

