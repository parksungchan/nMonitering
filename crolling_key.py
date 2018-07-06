import datetime
import pymysql
from common import key_value as key_value
sIdx = 1
eIdx = 20
# Open database connection
try:
    db = pymysql.connect(host=key_value.host
                         , port=key_value.port
                         , user=key_value.user
                         , passwd=key_value.password
                         , db=key_value.db
                         , charset=key_value.charset
                         , autocommit=True)
except:
    print('db connection error............................................')
    db = None

if db is not None:
    import crolling as crolling
    from common import crolling_util as crolling_util
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

    crolling_util.get_rank_common(sIdx, eIdx, findKeyArr, db)

    print('')
    end = datetime.datetime.now()
    endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
    print('End:' + endStr)
    print('Sub:' + str(end - now))


    # disconnect from server
    if db is not None:
        db.close()