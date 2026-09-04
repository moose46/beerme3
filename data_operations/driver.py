import logging.config
import sqlite3
from dataclasses import dataclass
from typing import Optional

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


@dataclass
class Driver:
    driver_name: str
    age: int
    home_town: str
    driver_id: int
    espn_driver_url: str
    nascar_driver_url: str
    driver_id: Optional[int] = -1

class DriverDB:
    def __init__(self, db_path="bets.db"):
        self.db_path = db_path
        def insert_driver(self, driver: Driver):
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
            except sqlite3.IntegrityError:
                pass
