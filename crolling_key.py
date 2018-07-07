import datetime
import pymysql
import crolling as crolling
from common import crolling_util as crolling_util
from common import key_value as key_value
sIdx = 1
eIdx = 20
rankKey = {}
rankKeyR = {}
# Open database connection
try:
    db = pymysql.connect(host=key_value.host
                         , port=key_value.port
                         , user=key_value.user
                         , passwd=key_value.password
                         , db=key_value.db
                         , charset=key_value.charset
                         , autocommit=True)

    curs = db.cursor()
    sql = "select * from flybeach.keyword "
    curs.execute(sql)
    rowsKey = curs.fetchall()
    for rows in rowsKey:
        id = rows[0].upper() + ':' + rows[1]
        rankKey[id] = {'view':rows[3], 'click':rows[4], 'cost':rows[2], 'total_cost':rows[5]}

    curs = db.cursor()
    sql = "select * from flybeach.keywordR "
    curs.execute(sql)
    rowsKeyR = curs.fetchall()
    for rows in rowsKeyR:
        rankKeyR[rows[0]] = {'pc_cnt': rows[1], 'mb_cnt': rows[2]}
except:
    print('db connection error............................................')
    db = None
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

crolling_util.get_rank_common(sIdx, eIdx, rankKey, rankKeyR, findKeyArr, db)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))


# disconnect from server
if db is not None:
    db.close()