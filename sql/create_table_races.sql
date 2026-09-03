-- races definition

CREATE TABLE "races" (
	"race_id"	INTEGER NOT NULL UNIQUE,
	"track_id"	INTEGER,
	"race_date"	TEXT NOT NULL UNIQUE,
	"results_url"	TEXT NOT NULL UNIQUE,
	"race_name"	TEXT,
	PRIMARY KEY("race_id" AUTOINCREMENT),
	FOREIGN KEY("track_id") REFERENCES "tracks"("track_id")
);