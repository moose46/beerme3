insert_query = f"""INSERT INTO tracks (track_name) VALUES (?)"""
import logging

fetch_query = """select count(*), track_id
                 from tracks
                 where track_name = ?"""
insert_query = """
               INSERT into tracks (track_name)
               VALUES (?) \
               """


class Track(object):
    def __init__(self):
        self._race_track_id = None
        self._track_name = None
        self._track_type = None
        self._cursor = None
        self._connection = None
        track_logger = logging.getLogger("track")
        track_logger.setLevel(logging.DEBUG)
        logging.basicConfig(filename='track.log', level=logging.DEBUG, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        pass

    def db_get_race_track_id(self):
        data_tuple = (self._track_name,)
        logging.info(f"data_tuple: {data_tuple}")
        self._cursor.execute(fetch_query, data_tuple)
        ret = self._cursor.fetchone()
        self._race_track_id = ret[1]
        return self._race_track_id

    def db_insert_track(self):

        data_tuple = (self._track_name,)
        logging.info(f"data_tuple: {data_tuple}")
        if self.db_get_race_track_id() is None:
            # logger.error(f"{data_tuple} {e}")
            self._cursor.execute(insert_query, (self._track_name,))
            self._connection.commit()
            self._cursor.execute(fetch_query, data_tuple)
            ret = self._cursor.fetchone()
            print(f"{self._track_name} Created")
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
