import datetime
from src_test.common import crolling_util as crolling_util

########################################################################################################################
# 파워링크 광고 부분에 몇위에 있는지를 알 수 있다.
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')

db, rowsKey, rowsKeyR, rankKey, rankKeyR = crolling_util.get_keyword_list()
crolling_util.get_rank_pwlink(rowsKey, rankKey, rankKeyR, db)

# db, rowsKey, rowsKeyR, rankKey, rankKeyR = crolling_util.get_keyword_list('mb')
# crolling_util.get_rank_pwlink_mb(rowsKey, rankKey, rankKeyR, db)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))

# disconnect from server
if db is not None:
    db.close()