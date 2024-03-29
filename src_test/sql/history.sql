-- 당일 이력 리스트를 보여준다.
select *
from history
where 1=1
and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d')
-- and find_key like '%래쉬가드%'
-- and item like '%알로%'
and find_key not in('신혼여행커플룩')
order by page,find_key
;
-- 특정 키워드의 이력을 보여준다.
--  {'key':'커플래쉬가드'       , 'name':'비치서핑 래쉬가드'                   , 'mid1':'14638288265', 'mid2':'80452092166', 'cnt':'2'}
-- ,{'key':'래쉬가드'           , 'name':'서프알로하 나시래쉬가드'             , 'mid1':'14489384918', 'mid2':'80495094273', 'cnt':'3'}
-- ,{'key':'커플레쉬가드'       , 'name':'서프알로하 래쉬가드(커플상의) '      , 'mid1':'14420533996', 'mid2':'', 'cnt':'8'}
-- ,{'key':'래쉬가드'           , 'name':'래쉬가드추천 FB1168_R52'             , 'mid1':'14705104256', 'mid2':'9954709419', 'cnt':'5'}
-- ,{'key':'왕뽕비키니'         , 'name':'왕뽕 하이웨스트 비키니 모노키니'     , 'mid1':'10591394440', 'mid2':'10054140280', 'cnt':'3'}
-- ,{'key':'커플수영복'         , 'name':'블루에스닉 커플수영복'               , 'mid1':'14595351003', 'mid2':'', 'cnt':'6'}
-- ,{'key':'모노키니'           , 'name':'크로스 모노키니'                     , 'mid1':'14355364202', 'mid2':'80418993407', 'cnt':'6'}
-- ,{'key':'신혼여행커플룩'     , 'name':'신혼여행커플룩 허니문웨어'           , 'mid1':'12727818144', 'mid2':'11751841925', 'cnt':'1'}
-- ,{'key':'모노키니'           , 'name':'섹시오프 모노키니'                   , 'mid1':'14616533726', 'mid2':'80494394781', 'cnt':'17'}
-- ,{'key':'비치원피스'         , 'name':'플라이비치 비치원피스 여름'          , 'mid1':'10926541260', 'mid2':'80657855013', 'cnt':'6'}
select * from history where mid1 = 14638288265 and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d') order by update_date desc, page, idx;
select * from history where mid1 = 14489384918 and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d') order by update_date desc, page, idx;
select * from history where mid1 = 14420533996 and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d') order by update_date desc, page, idx;
select * from history where mid1 = 14705104256 and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d') order by update_date desc, page, idx;
select * from history where mid1 = 10591394440 and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d') order by update_date desc, page, idx;
select * from history where mid1 = 14595351003 and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d') order by update_date desc, page, idx;
select * from history where mid1 = 14355364202 and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d') order by update_date desc, page, idx;
select * from history where mid1 = 12727818144 and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d') order by update_date desc, page, idx;
select * from history where mid1 = 14616533726 and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d') order by update_date desc, page, idx;
select * from history where mid1 = 10926541260 and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d') order by update_date desc, page, idx;
;
select *
from history
where mid1 = '10926541260'
-- and find_key = '래쉬가드'
order by update_date desc


