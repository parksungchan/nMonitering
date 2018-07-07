import datetime
import crolling as crolling
from common import crolling_util as crolling_util

sIdx = 1
eIdx = 20
db, rowsKey, rowsKeyR, rankKey, rankKeyR = crolling_util.get_keyword_list()
########################################################################################################################
# Main Function 13.00
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')

findKeyArr = crolling.key # 검색 키워드
itemKeyArr = [] # 찾고자 하는 제품 키워드
# findKeyArr = ['비치원피스', '래쉬가드', '커플레쉬가드', '왕뽕비키니', '하이웨스트비키니', '비키니', '모노키니', '원피스수영복']
# itemKeyArr = ['FB1168']s

crolling_util.get_rank_common(sIdx, eIdx, findKeyArr, rankKey, rankKeyR, db)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))


# disconnect from server
if db is not None:
    db.close()