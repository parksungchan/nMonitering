import crolling as crolling
import crolling_util as crolling_util

logPath = 'logNv'
sIdx = 1
eIdx = 20
pagePrintCnt = 50
########################################################################################################################
# Main Function
########################################################################################################################
for keyJson in crolling.keyNv:
    print(keyJson)

print('')
for keyJson in crolling.keyNv:
    if keyJson['mid2'] == '':
        keyJson['mid2'] = '사용안함'
    print('검색명='+keyJson['key']+'상품명='+keyJson['mid1']+'구매처='+keyJson['mid2']+'페이지=1')
print('')

for keyJson in crolling.keyNv:
    crolling_util.get_rank_product(keyJson['item'], [keyJson['key']], sIdx, eIdx, pagePrintCnt, logPath)