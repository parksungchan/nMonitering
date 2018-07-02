import crolling as crolling
import crolling_util as crolling_util

logPath = 'logMain'
sIdx = 1
eIdx = 30
pagePrintCnt = 50
strArr = []
# ########################################################################################################################
# # 대표제품
# ########################################################################################################################
# 커플레쉬가드 커플수영복 FB1168_R54
strArr = 'R54'
crolling_util.get_rank_product(strArr, crolling.BW_CP, sIdx, eIdx, pagePrintCnt, logPath)

# 래쉬가드추천 ( 여성레쉬가드 ) FB1168_R52
# 여성레쉬가드 래쉬가드 FB1168_R55
strArr = 'R52'
crolling_util.get_rank_product(strArr, crolling.BW_TOP, sIdx, eIdx, pagePrintCnt, logPath)
########################################################################################################################
# 왕뽕 하이웨스트 비키니 모노키니 FB1168_R57
strArr = '왕뽕 하이웨스트'
crolling_util.get_rank_product(strArr, crolling.VK, sIdx, eIdx, pagePrintCnt, logPath)

# 왕뽕 원피스수영복 모노키니 FB1168_R56
strArr = 'FB1168'
crolling_util.get_rank_product(strArr, crolling.VK_OP, sIdx, eIdx, pagePrintCnt, logPath)
########################################################################################################################
# 신혼여행커플룩 허니문커플룩
# [플라이비치] 신혼여행커플룩 허니문커플룩
strArr = '신혼여행커플룩 허니문커플룩'
crolling_util.get_rank_product(strArr, crolling.BW_CP, sIdx, eIdx, pagePrintCnt, logPath)

# [플라이비치]신혼여행커플룩,허니문웨어
strArr = '[플라이비치] 신혼여행커플룩 허니문커플룩'
crolling_util.get_rank_product(strArr, crolling.BW_CP, sIdx, eIdx, pagePrintCnt, logPath)
########################################################################################################################
# 비치원피스 비치웨어 FB1168_R58
strArr = 'FB1168'
crolling_util.get_rank_product(strArr, crolling.OP, sIdx, eIdx, pagePrintCnt, logPath)




