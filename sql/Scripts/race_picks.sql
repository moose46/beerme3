
select
	track,
	driver,
	pos,
	case
		when greg_pick = true then 'GREG'
		when bob_pick = true then 'BOB'
	end as pick
from
		nascar_results nr
where
		nr.greg_pick is not false
	or bob_pick is not false

order by
		race_date,pos