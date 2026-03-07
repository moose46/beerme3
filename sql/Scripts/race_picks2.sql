
select
	race_date,
	track,
	(
	select
		(pos,
		driver)
	from
		nascar_results g
	where
		greg_pick = true
		and g.race_date = a.race_date
	group by
		pos,
		driver) as greg,
	(
	select
		(pos,
		driver)
	from
		nascar_results b
	where
		bob_pick = true
		and b.race_date = a.race_date) as bob
from
	public.nascar_results a
group by
	race_date,
	track