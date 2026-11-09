import csv
import sqlite3
from collections import defaultdict, namedtuple

from prompt_toolkit.utils import to_int


class Entry:
    def __init__(
            self, player_name, badge_color, finish=0, driver_name="", beers=0, car_number=99
    ):
        self.player_name = player_name
        self.driver_name = driver_name
        self.finish = finish
        self.beers = beers
        self.car_number = car_number
        self.badge_color = badge_color

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return (f"Entry:{self.player_name:4s} {self.race_name} {self.driver_name} {self.finish} {self.beer} "
                f"{self.badge_color}")


class BeerBet(Entry):
    bob: Entry
    greg: Entry

    def __init__(self, bob, greg, race_name, badge_color):
        self.race_name = race_name
        self.bob = bob
        self.greg = greg
        self.race_name = race_name
        self.badge_color = badge_color

    def the_winner(self):
        # if self.greg.finish > self.bob.finish:
        self.bob.beer = self.bob.beers  # type: ignore
        # elif self.greg.finish < self.bob.finish:
        self.greg.beer = self.greg.beers  # type: ignore

        return {
            "Bob"        : self.bob.beers,
            "Greg"       : self.greg.beers,
            "badge_color": self.badge_color,
        }

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return (
            f"Race: {self.race_name}:\n"
            f"\tName: Driver:{self.bob.driver_name} Finish:{self.bob.finish} Beers:{self.bob.beers} color:"
            f"{self.badge_color}\n"
            f"\tName: Driver:{self.greg.driver_name} Finish:{self.greg.finish} Beers:{self.greg.beers} color:"
            f"{self.badge_color}"
        )


class BetData2026:
    def __getitem__(self, race_date):  # '02-15-2026'
        return self.individual_bets[race_date]

    def __init__(self) -> None:
        self.individual_bets = defaultdict()
        # self.individual_bets.setdefault("missing_key")
        self.individual_bets["02-15-2026"] = {
            "Greg"       : "William Byron",
            "Bob"        : "Ryan Blaney",
            "Track"      : "Daytona",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["02-22-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Chase Elliott",
            "Track"      : "Atlanta",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-01-2026"] = {
            "Greg"       : "Shane van Gisbergen",
            "Bob"        : "Tyler Reddick",
            "Track"      : "COTA",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-08-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Kyle Larson",
            "Track"      : "Phoenix",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-15-2026"] = {
            "Greg"       : "Kyle Larson",
            "Bob"        : "Christopher Bell",
            "Track"      : "Las Vegas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-22-2026"] = {
            "Greg"       : "Denny Hamlin",
            "Bob"        : "Tyler Reddick",
            "Track"      : "Darlington",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-29-2026"] = {
            "Greg"       : "William Byron",
            "Bob"        : "Denny Hamlin",
            "Track"      : "Martinsville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-12-2026"] = {
            "Greg"       : "Kyle Larson",
            "Bob"        : "Ty Gibbs",
            "Track"      : "Bristol",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-19-2026"] = {
            "Greg"       : "Kyle Larson",
            "Bob"        : "Tyler Reddick",
            "Track"      : "Kansas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-26-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Tyler Reddick",
            "Track"      : "Talladega",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-03-2026"] = {
            "Greg"       : "Denny Hamlin",
            "Bob"        : "Carson Hocevar",
            "Track"      : "Texas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-10-2026"] = {
            "Greg"       : "Shane van Gisbergen",
            "Bob"        : "Ty Gibbs",
            "Track"      : "Watkins Gleen",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-24-2026"] = {
            "Greg"       : "Denny Hamlin",
            "Bob"        : "Ross Chastain",
            "Track"      : "Charlotte",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-31-2026"] = {
            "Greg"       : "Tyler Reddick",
            "Bob"        : "Denny Hamlin",
            "Track"      : "Nashville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-07-2026"] = {
            "Greg"       : "Kyle Larson",
            "Bob"        : "Tyler Reddick",
            "Track"      : "Michigan",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-14-2026"] = {
            "Greg"       : "Denny Hamlin",
            "Bob"        : "Chase Briscoe",
            "Track"      : "Pocono",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-21-2026"] = {
            "Greg"       : "Connor Zilisch",
            "Bob"        : "Shane van Gisbergen",
            "Track"      : "Coronado",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-28-2026"] = {
            "Greg"       : "Shane van Gisbergen",
            "Bob"        : "Kyle Larson",
            "Track"      : "Sonoma Raceway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-05-2026"] = {
            "Greg"       : "Kyle Larson",
            "Bob"        : "Denny Hamlin",
            "Track"      : "Chicagoland Speedway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-12-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Chase Elliott",
            "Track"      : "EchoPark Speedway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-19-2026"] = {
            "Greg"       : "William Byron",
            "Bob"        : "Christopher Bell",
            "Track"      : "North Wilkesboro",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-26-2026"] = {
            "Greg"       : "Denny Hamlin",
            "Bob"        : "Carson Hocevar",
            "Track"      : "Indy",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["08-09-2026"] = {
            "Greg"       : "Denny Hamlin",
            "Bob"        : "Ryan Blaney",
            "Track"      : "Iowa Speedway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["08-15-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Denny Hamlin",
            "Track"      : "Richmond Raceway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["08-23-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Denny Hamlin",
            "Track"      : "New Hampshire Raceway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["08-29-2026"] = {
            "Greg"       : "William Byron",
            "Bob"        : "Kyle Larson",
            "Track"      : "Daytona",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["09-06-2026"] = {
            "Greg"       : "Tyler Reddick",
            "Bob"        : "Denny Hamlin",
            "Track"      : "Darlington",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["09-13-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Joey Logano",
            "Track"      : "St. Louis",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["09-19-2026"] = {
            "Greg"       : "Denny Hamlin",
            "Bob"        : "Kyle Larson",
            "Track"      : "Bristol Baby",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["09-27-2026"] = {
            "Greg"       : "Kyle Larson",
            "Bob"        : "Christopher Bell",
            "Track"      : "Kansas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["10-04-2026"] = {
            "Greg"       : "Christopher Bell",
            "Bob"        : "Denny Hamlin",
            "Track"      : "Las Vegas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["10-11-2026"] = {
            "Greg"       : "Kyle Larson",
            "Bob"        : "Chase Briscoe",
            "Track"      : "Charlotte",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["10-18-2026"] = {
            "Greg"       : "Christopher Bell",
            "Bob"        : "Ryan Blaney",
            "Track"      : "Phoenix",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["10-25-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Chase Briscoe",
            "Track"      : "Talladega",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["11-01-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Denny Hamlin",
            "Track"      : "Martinsville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["11-08-2026"] = {
            "Greg"       : "Denny Hamlin",
            "Bob"        : "Chase Briscoe",
            "Track"      : "Miami",
            "badge_color": "bg-warning text-dark",
        }

        # # start of can't pick a driver twice

    @property
    def get_bets(self):
        """_summary_

        Returns:
            Returns a list of dictionaries of all the current bet in date_information for Greg and Bob
            first pick starts at the first of the year and alternates each week
        """
        # for first_pick, x in enumerate(self.individual_bets):
        #     self.individual_bets[x]["first_pick"] = "Greg" if first_pick % 2 else "Bob"
        return self.individual_bets

    def get_results(self):
        """_summary_"""

    def create_db_from_csv_files(self, db):
        cursor = db.cursor()
        for race_date in self.individual_bets:
            results_file_name = f"{race_date}.csv"
            track = self.individual_bets[race_date]['Track']
            with open(results_file_name) as csvfile:
                reader = csv.reader(csvfile, delimiter="\t")
                try:
                    rawResult = namedtuple("rawResult", next(reader), rename=True)
                except Exception as e:
                    print(f'{namedtuple} {e}')
                    exit()
                for row in reader:
                    result = rawResult(*row)
                    # load race_date and track into the race_scheudle table
                    race_id = self.load_race_schedule(track, race_date)
                    # print(f'{result.DRIVER}')
                    cursor.execute(
                        f"insert into race_results(track,race_date,driver, finish, car_number, race_id) values('"
                        f"{track}',"
                        f"'{race_date}',"
                        f"'{result.DRIVER}',{result.POS}, {result.CAR}, {race_id})")
                    db.commit()

    def load_bet_data(self, bets):
        bob_total = 0
        greg_total = 0
        for race_date in bets:
            track = self.individual_bets[race_date]['Track']
            # race_date = self.individual_bets[race_date]
            gregs_pick = self.individual_bets[race_date]['Greg']
            bobs_pick = self.individual_bets[race_date]['Bob']
            cursor.execute(f"update race_results set player_name=?  where race_date = ? and driver = ?",
                           ("Bob", race_date, bobs_pick))
            cursor.execute(f"update race_results set player_name=?  where race_date = ? and driver = ?",
                           ("Greg", race_date, gregs_pick))
            db.commit()
            # get drivers finish position for bobs pick
            cursor.execute(
                f"select finish from race_results where track='{track}' and race_date='{race_date}' and driver='"
                f"{bobs_pick}'")
            bob_finish = to_int(cursor.fetchone()[0])
            cursor.execute(
                f"select finish from race_results where track='{track}' and race_date='{race_date}' and driver='"
                f"{gregs_pick}'")
            greg_finish = to_int(cursor.fetchone()[0])
            bob_awarded = 0
            greg_awarded = 0
            if greg_finish < bob_finish:
                greg_total += 1
                greg_awarded = 1
                if greg_finish == 1:
                    greg_total += 1
                    greg_awarded = 2
            elif bob_finish < greg_finish:
                bob_total += 1
                bob_awarded = 1
                if bob_finish == 1:
                    bob_total += 1
                    bob_awarded = 2
            cursor.execute(
                "update race_results set player_beers_total=?, points_awarded=? where track=? and race_date=? and player_name=?",
                (bob_total,bob_awarded, track, race_date, 'Bob'))
            cursor.execute(
                "update race_results set player_beers_total=?, points_awarded=? where track=? and race_date=? and player_name=?",
                (greg_total,greg_awarded, track, race_date, 'Greg'))
            db.commit()
            print(f"bob={bob_total}, greg={greg_total}, track={track}")
        # cursor.execute("select * from scoring_results")

    def load_race_schedule(self, track, race_date):
        try:
            cursor.execute("insert into race_schedule (track, race_date) values(?,?)", (track, race_date))
            # db.commit()
        except sqlite3.IntegrityError:
            pass
        cursor.execute("select id from race_schedule where track=? and race_date=?", (track, race_date))
        return cursor.fetchone()[0]

    def create_score_board(self):
        pass


import os

if __name__ == "__main__":
    """_summary_
    Returns: List of races
    """

    bets = BetData2026()
    # db = sqlite3.connect(":memory:")
    try:
        os.remove("beerme.db")
    except FileNotFoundError:
        pass
    db = sqlite3.connect("beerme.db")
    cursor = db.cursor()
    race_schedule = """
                    create table if not exists race_schedule
                    (
                        id        integer primary key autoincrement,
                        track     varchar(50) not null,
                        race_date text        not null,
                        unique (race_date, track)
                    )
                    """
    cursor.execute(race_schedule)
    csv_table = """create table if not exists race_results
                   (
                       id                 integer primary key autoincrement,
                       race_id            integer     not null,
                       track              varchar(50) not null,
                       race_date          text        not null,
                       driver             varchar(50) not null,
                       car_number         int         not null default 0,
                       finish             int         not null,
                       player_name        varchar(50),
                       player_beers_total int         not null default 0,
                       points_awarded int         not null default 0
                   )"""
    cursor.execute(csv_table)
    scoring_results = """create table if not exists scoring_results
                         (
                             race_name        varchar(50) not null,
                             greg_driver_name varchar(50) not null,
                             greg_beer        int         not null default 0,
                             bob_driver_name  varchar(50) not null,
                             bob_beer         int         not null default 0
                         )"""
    cursor.execute(scoring_results)
    # weekly_bets = """create table if not exists weekly_bets
    #                  (
    #                      track       varchar(50) not null,
    #                      race_date   varchar(12) not null,
    #                      bob_driver  varchar(50) not null,
    #                      greg_driver varchar(50) not null
    #                  )"""
    # cursor.execute(weekly_bets)
    # web_data = """create table if not exists web_data
    #               (
    #                   race_date       varchar(16) not null,
    #                   race_track      varchar(32) not null,
    #                   player_name     varchar(16) not null,
    #                   driver_name     varchar(16) not null,
    #                   car_number      int default 0,
    #                   finish_position int default 0,
    #                   beers_won       int default 0
    #               )"""
    # cursor.execute(web_data)
    # results = bets.get_bets
    bets.create_db_from_csv_files(db)
    bets.load_bet_data(bets.individual_bets)
    bets.create_score_board()
    # cursor.execute("select * from race_results")
    # for row in cursor.fetchall():
    #     print(row)
    # cursor.execute("select * from scoring_results;")
    # for row in cursor.fetchall():
    #     print(row)
    # for result in results:
    #     print(f"{results[result]}")
