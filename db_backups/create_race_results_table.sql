-- public.race_results definition
-- Drop table
-- DROP TABLE race_results;

create table race_results (
	id int2 default nextval('seq_race_results_id'::regclass) not null,
	race_id int2 not null,
	driver varchar not null,
	pos int4 not null,
	greg_pick bool null,
	bob_pick bool null,
	constraint race_results_pk primary key (id),
	constraint race_results_unique unique (race_id,
driver),
	constraint race_results_unique_1 unique (pos,
race_id),
	constraint race_results_unique_2 unique (race_id,
driver,
greg_pick),
	constraint race_results_unique_3 unique (race_id,
driver,
bob_pick)
);
-- public.race_results foreign keys

alter table public.race_results add constraint race_results_races_fk foreign key (race_id) references races(race_id);
