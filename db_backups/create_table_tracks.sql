-- public.tracks definition
-- Drop table
-- DROP TABLE tracks;

create table tracks (
	track_name varchar not null,
	id int4 default nextval('seq_track_id'::regclass) not null,
	constraint track_pk primary key (id),
	constraint track_unique unique (track_name)
);
