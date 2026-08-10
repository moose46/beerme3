import sqlite3

from data_operations.bet import Bet
from data_operations.track import Track
import data_operations.scrape_espn as espn
# from data_operations.db_hydrate import cursor

insert_query = """
               INSERT or REPLACE INTO races (race_date, results_url, race_name, track_id)
               VALUES (?, ?, ?, ?)
               """
select_track_query = """
                     SELECT track_id
                     from tracks
                     where track_name = ? \
                     """
select_race_id_query = """select race_id
                          from races
                          where race_date = ?
                            and results_url = ?
                            and race_name = ?
                            and track_id = ?"""


class Race:
    def __init__(self):
        self._race_name = None
        self._race_date = None
        self._race_results_url = None
        # self._race_track_name = None
        # self._track_id = None
        self._race_id = None
        self._race_track_name = None
        self.track_name_tuple = (self._race_track_name,)
        self.greg = Bet()
        self.bob = Bet()
        self._track = Track()
        self._connection = None
        self.track.connection = self._connection
        self._cursor = None
        self.track.cursor = self._cursor

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, connection: sqlite3.Connection):
        self._connection = connection
        self.track.connection = self._connection

    @property
    def track(self):
        return self._track

    @track.setter
    def track(self, track: Track):
        self._track = track

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, cursor: sqlite3.Cursor):
        self._cursor = cursor
        self.track.cursor = cursor

    @property
    def race_track_name(self):
        return self.track.track_name

    @race_track_name.setter
    def race_track_name(self, race_track_name: str):
        self.track.track_name = race_track_name

    @property
    def results_url(self):
        return self._race_results_url

    @results_url.setter
    def results_url(self, race_results_url: str):
        self._race_results_url = race_results_url

    @property
    def race_name(self):
        return self._race_name

    @race_name.setter
    def race_name(self, race_name: str):
        self._race_name = race_name

    @property
    def race_date(self):
        return self._race_date

    @race_date.setter
    def race_date(self, race_date: str):
        self._race_date = race_date

    def db_insert_race(self):
        # look up track id, track must be already in the database
        data_tuple = (self._race_date, self._race_results_url, self._race_name, self.track.race_track_id)
        self._cursor.execute(insert_query, data_tuple)
        self._connection.commit()

    def db_get_race(self, race_name: str, race_date: str, cursor: sqlite3.Cursor):
        query = """select *
                   from races
                   where race_date = ?
                     and race_name = ?"""
        cursor.execute(query, (self.race_name, self.race_date))
        race = self.cursor.fetchone()
        return race
    def db_insert_race_results(self):
        espn.get_race_results(self._race_results_url)

    def __repr__(self):
        return f"{self.race_date} {self.race_name} {self.track_id} {self.race_id}"

    def __str__(self):
        return f""""""
