select sum(race_results.points_awarded) as total, player_name
from race_results
where player_name is not null
group by player_name
