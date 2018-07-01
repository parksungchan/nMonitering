import datetime
import requests
from bs4 import BeautifulSoup
import openpyxl
import os, shutil

file_path = os.path.dirname(os.path.abspath(__file__))
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
dirlist = sorted(os.listdir(file_path), reverse=True)
print('Start:'+nowStr)

def println(strTxt, cnt):
    return (strTxt + " " * cnt)[:cnt]

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

def add_key(kMain, kSub):
    for ks in kSub:
        kMain.append(ks)
    return kMain

def get_rank_key_count():
    rankData = {}
    for dir in dirlist:
        file = file_path + '/' + dir
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
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_rank(strArr, sIdx, eIdx):
    rankData = get_rank_key_count()

    make_dir(file_path+"/log")
    with open(file_path+"/log/"+nowStr + ".txt", "a") as myfile:
        for strTxt in strArr:
            rd = {}
            if strTxt in rankData:
                rd = rankData[strTxt]

            pStr1 = 'Key:$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
            pStr2 = 'Key:' + strTxt + '( '+ str(rd) +')'
            print(pStr1)
            print(pStr2)
            print(pStr1)
            myfile.write('Start:' + nowStr + '\n')
            myfile.write(pStr1 + '\n')
            myfile.write(pStr2 + '\n')
            myfile.write(pStr1 + '\n')

            for pg in range(sIdx, eIdx):
                idx = 1
                soup = get_soup(strTxt, pg)
                for tag in soup.select('li'):
                    tagImg = tag.find(class_='img')
                    if tagImg:
                        # print(tagImg)
                        ct = tagImg.contents[1]
                        imgName = ct.get('alt')
                        pageurl = tagImg.attrs['href']

                        adIdx = str(tag).find('ad _itemSection')
                        if adIdx > 0:
                            site = '(광고)'
                        else:
                            site = ''

                        runFlag = 'Y'
                        fbIdx = tag.text.find('FLYBEACH')
                        fbsIdxH = tag.text.find('플라이비치')
                        if fbIdx > -1:
                            site += 'FLYBEACH    '
                        elif fbsIdxH > -1:
                            site += '플라이비치  '
                        else:
                            runFlag = 'N'
                        if runFlag == 'Y':
                            pStr = site
                            pStr += 'Page:' + println(str(pg), 5)
                            pStr += 'INDEX:' + println(str(idx), 5)
                            pStr += 'MID:' + println(tag.attrs['data-nv-mid'], 20)
                            pStr += '(' + str(imgName) + ')     ' + pageurl
                            print(pStr)
                            myfile.write(pStr + '\n')
                        idx += 1

        end = datetime.datetime.now()
        endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
        print('End:' + endStr)
        print('Sub:' + str(end - now))
        myfile.write('End:' + endStr+ '\n')
        myfile.write('Sub:' + str(end - now)+ '\n')

def get_rank_product(strKey, findArr, sIdx, eIdx, pagePrintCnt):
    rankData = get_rank_key_count()
    make_dir(file_path + "/logMain")

    with open(file_path + "/logMain/" + nowStr + ".txt", "a") as myfile:
        pStr1 = 'Find Text:============================================================================================'
        pStr2 = 'Find Text:' + str(strKey)
        print(pStr1)
        print(pStr2)
        print(pStr1)
        print('')
        myfile.write('Start:' + nowStr + '\n')
        myfile.write(pStr1 + '\n')
        myfile.write(pStr2 + '\n')
        myfile.write(pStr1 + '\n')
        myfile.write('\n')

        for strTxt in findArr:
            pStr1 = 'Key:$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
            try:
                pStr2 = 'Key:' + strTxt + '( ' + str(rankData[strTxt]) + ')'
            except:
                pStr2 = 'Key:' + strTxt + '( )'
            print(pStr1)
            print(pStr2)
            print(pStr1)
            myfile.write('Start:' + nowStr + '\n')
            myfile.write(pStr1 + '\n')
            myfile.write(pStr2 + '\n')
            myfile.write(pStr1 + '\n')

            searchFlag = 'N'
            for pg in range(sIdx, eIdx):
                soup = get_soup(strTxt, pg)
                idx = 1
                for tag in soup.select('li'):
                    tagImg = tag.find(class_='img')
                    tagMid = tag.find(class_='_model_list _itemSection')
                    if tagImg:
                        # print(tagImg)
                        ct = tagImg.contents[1]
                        imgName = ct.get('alt')
                        pageurl = tagImg.attrs['href']

                        tagImgIdx = tag.text.find(strKey)

                        if tagImgIdx > -1:
                            fbIdx = tag.text.find('FLYBEACH')
                            fbsIdxH = tag.text.find('플라이비치')
                            site = None
                            if fbIdx > -1:
                                site = 'FLYBEACH    '
                            elif fbsIdxH > -1:
                                site = '플라이비치  '

                            adIdx = str(tag).find('ad _itemSection')
                            if adIdx < 1 and site is not None:
                                pStr = site
                                pStr += 'Page:' + println(str(pg), 5)
                                pStr += 'INDEX:' + println(str(idx), 5)
                                pStr += 'MID:'+println(tag.attrs['data-nv-mid'], 20)
                                pStr += '(' + str(imgName) + ')     ' + pageurl
                                searchFlag = 'Y'
                                print(pStr)
                                myfile.write(pStr + '\n')
                                searchFlag = 'Y'
                                break

                        idx += 1

                if pg % pagePrintCnt == 0:
                    print('Process Page:' + str(pg))

                if searchFlag == 'Y':
                    break

        end = datetime.datetime.now()
        endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
        print('End:' + endStr)
        print('Sub:' + str(end - now))
        myfile.write('End:' + endStr + '\n')
        myfile.write('Sub:' + str(end - now) + '\n')