
select
	 to_char(race_date,'MM/DD/YYYY'),
--	 to_char(race_date,'DD/MM/YYYY'),
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
	) as bob_driver,
	(
	select
		pos
	from
		nascar_results nr
	where
		nr.greg_pick = true
		and pos = 1
		and nr.race_date = a.race_date ) as greg_first_place,
	(
	select
		pos
	from
		nascar_results nr
	where
		nr.bob_pick = true
		and pos = 1
		and nr.race_date = a.race_date) as bob_first_place
	--	select the winner
	--	end of select the winner
from
	public.nascar_results a
group by
	race_date,
	track
order by race_date