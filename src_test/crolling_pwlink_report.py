import datetime, pymysql
from src_test.common import key_value as key_value

sIdx = 1
eIdx = 20
# 2018-07-06
now = datetime.date.today()
upStr = now.strftime("%Y-%m-%d")

def println(strTxt, cnt):
    if len(strTxt) > cnt:
        cnt = len(strTxt)+1
    return (strTxt + " " * cnt)[:cnt]

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
    curs = db.cursor()
    sql =  "select * from flybeach.history_pwlink "
    sql += "where update_date=%s  "
    sql += "order by pc_mb desc, main_sub, idx "
    curs.execute(sql, (upStr))
    rows = curs.fetchall()

    for row in rows:
        pStr = println(row[0].upper(), 5)
        pStr += println(row[1], 7)
        pStr += println(row[2], 30)
        pStr += println('idx:'+str(row[3]), 15)
        pStr += println('idxTotal:' + str(row[4]), 20)
        pStr += println('view:' + str(row[5]), 15)
        pStr += println('click:' + str(row[6]), 15)
        pStr += println('cost:' + str(row[7]), 15)
        pStr += println('total_cost:' + str(row[8]), 15)
        pStr += println('item:' + str(row[9]), 40)
        pStr += println('item_Desc:' + str(row[10]), 100)
        print(pStr)
















