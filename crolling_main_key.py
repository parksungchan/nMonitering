import datetime
import crolling as crolling
from common import crolling_util as crolling_util

sIdx = 1
eIdx = 100
db, rowsKey, rowsKeyR, rankKey, rankKeyR = crolling_util.get_keyword_list()
########################################################################################################################
# 네이버 쇼핑 검색 키워드에 제품이 몇위에 있는지를 확인 할 수 있다.
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')

findKeyArr = ['래쉬가드', '비키니','모노키니','하이웨스트비키니']
crolling_util.get_rank_common(sIdx, eIdx, findKeyArr, rankKey, rankKeyR, db)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))


# disconnect from server
if db is not None:
    db.close()