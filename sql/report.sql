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
