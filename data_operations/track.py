import logging.config
import sqlite3
from dataclasses import dataclass
from typing import Optional

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


@dataclass
class Track:
    track_name: str
    track_id: Optional[int] = -1


class TrackDB:
    def __init__(self, db_path="bets.db") -> None:
        self._db_path = db_path

    def insert_track(self, track: Track) -> Optional[int]:
        try:
            with sqlite3.connect(self._db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f"INSERT INTO tracks (track_name) VALUES (?)", (track.track_name,))
                conn.commit()
                return self.get_track_id(track)
        except sqlite3.IntegrityError as e:
            return self.get_track_id(track)

    def get_track_id(self, track: Track) -> Optional[int]:
        try:
            with sqlite3.connect(self._db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT track_id FROM tracks where track_name = ?", (track.track_name,))
                ret = cursor.fetchone()
                return ret[0]
        except Exception as e:
            logger.info(f"Error Getting Track ID: {track.track_name} {e}")
