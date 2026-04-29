"""
python load_csv_db.py
hydrates the nascar_results from data/mm-dd-yyyy.csv files
bets[mm-dd-yyyy] must have the current race and bet data first
run scrape_espn.py before running this file

"""
import csv
from collections import defaultdict
from pathlib import Path

import psycopg

import db_connection as postgres_db

TARGET_RESULTS = (
    r"C:\Users\me\PycharmProjects\BeerMe3\data"
)


class CsvDB:
    def __init__(self):
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
        self.bets = self.get_bets()
        self.track_id = 0  # current track_id
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
                except Exception as e1:
                    exit(e1.__str__())


        return results_file_name

    def get_track_id(self, track_name):
        sql = "select id from track where track_name = %s"
        self.cursor.execute(sql, (track_name,))
        return self.cursor.fetchone()[0]

    def get_bets(self):
        self.bets['02-15-2026'] = {
            "Greg"       : "William Byron",
            "Bob"        : "Ryan Blaney",
            "Track"      : "Daytona",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["02-22-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Chase Elliott",
            "Track"      : "Atlanta",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["03-01-2026"] = {
            "Greg"       : "Shane van Gisbergen",
            "Bob"        : "Tyler Reddick",
            "Track"      : "COTA",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["03-08-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Kyle Larson",
            "Track"      : "Phoenix",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["03-15-2026"] = {
            "Greg"       : "Kyle Larson",
            "Bob"        : "Christopher Bell",
            "Track"      : "Las Vegas",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["03-22-2026"] = {
            "Greg"       : "Denny Hamlin",
            "Bob"        : "Tyler Reddick",
            "Track"      : "Darlington",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["03-29-2026"] = {
            "Greg"       : "William Byron",
            "Bob"        : "Denny Hamlin",
            "Track"      : "Martinsville",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["04-12-2026"] = {
            "Greg"       : "Kyle Larson",
            "Bob"        : "Ty Gibbs",
            "Track"      : "Bristol",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["04-19-2026"] = {
            "Greg"       : "Kyle Larson",
            "Bob"        : "Tyler Reddick",
            "Track"      : "Kansas",
            "badge_color": "bg-warning text-dark",
        }

        self.bets["04-26-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Tyler Reddick",
            "Track"      : "Talladega",
            "badge_color": "bg-warning text-dark",
        }

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
        except Exception as e:
            self.connection.rollback()
            exit(e.__str__())

        return True

    def check_if_already_loaded(self, thebet):
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
        except Exception as e:
            self.connection.rollback()
            exit(e.__str__())
        # print(cnt[1])
        return False if cnt[0] == 0 else True


if __name__ == "__main__":
    db = postgres_db.PostgreSQL()
    loader = CsvDB()

    for bet in loader.bets:
        hydrated = loader.hydrate_track_table(loader.bets[bet]["Track"])
        if not loader.check_if_already_loaded(bet):
            try:
                print(loader.read_csv_race_results(bet))
            except Exception as e:
                exit(e.__str__())
