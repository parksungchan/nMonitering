select *
from history
where 1=1
and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d')
-- and find_key like '%래쉬가드%'
-- and item like '%알로%'
;
select *
from history_pwlink
where 1=1
and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d')
-- and pc_mb = 'mb'
order by pc_mb, main_sub, idx
;
select *
from keywordR
;
select * from (
  select find_key
      , count(*) cnt
  from keywordR
  where 1=1
  group by find_key
) q
where cnt >1
;
select *
from keyword kw
where 1=1
and kw.find_key like '%왕뽕비키니%'
