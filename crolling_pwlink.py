import datetime
import crolling as crolling
from common import crolling_util as crolling_util
import pymysql
from common import key_value as key_value
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
    # Main Function
    ########################################################################################################################
    now = datetime.datetime.now()
    nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
    print('Start:'+nowStr)
    print('')
    findKeyArr = crolling.key
    findKeyArr = ['레쉬가드','래시가드']
    crolling_util.get_rank_pwlink(findKeyArr, db)

    print('')
    end = datetime.datetime.now()
    endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
    print('End:' + endStr)
    print('Sub:' + str(end - now))

    # disconnect from server
    if db is not None:
        db.close()