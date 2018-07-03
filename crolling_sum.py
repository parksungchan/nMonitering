import datetime
import crolling as crolling
import crolling_util as crolling_util

logKeyPath = 'logSum'
pageFlag = True # True :page import, False:key import

sIdx = 1
eIdx = 100
########################################################################################################################
# Main Function
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')

findKeyArr = [] # 검색 키워드
itemKeyArr = [] # 찾고자 하는 제품 키워드

# 커플레쉬가드 커플수영복 FB1168_R54
# 신혼여행커플룩 허니문커플룩
# [플라이비치] 신혼여행커플룩 허니문커플룩
# [플라이비치]신혼여행커플룩,허니문웨어
# 여성레쉬가드 래쉬가드 FB1168_R55
# 래쉬가드추천 ( 여성레쉬가드 ) FB1168_R52
# 왕뽕 하이웨스트 비키니 모노키니 FB1168_R57
# 왕뽕 원피스수영복 모노키니 FB1168_R56
# 비치원피스 비치웨어 FB1168_R58
# [플라이비치] 비치원피스 여름원피스

findKeyArr = crolling.key # 검색 키워드
itemKeyArr = ['FB1168', '왕뽕 하이웨스트', '신혼여행커플룩 허니문커플룩', '[플라이비치] 신혼여행커플룩 허니문커플룩']
crolling_util.get_rank_common(sIdx, eIdx, findKeyArr, itemKeyArr, logKeyPath, pageFlag)

