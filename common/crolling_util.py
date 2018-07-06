import datetime
import requests
from bs4 import BeautifulSoup
import openpyxl
import os
import crolling as crolling
import pymysql
import selenium

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
    rank_list = sorted(os.listdir(crolling.prj_path), reverse=True)
    for dir in rank_list:
        file = crolling.prj_path + '/' + dir
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

def get_soup_pwlinkSub(strTxt, pg):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = 'https://ad.search.naver.com/search.naver?where=ad&query=' + strTxt+'&pagingIndex='+str(pg)
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    return soup

def print_find_text(strKey):
    pStr1 = '============================================================================================'
    pStr2 = str(strKey)
    pStr3 = '--------------------------------------------------------------------------------------------'
    print(pStr1)
    print(pStr2)
    print(pStr3)

def insert_history(db, input_data):
    if db is None:
        return
    # try:
    find_key = input_data['find_key']
    ad = input_data['ad']
    site = input_data['site']
    item = input_data['item']
    page = input_data['page']
    idx = input_data['idx']
    mid1 = input_data['mid1']
    url = input_data['url']
    now = datetime.date.today()
    upStr = now.strftime("%Y-%m-%d")

    nowTime = datetime.datetime.now()
    nowTimeStr = nowTime.strftime("%Y-%m-%d %H:%M:%S")
    # nowDate = datetime.datetime(2009, 5, 5)
    curs = db.cursor()
    sql = "select * from flybeach.history "
    sql += "where update_date=%s and find_key=%s and mid1=%s and ad=%s "
    curs.execute(sql, (upStr, find_key, mid1, ad))
    rows = curs.fetchall()

    if len(rows) > 0:
        #Update
        sql = "update flybeach.history "
        sql += "set page=" + str(page) + ", last_update_date='" + nowTimeStr + "' "
        sql += "where update_date=%s and find_key=%s and mid1=%s "
        curs.execute(sql, (upStr, find_key, mid1))
    else:
        # Insert
        sql = "insert into flybeach.history(find_key, ad, site, item, page, idx, mid1, url, update_date) "
        sql += "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        curs.execute(sql, (find_key, ad, site, item, page, idx, mid1, url, upStr))

    db.commit()
    # except Exception as e:
    #     print(e)

def insert_history_pwlink(db, input_data):
    if db is None:
        return
    # try:
    find_key = input_data['find_key']
    main_sub = input_data['main_sub']
    idx = input_data['idx']
    item = input_data['item']
    item_desc = input_data['item_desc']

    now = datetime.date.today()
    upStr = now.strftime("%Y-%m-%d")

    nowTime = datetime.datetime.now()
    nowTimeStr = nowTime.strftime("%Y-%m-%d %H:%M:%S")
    # nowDate = datetime.datetime(2009, 5, 5)
    curs = db.cursor()
    sql = "select * from flybeach.history_pwlink "
    sql += "where update_date=%s and find_key=%s and idx=%s "
    curs.execute(sql, (upStr, find_key, idx))
    rows = curs.fetchall()

    if len(rows) > 0:
        #Update
        sql = "update flybeach.history_pwlink "
        sql += "set main_sub='" + main_sub + "', idx=" + str(idx) + ", last_update_date='" + nowTimeStr + "' "
        sql += "where update_date=%s and find_key=%s "
        curs.execute(sql, (upStr, find_key))
    else:
        # Insert
        sql = "insert into flybeach.history_pwlink(find_key, main_sub, idx, item, item_desc, update_date) "
        sql += "values (%s, %s, %s, %s, %s, %s)"
        curs.execute(sql, (find_key, main_sub, idx, item, item_desc, upStr))

    db.commit()
    # except Exception as e:
    #     print(e)

def find_page(findKey, pg, db):
    idx = 0
    soup = get_soup(findKey, pg)
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
                site = 'FLYBEACH'
            elif fbsIdxH > -1:
                site = '플라이비치'

            ad = ''
            if site is not None and adIdx > 0:
                ad = '(광고)'

            if site is not None:
                pStr = ad
                pStr += site
                pStr += println(str(imgName),25)
                pStr += 'Page:' + println(str(pg), 5)
                pStr += 'INDEX:' + println(str(idx), 5)
                pStr += 'MID:' + println(tag.attrs['data-nv-mid'], 20)
                pStr += '      ' + pageurl
                input_data = {'find_key':findKey, 'ad':ad, 'site':site, 'item':str(imgName), 'page':pg, 'idx':idx
                                , 'mid1':tag.attrs['data-nv-mid'], 'url':pageurl}
                insert_history(db, input_data)
                print(pStr)

    if pg % crolling.pagePrintCnt == 0:
        print('Process Page:' + str(pg))

def get_rank_common(sIdx, eIdx, findKeyArr, db):
    rankData = get_rank_key_count()
    for findKey in findKeyArr:
        rd = ''
        if findKey in rankData.keys():
            rd = str(rankData[findKey])
        strTxtPrint = findKey + '( ' + rd + ')'
        print_find_text(str(strTxtPrint))
        for pg in range(sIdx, eIdx + 1):
            find_page(findKey, pg, db)

        print('')


def get_rank_pwlink(findKeyArr, db):
    rankData = get_rank_key_count()
    for findKey in findKeyArr:
        rd = ''
        if findKey in rankData.keys():
            rd = str(rankData[findKey])
        strTxtPrint = findKey + '( ' + rd + ')'
        print_find_text(str(strTxtPrint))

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
                        findFlag = 'Y'
                        input_data = {'find_key': findKey, 'main_sub': 'main', 'idx': idx
                                        , 'item': tagTit.contents[0], 'item_desc': tagdsc.text }
                        insert_history_pwlink(db, input_data)
                        break
                    idx += 1

        if findFlag == 'N':
            get_rank_pwlink_sub(findKey, 1, db)

def get_rank_pwlink_sub(findKey, pg, db):
    pStr = ' - Sub Add Page...........................................................................................'
    print(pStr)
    soup = get_soup_pwlinkSub(findKey, pg)

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
                input_data = {'find_key': findKey, 'main_sub': 'main', 'idx': idx
                    , 'item': tagTit.contents[0], 'item_desc': tagdsc.text}
                insert_history_pwlink(db, input_data)
                print(pStr)
                return
        idx += 1

    if pg >= 3:
        return
    else:
        pg += 1
        get_rank_pwlink_sub(findKey, pg, db)

def get_rank_pwimg(findKeyArr, db):
    None
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

