select *
from history_pwlink
where 1=1
and update_date = DATE_FORMAT(NOW(),'%Y-%m-%d')
-- and pc_mb = 'mb'
-- order by idx_total,cost,pc_mb, main_sub, idx
-- order by idx
order by total_cost desc
;


