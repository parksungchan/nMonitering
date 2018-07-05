import datetime
import crolling as crolling
from common import crolling_util as crolling_util

logKeyPath = 'logPw'
########################################################################################################################
# Main Function
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')
findKeyArr = crolling.key
# findKeyArr = ['래쉬가드','비키니']
crolling_util.get_rank_pwlink(findKeyArr, logKeyPath)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))