"""
python load_csv_db.py
hydrates the nascar_results from races/mm-dd-yyyy.csv files
bets[mm-dd-yyyy] must have the current race and bet races first
run scrape_espn.py before running this file

"""
import csv
import json
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any

import psycopg

import db_connection as postgres_db
from settings import PYCHARM_DATA, TARGET_BEERME_BET_DATA2026, \
    SOURCE_BEERME_BET_DATA2026, VISUAL_CODE_SOURCE_RESULTS, PYCHARM_JSON_DATA_FILE


# C:\Users\me\PycharmProjects\BeerMe3\races\2026_bets.json
def read_bets_JSON_DATA_FILE():
    try:
        with open(f'{PYCHARM_JSON_DATA_FILE}', "r") as file:
            return json.load(file)
    except FileNotFoundError:
        exit(f"File {VISUAL_CODE_SOURCE_RESULTS}\\2026_bets.json does not exist")


class CsvDB:
    def __init__(self, bets):
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
        self.bets = bets
        self.track_id = 0  # current track_id
        self.tracks_found = 0
        self.results_loaded = 0
        self.races_scored = 0

    def read_csv_race_results(self, abet):
        # abet is one bet from a list of bets
        results_file_name: str = f"{PYCHARM_DATA}\\{abet}.csv"
        track_id = self.get_track_id(track_name=self.bets[abet]["Track"])
        with open(Path(f"{VISUAL_CODE_SOURCE_RESULTS}\\{abet}.csv"), "r") as file:
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
        sql = "select id from tracks where track_name = %s"
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
                  insert into tracks (track_name, id)
                  select %s, nextval('seq_track_id')
                  where not exists  (select track_name
                                     from tracks
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


def copy_race_bets():
    my_file = Path(f"{SOURCE_BEERME_BET_DATA2026}")
    if my_file.is_file():
        try:
            print(
                f"-- Copying {Path(my_file)} to "
                f"{TARGET_BEERME_BET_DATA2026}"
            )
            shutil.copy2(f"{SOURCE_BEERME_BET_DATA2026}",
                         f"{TARGET_BEERME_BET_DATA2026}")  # copy2 preserves
            print(
                f"\n-- Copying {Path(PYCHARM_JSON_DATA_FILE)} to  "
                f"{VISUAL_CODE_SOURCE_RESULTS}"
            )

            shutil.copy2(f"{PYCHARM_JSON_DATA_FILE}",
                         f"{VISUAL_CODE_SOURCE_RESULTS}\\")  # copy2 preserves
        except Exception as e2:
            exit(e2.__str__())


def convert_json_file():
    new_bet = {}
    try:
        with open(f'{PYCHARM_JSON_DATA_FILE}', "r") as file:
            data = json.load(file)
            bet_json_list = []
            for bet in data:
                # print(bet)
                new_bet['race_date'] = bet['race_date']
                new_bet['drivers'] = {}
                new_bet['drivers']['Greg'] = bet['Greg']
                new_bet['drivers']['Bob'] = bet['Bob']
                new_bet['track'] = bet['Track']
                # print(new_bet)
                bet_json_list.append(new_bet)
        with open(f'test.json', "w") as file:
            x = json.dump(bet_json_list, file, indent=4)
        # print(x)
    except Exception as e:
        exit(e.__str__())


if __name__ == "__main__":
    db = postgres_db.PostgreSQL()
    # hydrate the CsvDB class with the bet races from bets
    bets = read_bets_JSON_DATA_FILE()
    loader = CsvDB(bets=bets)
    for bet in bets:
        hydrated = loader.hydrate_track_table(bet["track"])
        if not loader.check_if_race_is_already_loaded(bet["race_date"]):
            try:
                print(loader.read_csv_race_results(bet))
            except Exception as e:
                print(e.__str__())
                continue
    print(f"{loader.tracks_found} tracks found")
    print(f"{loader.races_scored} races scored")
    print(f"{loader.results_loaded} results loaded")
    copy_race_bets()
    # convert_json_file()
