import datetime
import requests
from bs4 import BeautifulSoup
import os
import crolling as crolling
import pymysql
# import selenium

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

def get_soup(strTxt, pg):
    url = 'https://search.shopping.naver.com/search/all.nhn?origQuery=' + strTxt
    url += '&pagingIndex=' + str(pg) + '&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=' + strTxt
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml') # 'html.parser''lxml'
    return soup

def get_soup_pwlinkMainPC(strTxt):
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

def get_soup_pwlinkMainMB(strTxt):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = 'https://m.ad.search.naver.com/search.naver?where=m_expd&query=' + strTxt
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
    title = input_data['title'].replace("'", "")
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
        sql += "set title='" + title + "', page=" + str(page) + ", last_update_date='" + nowTimeStr + "' "
        sql += "where update_date=%s and find_key=%s and mid1=%s "
        curs.execute(sql, (upStr, find_key, mid1))
    else:
        # Insert
        sql = "insert into flybeach.history(title, find_key, ad, site, item, page, idx, mid1, url, update_date) "
        sql += "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        curs.execute(sql, (title, find_key, ad, site, item, page, idx, mid1, url, upStr))

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
    idx_total = input_data['idx_total']
    item = input_data['item']
    item_desc = input_data['item_desc']
    pc_mb = input_data['pc_mb']
    view = input_data['view']
    click = input_data['click']
    cost = input_data['cost']
    total_cost = input_data['total_cost']

    now = datetime.date.today()
    upStr = now.strftime("%Y-%m-%d")

    nowTime = datetime.datetime.now()
    nowTimeStr = nowTime.strftime("%Y-%m-%d %H:%M:%S")
    # nowDate = datetime.datetime(2009, 5, 5)
    curs = db.cursor()
    sql = "select * from flybeach.history_pwlink "
    sql += "where update_date=%s and find_key=%s and pc_mb=%s "
    curs.execute(sql, (upStr, find_key, pc_mb))
    rows = curs.fetchall()

    if len(rows) > 0:
        #Update
        sql = "update flybeach.history_pwlink "
        sql += "set main_sub='" + main_sub + "', idx=" + str(idx) + ", idx_total=" + str(idx_total) + ", last_update_date='" + nowTimeStr + "' "
        sql += ", view=" + str(view) + ", click=" + str(click) + ", cost=" + str(cost) + ", total_cost=" + str(total_cost) + " "
        sql += "where update_date=%s and find_key=%s "
        curs.execute(sql, (upStr, find_key))
    else:
        # Insert
        sql = "insert into flybeach.history_pwlink(find_key, main_sub, idx, idx_total, item, item_desc, update_date, pc_mb, view, click, cost, total_cost) "
        sql += "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        curs.execute(sql, (find_key, main_sub, idx, idx_total, item, item_desc, upStr, pc_mb, view, click, cost, total_cost))

    db.commit()
    # except Exception as e:
    #     print(e)

def find_page(strTxtPrint, findKey, pg, db):
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
                psite = 'FLYBEACH    '
            elif fbsIdxH > -1:
                site = '플라이비치'
                psite = '플라이비치  '

            ad = ''
            if site is not None and adIdx > 0:
                ad = '(광고)'

            if site is not None:
                pStr = ad
                pStr += psite
                pStr += println(str(imgName),25)
                pStr += 'Page:' + println(str(pg), 5)
                pStr += 'INDEX:' + println(str(idx), 5)
                pStr += 'MID:' + println(tag.attrs['data-nv-mid'], 20)
                pStr += '      ' + pageurl
                input_data = {'title':strTxtPrint, 'find_key':findKey, 'ad':ad, 'site':site, 'item':str(imgName), 'page':pg, 'idx':idx
                                , 'mid1':tag.attrs['data-nv-mid'], 'url':pageurl}
                insert_history(db, input_data)
                print(pStr)

    if pg % crolling.pagePrintCnt == 0:
        print('Process Page:' + str(pg))

def set_make_title(rowsKey, rowsKeyR, findKey):
    rd = ''
    if findKey in rowsKeyR.keys():
        rd = str(rowsKeyR[findKey])

    pcFindKey = 'PC:' + findKey
    pcrd = ''
    mbFindKey = 'MB:' + findKey
    mbrd = ''
    if pcFindKey in rowsKey.keys():
        pcrd = str(rowsKey[pcFindKey])
    if mbFindKey in rowsKey.keys():
        mbrd = str(rowsKey[mbFindKey])
    strTxtPrint = findKey + '( ' + rd + ')' + '          ( PC:' + pcrd + ')' + '     ( MB:' + mbrd + ')'
    return strTxtPrint

def get_rank_common(sIdx, eIdx, rowsKey, rowsKeyR, findKeyArr, db):
    for findKey in findKeyArr:
        strTxtPrint = set_make_title(rowsKey, rowsKeyR, findKey)
        print_find_text(str(strTxtPrint))
        for pg in range(sIdx, eIdx + 1):
            find_page(strTxtPrint, findKey, pg, db)

        print('')

def get_rank_pwlink(rowsKey, rankKey, rankKeyR, db):
    findKeyCnt = 0
    for findKeyArr in rowsKey:
        pc_mb = findKeyArr[0]
        findKey = findKeyArr[1]
        view = findKeyArr[2]
        click = findKeyArr[3]
        cost = findKeyArr[4]
        total_cost = findKeyArr[5]

        findKeyCnt += 1
        strTxtPrint = str(findKeyCnt) + '. ' + set_make_title(rankKey, rankKeyR, findKey)
        print_find_text(str(strTxtPrint))

        idx = 0
        findFlag = 'N'
        input_data = {}
        if pc_mb == 'pc':
            soup = get_soup_pwlinkMainPC(findKey)
            for tag in soup.select('li'):
                tagTit = tag.find(class_='lnk_tit')
                tagdsc = tag.find(class_='ad_dsc')
                if tagTit:
                    id = tagTit.parent.parent.parent.parent.attrs['id']
                    if id == 'power_link_body' or id == 'biz_site_body':
                        idx += 1
                        if tagTit.attrs['onclick'].find('www.flybeach.co.kr') > -1:
                            pStr = 'INDEX:' + println(str(idx), 10)
                            pStr += println(tagTit.contents[0], 60)
                            tagdscTxt = ''
                            if tagdsc is not None:
                                tagdscTxt = tagdsc.text
                            pStr += println(tagdscTxt, 90)
                            site = tagTit.attrs['onclick']
                            pStr += site[site.find('urlencode'):]
                            print(pStr)
                            findFlag = 'Y'
                            input_data = {'find_key': findKey, 'main_sub': 'main', 'idx': idx, 'idx_total':idx
                                          , 'view': view, 'click': click, 'cost': cost, 'total_cost': total_cost
                                , 'item': tagTit.contents[0], 'item_desc': tagdscTxt, 'pc_mb': 'pc'}

            if findFlag == 'N':
                get_rank_pwlink_sub(findKey, 1, db, idx, view, click, cost, total_cost)
            else:
                input_data['idx_total'] = idx
                insert_history_pwlink(db, input_data)
        else:
            soup = get_soup_pwlinkMainMB(findKey)
            for tag in soup.select('li'):
                tagTxt = tag.text.replace('\n','$').replace('$$','$').replace('$$','$').replace('$$','$').replace('$$','$')
                if tagTxt.find('모바일') > -1:
                    idx += 1
                    if tagTxt.find('flybeach.co.kr') > -1:
                        pStr = 'INDEX:' + println(str(idx), 10)
                        pStr += println(tagTxt,100)
                        print(pStr)
                        input_data = {'find_key': findKey, 'main_sub': 'main', 'idx': idx
                            , 'view': view, 'click': click, 'cost': cost, 'total_cost': total_cost
                            , 'item': tagTxt.split('$')[1], 'item_desc': tagTxt, 'pc_mb': 'mb'}
            input_data['idx_total'] = idx
            insert_history_pwlink(db, input_data)

def get_rank_pwlink_sub(findKey, pg, db, idx_total, view, click, cost, total_cost):
    pStr = ' - Sub Page:' + str(pg) + '............................................................................'
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
                if tagdsc.text is not None:
                    pStr += println(tagdsc.text, 90)
                pStr += println(tagUrl.text, 90)
                input_data = {'find_key': findKey, 'main_sub': 'sub', 'idx': tag.find(class_='no').text, 'idx_total':str(idx_total)
                    , 'view': view, 'click': click, 'cost': cost, 'total_cost': total_cost
                    , 'item': tagTit.contents[0], 'item_desc': tagdsc.text, 'pc_mb':'pc'}
                insert_history_pwlink(db, input_data)
                print(pStr)
                return
        idx += 1

    if pg >= 2:
        return
    else:
        pg += 1
        get_rank_pwlink_sub(findKey, pg, db, idx_total, view, click, cost, total_cost)

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

