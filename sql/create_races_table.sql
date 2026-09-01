-- races definition

CREATE TABLE "races" (
	"race_id" INTEGER NOT NULL UNIQUE,
"track_id" INTEGER,
"race_date" TEXT NOT NULL,
"results_url" TEXT NOT NULL,
"race_name" TEXT,
"race_track_name" TEXT NOT NULL,
PRIMARY KEY("race_id" AUTOINCREMENT),
FOREIGN KEY("track_id") REFERENCES "tracks"("track_id")
);

CREATE UNIQUE INDEX races_track_id_IDX ON
races (track_id,
race_date,
race_name);
