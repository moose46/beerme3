class Track(object):
    def __init__(self):
        self._race_track_id = None
        self._track_name = None
        self._track_type = None
        self._cursor = None

    def db_insert_track(self):
        if self._race_track_id is None:
            pass

    def db_select_track(self, track_name: str = None):
        if track_name is None:
            return f"Track Name Can Not Be None!"
        select_query = f"""select * from tracks where track_name = ?"""
        pass

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
