import logging.config
import sqlite3
from dataclasses import dataclass
from typing import Optional

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


@dataclass
class Race:
    race_date: str
    race_results_url: str
    race_name: str
    race_name: str
    race_track_id: int
    race_track_name: str
    race_results_url: str
    race_id: Optional[int] = -1


class RaceDB:
    def __init__(self, db_path="bets.db") -> None:
        self._db_path = db_path

    def insert_race(self, race: Race):
        try:
            with sqlite3.connect(self._db_path) as connection:
                cursor = connection.cursor()
                cursor.execute('''INSERT INTO races (race_date, results_url, race_name, track_id, race_track_name)
                                  VALUES (?, ?, ?, ?, ?)''',
                               (race.race_date, race.race_results_url, race.race_name, race.race_track_id,
                                race.race_track_name))
                connection.commit()
                return self.get_race_id(race)
        except sqlite3.IntegrityError:
            return self.get_race_id(race)

    def get_race_id(self, race: Race) -> Optional[int]:
        try:
            with sqlite3.connect(self._db_path) as connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT track_id FROM tracks where track_name = ?", (race.race_track_name,))
                ret = cursor.fetchone()
                race.race_id = ret[0]
                return ret[0]
        except Exception as e:
            logger.info(f"Error Getting Track ID: {race.track_name} {e}")
