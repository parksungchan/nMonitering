import datetime
import crolling as crolling
from common import crolling_util as crolling_util

sIdx = 1
eIdx = 20
db, rowsKey, rowsKeyR, rankKey, rankKeyR = crolling_util.get_keyword_list()
########################################################################################################################
# Main Function 13.00
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')

findKeyArr = crolling_util.get_key_nv_list()
# findKeyArr = ['커플래쉬가드']
crolling_util.get_rank_common(sIdx, eIdx, findKeyArr, rankKey, rankKeyR, db)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))


# disconnect from server
if db is not None:
    db.close()