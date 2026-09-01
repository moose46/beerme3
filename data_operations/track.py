import os

insert_query = f"""INSERT INTO tracks (track_name) VALUES (?)"""
from logging import getLogger
import logging.config

fetch_query = """select count(*), track_id
                 from tracks
                 where track_name = ?"""
insert_query = """
               INSERT into tracks (track_name)
               VALUES (?) \
               """
import sqlite3
from sqlite3 import Error

DB_FILENAME = os.getcwd() + "//bets.db"


class Track(object):
    def __init__(self):
        self._race_track_id = None
        self._track_name = None
        self._track_type = None
        self._cursor = None
        self._connection = None
        # logging.config.fileConfig('logging.conf')
        self._logger = getLogger(__name__)
        # logger.info(f"Track Class Initialized")
        try:
            self._connection = sqlite3.connect(DB_FILENAME)
            self._cursor = self._connection.cursor()
            # self._logger.debug(f"Connected to Database {DB_FILENAME}")
        except Error as e:
            logging.exception(f"Error: {DB_FILENAME}")

    def db_get_race_track_id(self):
        data_tuple = (self._track_name,)
        # self._logger.debug(f"data_tuple: {data_tuple}")
        self._cursor.execute(fetch_query, data_tuple)
        ret = self._cursor.fetchone()
        # logging.debug(f"race_track_id: {ret}")
        self._race_track_id = ret[1]
        self._logger.info(f"{self._track_name}: {self._race_track_id} {self._track_type}")
        return self._race_track_id

    def db_insert_track(self, track_name: str = None):

        try:
            data_tuple = (track_name,)
            self._track_name = track_name
            # logging.info(f"data_tuple: {data_tuple}")
            if self.db_get_race_track_id() is None:
                # logging.debug(f"{data_tuple} {data_tuple}")
                self._cursor.execute(insert_query, (track_name,))
                self._connection.commit()
                self._cursor.execute(fetch_query, data_tuple)
                ret = self._cursor.fetchone()
                self._logger.info(f"Track Created {track_name}")
                self._race_track_id = ret[1]
                self._track_name = track_name
            return self._race_track_id
        except Error as e:
            logging.exception(f"Track Insert Error: {DB_FILENAME}")
            return None

    def db_select_track(self, track_name: str = None):
        if track_name is None:
            return f"Track Name Can Not Be None!"
        select_query = f"""select * from tracks where track_name = ?"""
        pass

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, value):
        self._connection = value

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        self._cursor = value

    @property
    def race_track_id(self):
        return self._race_track_id

    @property
    def track_name(self):
        return self._track_name

    @property
    def track_type(self):
        return self._track_type

    @race_track_id.setter
    def race_track_id(self, value):
        self._race_track_id = value

    @track_name.setter
    def track_name(self, value):
        self._track_name = value

    @track_type.setter
    def track_type(self, value):
        self._track_type = value


if __name__ == "__main__":
    track = Track()
    track.track_name = "Pocono Raceway"
    track.db_get_race_track_id()
