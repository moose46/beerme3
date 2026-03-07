
select
	race_date,
	track,
	(
	select
		(pos)
	from
		nascar_results g
	where
		greg_pick = true
		and g.race_date = a.race_date
	) as greg_pos,
	(
	select
		(driver)
	from
		nascar_results g
	where
		greg_pick = true
		and g.race_date = a.race_date
	) as greg_driver,
	(
	select
		(pos)
	from
		nascar_results b
	where
		bob_pick = true
		and b.race_date = a.race_date) as bob_pos,
	(
	select
		(driver)
	from
		nascar_results g
	where
		bob_pick = true
		and g.race_date = a.race_date
	) as bob_driver
from
	public.nascar_results a
group by
	race_date,
	track
