import csv
from collections import defaultdict
from pathlib import Path

import psycopg

import db_connection as postgres_db

TARGET_RESULTS = (
    r"C:\Users\me\PycharmProjects\BeerMe3\data"
)


class CSV_DB:
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
        self.bets = defaultdict(dict)
        self.bets = self.get_bets()

    def read_csv_race_results(self, abet):
        results_file_name: str = f"{TARGET_RESULTS}\\{abet}.csv"
        with open(Path(f"{TARGET_RESULTS}\\{abet}.csv"), "r") as file:
            reader = csv.DictReader(file, delimiter="\t")
            for row in reader:
                bob_pick = False
                greg_pick = False
                if row["DRIVER"] == self.bets[abet]["Greg"]:
                    print(f"Greg Picked {self.bets[abet]["Track"]} {row['DRIVER']} {row['POS']}")
                    greg_pick = True
                if row["DRIVER"] == self.bets[abet]["Bob"]:
                    print(f"Bob Picked {self.bets[abet]["Track"]} {row['DRIVER']} {row['POS']}")
                    bob_pick = True
                # print(f"4. Processing {row} {self.bets[abet]['Greg']}")
                try:
                    self.cursor.execute("""
                                        insert into nascar_results
                                            (race_date, driver, pos, greg_pick, bob_pick, track)
                                        values (%s, %s, %s, %s, %s, %s)
                                        """,
                                        (
                                            abet,
                                            row['DRIVER'],
                                            row['POS'],
                                            greg_pick,
                                            bob_pick,
                                            self.bets[abet]["Track"]
                                        )
                                        )
                    self.connection.commit()
                except Exception as e:
                    return None

        return results_file_name

    def insert_results(self, abet):
        pass

    def get_bets(self):
        self.bets['02-15-2026'] = {
            "Greg": "William Byron",
            "Bob": "Ryan Blaney",
            "Track": "Daytona",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["02-22-2026"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Chase Elliott",
            "Track": "Atlanta",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["03-01-2026"] = {
            "Greg": "Shane van Gisbergen",
            "Bob": "Tyler Reddick",
            "Track": "COTA",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["03-08-2026"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Kyle Larson",
            "Track": "Phoenix",
            "badge_color": "bg-warning text-dark",
        }
        self.bets["03-15-2026"] = {
            "Greg": "Kyle Larson",
            "Bob": "Christopher Bell",
            "Track": "Las Vegas",
            "badge_color": "bg-warning text-dark",
        }

        return self.bets

    def check_if_already_loaded(self,bet):
        self.cursor.execute(f"select count(*) from nascar_results where race_date = '{bet}'")
        cnt = self.cursor.fetchone()
        return cnt[0] > 0


if __name__ == "__main__":
    db = postgres_db.PostgreSQL()
    loader = CSV_DB()

    for bet in loader.bets:
        if not loader.check_if_already_loaded(bet):
            try:
                print(loader.read_csv_race_results(bet))
            except Exception as e:
                print(e)
                continue
