import os

insert_query = f"""INSERT INTO tracks (track_name) VALUES (?)"""
from logging import debug, Formatter, StreamHandler, getLogger, ERROR, error, DEBUG, FileHandler, INFO
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
        logging.config.fileConfig('logging.conf')
        logger = getLogger("track")
        logger.info(f"Track Class Initialized")
        try:
            self._connection = sqlite3.connect(DB_FILENAME)
            self._cursor = self._connection.cursor()
            logging.debug(f"Connected to Database")
        except Error as e:
            logging.debug(f"Error: {DB_FILENAME} {e}")
            exit(str(e))

    def db_get_race_track_id(self):
        data_tuple = (self._track_name,)
        logging.debug(f"data_tuple: {data_tuple}")
        self._cursor.execute(fetch_query, data_tuple)
        ret = self._cursor.fetchone()
        # logging.debug(f"race_track_id: {ret}")
        self._race_track_id = ret[1]
        logging.debug(f"race_track_id: {self._race_track_id}")
        return self._race_track_id

    def db_insert_track(self, track_name: str = None):

        if track_name is None:
            data_tuple = (self._track_name,)
        else:
            data_tuple = (track_name,)
        logging.debug(f"data_tuple: {data_tuple}")
        if self.db_get_race_track_id() is None:
            # logging.debug(f"{data_tuple} {data_tuple}")
            self._cursor.execute(insert_query, (self._track_name,))
            self._connection.commit()
            self._cursor.execute(fetch_query, data_tuple)
            ret = self._cursor.fetchone()
            logging.debug(f"{self._track_name} Created")
            self._race_track_id = ret[1]
        return self._race_track_id

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
    track.track_name= "Pocono Raceway"
    track.db_get_race_track_id()
