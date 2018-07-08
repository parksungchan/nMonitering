import datetime
from common import crolling_util as crolling_util
########################################################################################################################
# Main Function
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')

# db, rowsKey, rowsKeyR, rankKey, rankKeyR = crolling_util.get_keyword_list('pc')
# crolling_util.get_rank_pwlink(rowsKey, rankKey, rankKeyR, db)

db, rowsKey, rowsKeyR, rankKey, rankKeyR = crolling_util.get_keyword_list('mb')
crolling_util.get_rank_pwlink_mb(rowsKey, rankKey, rankKeyR, db)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))

# disconnect from server
if db is not None:
    db.close()