import crolling_util as crolling_util

sIdx = 1
eIdx = 30
pagePrintCnt = 50
strType = []
strArr = []
# 스포츠/레저 > 수영 > 비치웨어 > 커플비치웨어
BW_CP = ['커플래쉬가드', '커플레쉬가드', '커플수영복', '커플비치웨어', '신혼여행커플룩']

# 스포츠/레저 > 수영 > 비치웨어 > 상의
BW_TOP = ['래쉬가드', '여성래쉬가드', '여자래쉬가드', '래쉬가드추천', '집업래쉬가드', '수영복래쉬가드']
BW_TOP1 = ['루즈핏래쉬가드', '래쉬가드브랜드', '여성집업래쉬가드']
BW_TOP = crolling_util.add_key(BW_TOP, BW_TOP1)

# 스포츠/레저 > 수영 > 비치웨어 > 상하세트
BW_TOP_SET = ['래쉬가드세트', '여성래쉬가드세트']

# 스포츠/레저 > 수영 > 여성수영복 > 비키니
VK = ['왕뽕비키니', '하이웨스트비키니', '비키니', '수영복', ' 여성수영복', '여자수영복', '원피스비키니', '비키니쇼핑몰', '비키니커버업']
VK1 = ['수영복쇼핑몰', '수영복브랜드', '수영복쇼핑몰', '섹시비키니', '비키니브랜드', '비키니수영복', '여자비키니', '비키니추천', '심플모노키니']
VK = crolling_util.add_key(VK, VK1)

# 스포츠/레저 > 수영 > 여성수영복 > 원피스수영복
VK_OP = ['모노키니', '원피스수영복', '실내수영복', '실내수영장수영복', '여자실내수영복', '여성실내수영복']

# 스포츠/레저 > 수영 > 비치웨어 > 원피스
OP = ['비치웨어', '비치원피스']

# 
# ########################################################################################################################
# # 대표제품
# ########################################################################################################################
# 왕뽕 하이웨스트 비키니 모노키니
# 래쉬가드추천 R52 (여성레쉬가드)
# R53 커플수영복 커플레쉬가드
# [플라이비치]신혼여행커플룩,허니문웨어
# 신혼여행커플룩 허니문커플룩
# [플라이비치] 비치원피스 여름원피스

# 래쉬가드추천 ( 여성레쉬가드 ) FB1168_R52
strArr = 'R52'
crolling_util.get_rank_product(strArr, BW_TOP, sIdx, eIdx, pagePrintCnt)

# 여성레쉬가드 래쉬가드 FB1168_R55
strArr = 'FB1168'
crolling_util.get_rank_product(strArr, BW_TOP, sIdx, eIdx, pagePrintCnt)

# 커플레쉬가드 커플수영복 FB1168_R54
strArr = 'R54'
crolling_util.get_rank_product(strArr, BW_CP, sIdx, eIdx, pagePrintCnt)
########################################################################################################################
# 왕뽕 하이웨스트 비키니 모노키니 FB1168_R57
strArr = '왕뽕 하이웨스트'
crolling_util.get_rank_product(strArr, VK, sIdx, eIdx, pagePrintCnt)

# 왕뽕 원피스수영복 모노키니 FB1168_R56
strArr = 'FB1168'
crolling_util.get_rank_product(strArr, VK_OP, sIdx, eIdx, pagePrintCnt)
########################################################################################################################
# 신혼여행커플룩 허니문커플룩
# [플라이비치] 신혼여행커플룩 허니문커플룩
# [플라이비치]신혼여행커플룩,허니문웨어
strArr = '신혼여행커플룩'
crolling_util.get_rank_product(strArr, BW_CP, sIdx, eIdx, pagePrintCnt)




