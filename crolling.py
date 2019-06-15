# True 이면 순위 체크 리스트 프린트 -> 지정 키워드가 프린트 된다.
# False 이면 지정 키워드가 프린트
nv_flag = True

def add_key(keyArr):
    for key in keyArr:
        keyList.append(key)
    return keyList
########################################################################################################################
keyList = []
# 스포츠/레저 > 수영 > 여성수영복 > 비키니
add_key( ['왕뽕비키니', '하이웨스트비키니', '비키니'] )
add_key( ['수영복', '여성수영복', '여자수영복'] )
add_key( ['원피스비키니', '비키니쇼핑몰', '비키니커버업', '수영복쇼핑몰', '수영복브랜드', '프릴비키니'] )
add_key( ['섹시비키니', '비키니브랜드', '비키니수영복', '비키니추천', '심플모노키니', '여자비키니', '여성비키니'] )

# 스포츠/레저 > 수영 > 여성수영복 > 원피스수영복
add_key( ['모노키니', '원피스수영복', '실내수영장수영복', '여자실내수영복', '실내수영복', '여성실내수영복'] )

# 스포츠/레저 > 수영 > 비치웨어 > 원피스
add_key( ['비치웨어', '비치원피스', '비치웨어쇼핑몰', '비치웨어브랜드'] )

# 스포츠/레저 > 수영 > 비치웨어 > 커플비치웨어
add_key( ['커플래쉬가드', '커플레쉬가드', '커플래시가드', '커플레시가드'] )
add_key( ['커플래쉬가드세트', '커플수영복', '커플비치웨어', '커플집업래쉬가드'] )
add_key( ['신혼여행커플룩'] )

# 스포츠/레저 > 수영 > 비치웨어 > 상의
add_key( ['래쉬가드', '레쉬가드', '래시가드', '레시가드'] )
add_key( ['래쉬가드추천', '수영복래쉬가드', '래쉬가드브랜드', '여성집업래쉬가드', '수영복래쉬가드', '루즈핏래쉬가드', '크롭래쉬가드'] )
add_key( ['여성래쉬가드', '여성레쉬가드', '여성래시가드', '여성레시가드'] )
add_key( ['여자래쉬가드', '여자레쉬가드', '여자래시가드', '여자레시가드'] )
add_key( ['집업래쉬가드', '집업레쉬가드', '집업래시가드', '집업레시가드'] )
add_key( ['남자래쉬가드', '남자레쉬가드', '남자래시가드', '남자레시가드'] )
add_key( ['남성래쉬가드', '남성레쉬가드', '남성래시가드', '남성레시가드'] )

########################################################################################################################
# Naver
keyNv = [
{'key': '커플수영복', 'name': '모던럭스 커플수영복'            , 'mid1': '17756448864', 'mid2': '80494526928', 'cnt': '1'}
,{'key': '커플수영복', 'name': '알로알로 커플수영복'            , 'mid1': '14482932189', 'mid2': '80494619031', 'cnt': '1'}
,{'key': '커플수영복', 'name': '나스카 커플수영복'            , 'mid1': '11617469511', 'mid2': '11614168937', 'cnt': '1'}

# ,{'key': '비치웨어', 'name': '신혼여행커플룩 허니문웨어'            , 'mid1': '12727818144', 'mid2': '11751841925', 'cnt': '11'}

,{'key': '래쉬가드', 'name': '플라이비치 비치서핑 캡소매 래쉬가드'            , 'mid1': '14483435845', 'mid2': '80452077802', 'cnt': '5'}
,{'key': '래쉬가드', 'name': '서프알로하 나시래쉬가드', 'mid1': '14489384918', 'mid2': '80495094273', 'cnt': '2'}

,{'key': '하이웨스트비키니', 'name': '브라우니 하이웨스트 비키니'            , 'mid1': '11713126134', 'mid2': '11882998599', 'cnt': '1'}
,{'key': '하이웨스트비키니', 'name': '트위 스트크롭 하이웨스트 비키니'            , 'mid1': '19377673584', 'mid2': '10047202087', 'cnt': '1'}
,{'key': '하이웨스트비키니', 'name': '하이웨스트비키니 모노키니 비키니 R77 FB1168'            , 'mid1': '10591394440', 'mid2': '10047202087', 'cnt': '3'}

,{'key': '비키니', 'name': '브라우니 하이웨스트 비키니'            , 'mid1': '11713126134', 'mid2': '11882998599', 'cnt': '2'}
,{'key': '비키니', 'name': '하이웨스트비키니 모노키니 비키니 R77 FB1168'            , 'mid1': '10591394440', 'mid2': '10047202087', 'cnt': '14'}

,{'key': '신혼여행커플룩', 'name': '신혼여행커플룩 허니문웨어'            , 'mid1': '12727818144', 'mid2': '11751841925', 'cnt': '1'}
]
########################################################################################################################



