import datetime
import crolling as crolling
from common import crolling_util as crolling_util

logKeyPath = 'logNv'

sIdx = 1
eIdx = 20
########################################################################################################################
# Main Function
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')
for keyJson in crolling.keyNv:
    pStr  = crolling_util.println('Key:' + keyJson['key'], 30)
    pStr += crolling_util.println('Name:' + keyJson['name'], 40)
    pStr += crolling_util.println('Mid1:' + keyJson['mid1'], 30)
    pStr += crolling_util.println('Mid2:' + keyJson['mid2'], 30)
    pStr += keyJson['cnt']
    print(pStr)
print('')

findKeyArr = [] # 검색 키워드
itemKeyArr = [] # 찾고자 하는 제품 키워드
for keyJson in crolling.keyNv:
    if keyJson['key'] in findKeyArr:
        None
    else:
        findKeyArr.append(keyJson['key'])

    if keyJson['mid1'] in itemKeyArr:
        None
    else:
        itemKeyArr.append(keyJson['mid1'])

    if keyJson['mid2'] == '':
        keyJson['mid2'] = '사용안함'
    print('검색명=' + keyJson['key'] + '상품명=' + keyJson['mid1'] + '구매처=' + keyJson['mid2'] + '페이지=' + keyJson['cnt'])
print('')

crolling_util.get_rank_common(sIdx, eIdx, findKeyArr, itemKeyArr, logKeyPath)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))