select *
from keyword kw
where 1=1
-- and kw.find_key like '%하바나%'
order by kw.pc_mb desc, view desc
;
select *
from keywordR
where 1=1 
and find_key != '연관키워드'
and find_key like '%해외여행%'
-- and find_key ='커플래쉬가드'
order by cast(replace(replace(pc_cnt,'<10', '10'),',','') as unsigned) desc




