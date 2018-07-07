import datetime
import crolling as crolling
from common import crolling_util as crolling_util
import pymysql
from common import key_value as key_value
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
    sql += "order by pc_mb desc "
    curs.execute(sql)
    rowsKey = curs.fetchall()
    for rows in rowsKey:
        id = rows[0].upper() + ':' + rows[1]
        rankKey[id] = {'view': rows[2], 'click': rows[3], 'cost': rows[4], 'total_cost': rows[5]}

    curs = db.cursor()
    sql = "select * from flybeach.keywordR "
    curs.execute(sql)
    rowsKeyR = curs.fetchall()
    for rows in rowsKeyR:
        rankKeyR[rows[0]] = {'pc_cnt': rows[1], 'mb_cnt': rows[2]}
except:
    print('db connection error............................................')
    db = None

import crolling as crolling
from common import crolling_util as crolling_util
########################################################################################################################
# Main Function
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')

crolling_util.get_rank_pwlink(rowsKey, rankKey, rankKeyR, db)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))

# disconnect from server
if db is not None:
    db.close()