select *
from history
where 1=1
and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d')
-- and find_key like '%래쉬가드%'
-- and item like '%알로%'
order by page
