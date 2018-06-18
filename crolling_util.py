import datetime
import requests
from bs4 import BeautifulSoup
import openpyxl
import os

file_path = 'D:\d_04python'
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
dirlist = sorted(os.listdir(file_path), reverse=True)
print('File Name:'+nowStr)

def get_strArr(strArr, strArrKey):
    for strStr in strArrKey:
        strArr.append(strStr)
    return strArr

def get_strArr_sub(strArr, strArrKey, strArrKeySub):
    for strR in strArrKey:
        for strRS in strArrKeySub:
            strArr.append(strR + strRS)
    return strArr

def get_rank(strArr, sIdx, eIdx):
    rankData = {}
    for dir in dirlist:
        file = file_path+'/'+dir
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


    with open(nowStr + ".txt", "a") as myfile:
        for strTxt in strArr:
            rd = {}
            if strTxt in rankData:
                rd = rankData[strTxt]

            pStr1 = 'Key:$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
            pStr2 = 'Key:' + strTxt + '( '+ str(rd) +')'
            print(pStr1)
            print(pStr2)
            print(pStr1)
            myfile.write(pStr1 + '\n')
            myfile.write(pStr2 + '\n')
            myfile.write(pStr1 + '\n')
            idx = 1
            for pg in range(sIdx, eIdx):
                url = 'https://search.shopping.naver.com/search/all.nhn?origQuery=' + strTxt
                url += '&pagingIndex=' + str(pg) + '&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=' + strTxt
                html = requests.get(url).text
                # print(html)
                soup = BeautifulSoup(html, 'html.parser')
                for tag in soup.select('li'):
                    tagImg = tag.find(class_='img')
                    if tagImg:
                        # print(tagImg)
                        ct = tagImg.contents[1]
                        imgName = ct.get('alt')
                        pageurl = tagImg.attrs['href']
                        tagImgIdx = tag.text.find('FLYBEACH')
                        tagImgIdxH = tag.text.find('플라이비치')
                        if tagImgIdx > -1:
                            adIdx = str(tag).find('ad _itemSection')
                            if adIdx > 0:
                                pStr = 'FLYBEACH   Page(광고):' + str(pg) + '    (' + str(imgName) + ')' + pageurl
                            else:
                                pStr = 'FLYBEACH   Page:' + str(pg) + '    (' + str(imgName) + ')' + pageurl
                            print(pStr)
                            myfile.write(pStr + '\n')
                        elif tagImgIdxH > -1:
                            adIdx = str(tag).find('ad _itemSection')
                            if adIdx > 0:
                                pStr = '플라이비치 Page(광고):' + str(pg) + '    (' + str(imgName) + ')' + pageurl
                            else:
                                pStr = '플라이비치 Page:' + str(pg) + '    (' + str(imgName) + ')' + pageurl
                            print(pStr)
                            myfile.write(pStr + '\n')
                        idx += 1

