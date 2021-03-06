select *
from history_pwlink
where 1=1
-- and cost not in(70)
-- and pc_mb like '%pc%'
-- and idx like 16
-- and pc_mb like '%mb%'
-- and (find_key like '%래쉬가드%' or find_key like '%래쉬가드%')
and item like '%플라이비치%'
and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d')
-- and pc_mb = 'mb'
-- order by idx_total,cost,pc_mb, main_sub, idx
order by pc_mb desc,idx asc
-- order by total_cost desc
;



-- -- 특정 키워드 뽑는 sql
-- select *
-- from history_pwlink
-- where 1=1
-- and cost not in(70)
-- and pc_mb like '%pc%'
-- -- and idx like 16
-- 
-- -- and pc_mb like '%mb%'
-- and find_key in( '비키니','모노키니','커플수영복','해외여행커플룩','해외여행비치웨어','칸쿤원피스','허니문비키니','허니문원피스','비키니커플','하와이커플룩','신혼여행커플웨어','커플수영복세트','해외여행비키니','해외여행옷','신혼여행커플수영복','신혼여행드레스','신혼여행커플웨어','신혼여행비치룩','신혼여행옷','칸쿤커플룩','해외여행시밀러룩','보라카이원피스','보라카이커플룩','여름커플룩','여름시밀러룩','휴양지원피스','하와이원피스','해외여행원피스','하와이커플룩','커플나시','커플허니문룩','신혼여행시밀러룩','여름원피스쇼핑몰', '여름맥시원피스', '여름원피스추천', '여름수영복','여름비키니', '여름원피스','여자여름옷','여름바캉스룩')
-- and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d')
-- and pc_mb = 'mb'
-- order by idx_total,cost,pc_mb, main_sub, idx
-- ;



-- -- 특정 키워드와 순위뽑는 sql (asc가 오름차순, desc가 내림차순)
-- select *
-- from history_pwlink
-- where 1=1
-- -- and cost not in(70)
-- -- and pc_mb like '%pc%'
-- -- and idx like 16
-- 
-- and find_key like '%해외%'
-- -- and idx > 15
-- 
-- and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d')
-- -- and pc_mb = 'mb'
-- -- order by idx_total,cost,pc_mb, main_sub, idx
-- order by pc_mb desc,idx asc
-- -- order by total_cost desc
-- ;
-- 


-- -- ★순위안에 표시 안되는 제품 ★ --
-- select kw.*
-- from keyword kw
-- where 1=1
-- and NOT EXISTS (
--   select *
--   from history_pwlink pw
--   where  kw.pc_mb = pw.pc_mb
--   and kw.find_key = pw.find_key
--   and pw.update_date = DATE_FORMAT(NOW(),'%Y-%m-%d')
-- )
-- and find_key in( '비키니','해외여행커플룩','해외여행비치웨어','칸쿤원피스','허니문비키니','허니문원피스','비키니커플','하와이커플룩','신혼여행커플웨어','커플수영복세트','해외여행비키니','해외여행옷','신혼여행커플수영복','신혼여행드레스','신혼여행커플웨어','신혼여행비치룩','신혼여행옷','칸쿤커플룩','해외여행시밀러룩','보라카이원피스','보라카이커플룩','여름커플룩','여름시밀러룩','휴양지원피스','하와이원피스','해외여행원피스','하와이커플룩','커플나시','커플허니문룩','신혼여행시밀러룩')
-- order by kw.pc_mb, kw.find_key
-- ;
