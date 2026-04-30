"""
python load_csv_db.py
hydrates the nascar_results from data/mm-dd-yyyy.csv files
bets[mm-dd-yyyy] must have the current race and bet data first
run scrape_espn.py before running this file

"""
import csv
from collections import defaultdict
from pathlib import Path
from typing import Any

import betData2026
from betData2026 import BetData
import psycopg

import db_connection as postgres_db

TARGET_RESULTS = (
    r"C:\Users\me\PycharmProjects\BeerMe3\data"
)


class CsvDB:
    def __init__(self, bets_2026):
        self.connection = psycopg.connect(
            dbname="beerme3",
            user="bob",
            password="admin",
            host="localhost",  # or your database server's IP
            port="5432"  # default PostgreSQL port
        )
        print("Connection successful!")
        self.cursor = self.connection.cursor()
        self.bets: dict = defaultdict(dict)
        # self.Bets = BetData()
        self.bets = bets_2026
        self.track_id = 0  # current track_id
        self.tracks_found = 0
        self.results_loaded = 0
        self.races_scored = 0

    def read_csv_race_results(self, abet):
        # abet is one bet from a list of bets
        results_file_name: str = f"{TARGET_RESULTS}\\{abet}.csv"
        track_id = self.get_track_id(track_name=self.bets[abet]["Track"])
        with open(Path(f"{TARGET_RESULTS}\\{abet}.csv"), "r") as file:
            reader = csv.DictReader(file, delimiter="\t")
            for row in reader:
                bob_pick = False
                greg_pick = False
                if row["DRIVER"] == self.bets[abet]["Greg"]:
                    print(
                        f"Greg Picked {self.bets[abet]["Track"]} "
                        f"{row['DRIVER']} {row['POS']}")
                    greg_pick = True
                if row["DRIVER"] == self.bets[abet]["Bob"]:
                    print(
                        f"Bob Picked {self.bets[abet]["Track"]} "
                        f"{row['DRIVER']} {row['POS']}")
                    bob_pick = True
                # print(f"4. Processing {row} {self.bets[abet]['Greg']}")
                try:
                    self.cursor.execute("""
                                        insert into nascar_results
                                        (race_date, driver, pos,
                                         greg_pick, bob_pick, track,
                                         track_id)
                                        values (%s, %s, %s, %s, %s, %s, %s)
                                        """,
                                        (
                                            abet,
                                            row['DRIVER'],
                                            row['POS'],
                                            greg_pick,
                                            bob_pick,
                                            self.bets[abet]["Track"],
                                            track_id
                                        )
                                        )
                    self.connection.commit()
                    self.results_loaded += 1
                except Exception as e1:
                    exit(e1.__str__())

        return results_file_name

    def get_track_id(self, track_name):
        sql = "select id from track where track_name = %s"
        self.cursor.execute(sql, (track_name,))
        try:
            return self.cursor.fetchone()[0]
        except Exception as eGetTrackId:
            exit(eGetTrackId.__str__())
    @property
    def get_bets(self):
        return self.bets

    def hydrate_track_table(self, track):
        """
        Check to see if track exists in the track table
        if it does not exist , create it and return the track id
        else return the track id
        :param track:
        """
        try:
            sql = """
                  insert into track (track_name, id)
                  select %s, nextval('seq_track_id')
                  where not exists  (select track_name
                                     from track
                                     where track_name = %s)
                  """
            self.cursor.execute(sql, (track, track))
            self.connection.commit()
            self.tracks_found += 1
            return track
        except Exception as e:
            self.connection.rollback()
            exit(e.__str__())

    def check_if_race_is_already_loaded(self, thebet) -> bool | Any:
        # checks the nascar_results table for thebet.track and thebet race_date
        # returns true if found, false if not found
        cnt = 0
        try:
            sql = """
                  select count(*)
                  from nascar_results
                  where race_date = %s
                  """
            self.cursor.execute(sql, (thebet,))
            cnt = self.cursor.fetchone()
            self.races_scored += 1
            # return cnt
        except Exception as echeck_if_race_is_already_loaded:
            self.connection.rollback()
            exit(echeck_if_race_is_already_loaded.__str__())

        return False if cnt[0] == 0 else True


if __name__ == "__main__":
    db = postgres_db.PostgreSQL()
    # load data from betData2026.py
    bets = BetData()
    # hydrate the CsvDB class with the bet data from betData2026
    loader = CsvDB(bets_2026=bets.get_bets)
    for bet in loader.get_bets:
        hydrated = loader.hydrate_track_table(loader.bets[bet]["Track"])
        if not loader.check_if_race_is_already_loaded(bet):
            try:
                print(loader.read_csv_race_results(bet))
            except Exception as e:
                exit(e.__str__())
    print(f"{loader.tracks_found} tracks found")
    print(f"{loader.races_scored} races scored")
    print(f"{loader.results_loaded} results loaded")
