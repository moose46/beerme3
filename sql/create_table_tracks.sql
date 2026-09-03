-- tracks definition

CREATE TABLE "tracks" (
	"track_id"	INTEGER NOT NULL UNIQUE,
	"track_name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("track_id" AUTOINCREMENT)
);