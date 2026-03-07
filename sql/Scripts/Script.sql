	select
		nr.bob_pick , nr.greg_pick ,nr.race_date 
	from
		nascar_results nr
	where 
		nr.greg_pick = true
		and nr.bob_pick = true
	group by nr.race_date , nr.bob_pick ,nr.greg_pick 
--		and nr.race_date = a.race_date
