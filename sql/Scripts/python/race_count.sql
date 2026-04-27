--python script RACE_COUNT sql_statements.py
select
	count(*)
from
	(
	select
		nr.race_date
	from
		nascar_results nr
	group by
		nr.race_date 
)