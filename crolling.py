import crolling_util as crolling_util

sIdx = 1
eIdx = 2
strArr = []
# strArr.append('모노키니')
# ########################################################################################################################
# # 대표키워드
# ########################################################################################################################
# eIdx = 100
# # strArrKey = ['비치웨어']
# # strArr = crolling_util.get_strArr(strArr, strArrKey)
# #
# # strArrKey = ['커플래쉬가드', '래쉬가드']
# # strArr = crolling_util.get_strArr(strArr, strArrKey)
# #
# # strArrKey = ['모노키니', '비키니', '수영복']
# # strArr = crolling_util.get_strArr(strArr, strArrKey)
# #
# # strArrKey = ['비치원피스', '신혼여행커플룩']
# # strArr = crolling_util.get_strArr(strArr, strArrKey)
# #######################################################################################################################
# 래쉬가드
# #######################################################################################################################
strArrKey = ['', '커플', '여성', '여자', '남자', '남성']
strArrKeySub = ['래쉬가드', '레쉬가드', '래시가드', '레시가드']
strArr = crolling_util.get_strArr_sub(strArr, strArrKey, strArrKeySub)

strArrKey = ['래쉬가드추천', '래쉬가드브랜드', '커플래쉬가드추천', '래쉬가드세트', '여성래쉬가드세트', '커플래쉬가드세트']
strArr = crolling_util.get_strArr(strArr, strArrKey)

strArrKey = ['집업래쉬가드', '여성집업래쉬가드', '커플집업래쉬가드', '수영복래쉬가드', '루즈핏래쉬가드', '크롭래쉬가드']
strArr = crolling_util.get_strArr(strArr, strArrKey)
########################################################################################################################
# 비키니
########################################################################################################################
strArrKey = ['비키니','수영복', '모노키니', '원피스수영복', '여자실내수영복', '여자수영복', '실내수영장수영복', '여성수영복', '하이웨스트비키니']
strArr = crolling_util.get_strArr(strArr, strArrKey)

strArrKey = ['여름옷', '원피스비키니', '바캉스룩', '실내수영복', '커플수영복' ]
strArr = crolling_util.get_strArr(strArr, strArrKey)

strArrKey = ['프릴비키니', '비키니쇼핑몰', '섹시비키니', '여성실내수영복', '수영복쇼핑몰', '비키니브랜드', '왕뽕비키니']
strArr = crolling_util.get_strArr(strArr, strArrKey)
########################################################################################################################
# 신혼여행커플룩
########################################################################################################################
strArrKey = ['비치원피스', '비치웨어', '도트원피스', '바캉스원피스', '여름옷', '바캉스룩', '커플비치웨어', '로브가디건', '여름원피스', '해외여행여름옷']
strArr = crolling_util.get_strArr(strArr, strArrKey)




########################################################################################################################
# Main Function
########################################################################################################################
crolling_util.get_rank(strArr, sIdx, eIdx)




