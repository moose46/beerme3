# from bs4 import BeautifulSoup
# from settings import SOURCE_BEERME_BET_DATA2026, HEADERS
import collections
# import requests
import sqlite3
import sys
from datetime import datetime
from sqlite3 import Error

from db_hydrate_tracks import cursor

DB_FILENAME = "bets.db"
import logging

ESPN_RACING_RESULTS = "https://www.espn.com/racing/results/_/year/"
collections.Callable = collections.abc.Callable
import data_operations.beerme as beerme

try:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
except Error as e:
    print(f"Error: {DB_FILENAME} {e}")
    exit()

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='beerme.log', level=logging.INFO, filemode='w')
    logger.info('Started')
    year = datetime.now().year
    try:
        year = int(sys.argv[1])
    except IndexError as e:
        pass

    url = f"{ESPN_RACING_RESULTS}/{year}"
    logger.info(f"Getting tracks from {url}")
    # try:
    # create a list of races for the year
    list_of_races = beerme.get_race_data_espn(url, year)
    for race in list_of_races:
        race.cursor = cursor
        race.connection = conn
        # race.track.db_get_race_track_id()
        race.track.db_insert_track()
        race.db_insert_race()
        race_results_dict = race.db_insert_race_results()
