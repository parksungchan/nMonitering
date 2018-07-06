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

import crolling as crolling
from common import crolling_util as crolling_util
########################################################################################################################
# Main Function
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')

pwLinkDataPc, pwLinkDataMb = crolling.get_rank_key_pwlink()
pwLinkDataPc = ['10CM왕뽕비키니', '래쉬가드']
crolling_util.get_rank_pwlink(pwLinkDataPc, db, 'pc')

pwLinkDataMb = ['20대비키니쇼핑몰']
crolling_util.get_rank_pwlink(pwLinkDataMb, db, 'mb')

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))

# disconnect from server
if db is not None:
    db.close()