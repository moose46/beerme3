-- bets definition

CREATE TABLE "bets" (
	"bet_id" INTEGER NOT NULL UNIQUE,
"race_date" TEXT NOT NULL,
"race_track" TEXT NOT NULL,
"greg_driver_name" TEXT NOT NULL,
"bob_driver_name" TEXT NOT NULL,
PRIMARY KEY("bet_id"),
UNIQUE("race_date", "race_track")
);
-- drivers definition

CREATE TABLE "drivers" (
	"driver_id" INTEGER NOT NULL UNIQUE,
"driver_name" TEXT NOT NULL UNIQUE,
"espn_driver_url" TEXT,
nascar_driver_url TEXT,
age INTEGER DEFAULT (-1) NOT NULL,
home_town TEXT,
sponsor TEXT,
team TEXT,
crew_chief TEXT,
PRIMARY KEY("driver_id" AUTOINCREMENT),
UNIQUE("driver_name", "espn_driver_url")
);

CREATE INDEX idx_driver_name_lower on
drivers(lower(driver_name));
-- teams definition

CREATE TABLE "teams" (
	"team_id" INTEGER NOT NULL UNIQUE,
"team_name" TEXT UNIQUE,
"team_url" TEXT,
PRIMARY KEY("team_id" AUTOINCREMENT),
UNIQUE("team_name")
);
-- tracks definition

CREATE TABLE "tracks" (
	"track_id" INTEGER NOT NULL UNIQUE,
"track_name" TEXT NOT NULL UNIQUE,
PRIMARY KEY("track_id" AUTOINCREMENT)
);
-- races definition

CREATE TABLE "races" (
	"race_id" INTEGER NOT NULL UNIQUE,
"track_id" INTEGER,
"race_date" TEXT NOT NULL UNIQUE,
"results_url" TEXT NOT NULL UNIQUE,
"race_name" TEXT,
race_track_name TEXT NOT NULL,
PRIMARY KEY("race_id" AUTOINCREMENT),
FOREIGN KEY("track_id") REFERENCES "tracks"("track_id")
);
-- results definition

CREATE TABLE "results" (
	"results_id" INTEGER NOT NULL UNIQUE,
"pos" INTEGER NOT NULL,
"driver_name" TEXT NOT NULL,
"start" INTEGER NOT NULL,
"race_id" INTEGER NOT NULL,
"manufacturer" TEXT,
"espn_driver_url" TEXT,
"driver_id" INTEGER NOT NULL,
"team_id" INTEGER,
team_name TEXT,
sponsor TEXT,
track_id INTEGER,
UNIQUE("driver_name", "race_id"),
PRIMARY KEY("results_id" AUTOINCREMENT),
FOREIGN KEY("driver_id") REFERENCES "drivers"("driver_id"),
FOREIGN KEY("race_id") REFERENCES "races"("race_id"),
FOREIGN KEY("team_id") REFERENCES "teams"("team_id")
);
