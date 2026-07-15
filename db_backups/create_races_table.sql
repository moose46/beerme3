-- public.races definition

-- Drop table

-- DROP TABLE public.races;

CREATE TABLE public.races (
	race_id int4 DEFAULT nextval('seq_race_id'::regclass) NOT NULL,
	race_date date NOT NULL,
	race_name varchar NOT NULL,
	track_id int4 NOT NULL,
	television varchar NULL,
	race_winner varchar NULL,
	CONSTRAINT races_pk PRIMARY KEY (race_id)
);


-- public.races foreign keys

ALTER TABLE public.races ADD CONSTRAINT races_tracks_fk FOREIGN KEY (track_id) REFERENCES public.tracks(id);