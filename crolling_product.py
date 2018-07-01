import crolling_util as crolling_util

sIdx = 1
eIdx = 10
strType = []
strArr = []

RG = ['커플래쉬가드', '커플레쉬가드', '커플수영복']
RG = crolling_util.get_strArr(strArr, RG)
RG = ['래쉬가드', '래쉬가드추천', '래쉬가드브랜드', '래쉬가드세트', '집업래쉬가드', '수영복래쉬가드', '여성래쉬가드', '여자래쉬가드', '여성래쉬가드세트', '여성집업래쉬가드']
RG = crolling_util.get_strArr(strArr, RG)

VK = ['왕뽕비키니', '모노키니', '하이웨스트비키니', '비키니', '수영복', ' 여성수영복', '여자수영복']
VK = crolling_util.get_strArr(strArr, VK)
VK = ['원피스수영복', '원피스비키니', '실내수영복', '비키니쇼핑몰', '섹시비키니', '비키니브랜드', '수영복쇼핑몰', '실내수영장수영복']
VK = crolling_util.get_strArr(strArr, VK)

OP = ['신혼여행커플룩', '커플비치웨어', '비치웨어', '비치원피스', '비치드레스']
# ########################################################################################################################
# # 대표제품
# ########################################################################################################################
# 왕뽕 하이웨스트 비키니 모노키니
# 래쉬가드추천 R52 (여성레쉬가드)
# R53 커플수영복 커플레쉬가드
# [플라이비치]신혼여행커플룩,허니문웨어
# 신혼여행커플룩 허니문커플룩
# [플라이비치] 비치원피스 여름원피스


strArr = ['왕뽕 하이웨스트']
crolling_util.get_rank_product(strArr, VK, sIdx, eIdx)
#
# strArr = ['R53', 'R52']
# crolling_util.get_rank_product(strArr, RG, sIdx, eIdx)

# strArr = ['신혼여행커플룩', '비치원피스']
# crolling_util.get_rank_product(strArr, OP, sIdx, eIdx)


