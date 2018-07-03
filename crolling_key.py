import datetime
import crolling as crolling
import crolling_util as crolling_util

logKeyPath = 'logKey'
pageFlag = True # True :page import, False:key import

sIdx = 19
eIdx = 19
########################################################################################################################
# Main Function
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')

findKeyArr = crolling.key # 검색 키워드
itemKeyArr = crolling.key # 찾고자 하는 제품 키워드
crolling_util.get_rank_common(sIdx, eIdx, findKeyArr, itemKeyArr, logKeyPath, pageFlag)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))
