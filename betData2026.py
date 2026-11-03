import csv
import sqlite3
from collections import defaultdict, namedtuple

from prompt_toolkit.utils import to_int


class BetData2026_1:
    def __init__(self):
        self.individual_bets = defaultdict(dict)
        self.individual_bets["02-15-2026"] = {
            "Greg"       : {"Driver": "William Byron", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Ryan Blaney", "Finish": 0, "beers": 0},
            "Track"      : "Daytona",
            "badge_color": "bg-warning text-dark",
        }

        self.individual_bets["02-22-2026"] = {
            "Greg"       : {"Driver": "Ryan Blaney", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Chase Elliott", "Finish": 0, "beers": 0},
            "Track"      : "Atlanta",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-01-2026"] = {
            "Greg"       : {"Driver": "Shane van Gisbergen", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Tyler Reddick", "Finish": 0, "beers": 0},
            "Track"      : "COTA",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-08-2026"] = {
            "Greg"       : {"Driver": "Ryan Blaney", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Track"      : "Phoenix",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-15-2026"] = {
            "Greg"       : {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Christopher Bell", "Finish": 0, "beers": 0},
            "Track"      : "Phoenix",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-22-2026"] = {
            "Greg"       : {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Tyler Reddick", "Finish": 0, "beers": 0},
            "Track"      : "Darlington",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-29-2026"] = {
            "Greg"       : {"Driver": "William Byron", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Track"      : "Martinsville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-12-2026"] = {
            "Greg"       : {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Ty Gibbs", "Finish": 0, "beers": 0},
            "Track"      : "Bristol",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-19-2026"] = {
            "Greg"       : {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Tyler Reddick", "Finish": 0, "beers": 0},
            "Track"      : "Kansas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-26-2026"] = {
            "Greg"       : {"Driver": "Ryan Blaney", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Tyler Reddick", "Finish": 0, "beers": 0},
            "Track"      : "Talladega",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-03-2026"] = {
            "Greg"       : {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Carson Hocevar", "Finish": 0, "beers": 0},
            "Track"      : "Texas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-10-2026"] = {
            "Greg"       : {"Driver": "Shane van Gisbergen", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Ty Gibbs", "Finish": 0, "beers": 0},
            "Track"      : "Watkins Glen",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-24-2026"] = {
            "Greg"       : {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Ross Chastain", "Finish": 0, "beers": 0},
            "Track"      : "Charlotte",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-31-2026"] = {
            "Greg"       : {"Driver": "Tyler Reddick", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Track"      : "Nashville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-07-2026"] = {
            "Greg"       : {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Tyler Reddick", "Finish": 0, "beers": 0},
            "Track"      : "Michigan",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-14-2026"] = {
            "Greg"       : {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Chase Briscoe", "Finish": 0, "beers": 0},
            "Track"      : "Pocono",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-21-2026"] = {
            "Greg"       : {"Driver": "Connor Zilisch", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Shane van Gisbergen", "Finish": 0, "beers": 0},
            "Track"      : "Coronado",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-28-2026"] = {
            "Greg"       : {"Driver": "Shane van Gisbergen", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Track"      : "Sonoma Raceway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-05-2026"] = {
            "Greg"       : {"Driver": "Kyle Larson", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Track"      : "Chicagoland Speedway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-12-2026"] = {
            "Greg"       : {"Driver": "Ryan Blaney", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Chase Elliott", "Finish": 0, "beers": 0},
            "Track"      : "EchoPark Speedway",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-26-2026"] = {
            "Greg"       : {"Driver": "Denny Hamlin", "Finish": 0, "beers": 0},
            "Bob"        : {"Driver": "Carson Hosevar", "Finish": 0, "beers": 0},
            "Track"      : "Indy",
            "badge_color": "bg-warning text-dark",
        }

    def __getitem__(self, race_date):  # '02-15-2026'
        return self.individual_bets[race_date]


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
            "Greg": "Ryan Blaney",
            "Bob": "Chase Briscoe",
            "Track": "Talladega",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["11-01-2026"] = {
            "Greg"       : "Ryan Blaney",
            "Bob"        : "Denny Hamlin",
            "Track"      : "Martinsville",
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
        for race in self.individual_bets:
            results_file_name = f"{race}.csv"
            track = self.individual_bets[race]['Track']
            with open(results_file_name) as csvfile:
                reader = csv.reader(csvfile, delimiter="\t")
                try:
                    rawResult = namedtuple("rawResult", next(reader), rename=True)
                except Exception as e:
                    print(f'{namedtuple} {e}')
                    exit()
                for row in reader:
                    result = rawResult(*row)
                    # print(f'{result.DRIVER}')
                    cursor.execute(
                        f"insert into race_results(track,race_date,driver, finish) values('{track}','{race}',"
                        f"'{result.DRIVER}',{result.POS})")

    def load_bet_data(self, bets):
        bob_total = 0
        greg_total = 0
        for bet in bets:
            track = self.individual_bets[bet]['Track']
            race_date = self.individual_bets[bet]
            greg = self.individual_bets[bet]['Greg']
            bob = self.individual_bets[bet]['Bob']
            cursor.execute(
                f"insert into scoring_results(track,race_date,bob_driver_name,greg_driver_name) values("
                f"'{track}','{bet}','{bob}','{greg}')")
            cursor.execute(f"select finish from race_results where track='{track}' and race_date='{bet}' and driver='{bob}'")
            bob = to_int(cursor.fetchone()[0])
            cursor.execute(f"select finish from race_results where track='{track}' and race_date='{bet}' and driver='{greg}'")
            greg = to_int(cursor.fetchone()[0])
            if greg < bob:
                greg_total += 1
                if greg == 1:
                    greg_total += 1
            else:
                bob_total += 1
                if bob == 1:
                    bob_total += 1
            print(f"bob={bob_total}, greg={greg_total}, track={track}")
        # cursor.execute("select * from scoring_results")


if __name__ == "__main__":
    """_summary_
    Returns: List of races
    """

    bets = BetData2026()
    db = sqlite3.connect(":memory:")
    cursor = db.cursor()
    csv_table = """create table race_results
                   (
                       track     varchar(50) not null,
                       race_date varchar(12) not null,
                       driver    varchar(50) not null,
                       finish    int         not null
                   )"""
    cursor.execute(csv_table)
    scoring_results = """create table scoring_results
                       (
                           track              varchar(50) not null,
                           race_date          varchar(12) not null,
                           bob_driver_name    varchar(50) not null,
                           greg_driver_name   varchar(50) not null,
                           bob_driver_finish  int         not null default 0,
                           greg_driver_finish int         not null default 0,
                           bob_points         int         not null default 0,
                           greg_points        int         not null default 0
                       )"""
    cursor.execute(scoring_results)
    weekly_bets = """create table weekly_bets
                     (
                         track       varchar(50) not null,
                         race_date   varchar(12) not null,
                         bob_driver  varchar(50) not null,
                         greg_driver varchar(50) not null
                     )"""
    cursor.execute(weekly_bets)
    # results = bets.get_bets
    bets.create_db_from_csv_files(db)
    bets.load_bet_data(bets.individual_bets)
    # cursor.execute("select * from race_results")
    # for row in cursor.fetchall():
    #     print(row)
        # cursor.execute("select * from scoring_results;")
        # for row in cursor.fetchall():
        #     print(row)
    # for result in results:
    #     print(f"{results[result]}")
