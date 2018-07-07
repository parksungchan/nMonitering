import datetime, pymysql
import crolling as crolling
from common import key_value as key_value
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
    sql += "where update_date=%s  and pc_mb=%s "
    sql += "order by idx "
    curs.execute(sql, (upStr, 'pc'))
    rows = curs.fetchall()

    for row in rows:
        rd = ''
        if row[0] in crolling.rankData.keys():
            rd = str(crolling.rankData[row[0]])
        strTxtPrint = row[0] + ' (' + rd + ')'
        print(println(row[8],5)+':'+println(strTxtPrint,50) + println(str(row[2])+' Index',20) + println(row[3],30) + println(row[4],30))
















