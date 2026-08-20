# from bs4 import BeautifulSoup
# from settings import SOURCE_BEERME_BET_DATA2026, HEADERS
import collections
import logging
# import requests
import sqlite3
import sys
from datetime import datetime
from sqlite3 import Error

from data_operations.copy_csv_files import copy_race_results_csv

# from db_hydrate_tracks import cursor

DB_FILENAME = "bets.db"
from logging import debug, Formatter, StreamHandler, getLogger, ERROR, error, DEBUG, FileHandler, INFO

ESPN_RACING_RESULTS = "https://www.espn.com/racing/results/_/year"
collections.Callable = collections.abc.Callable
import data_operations.beerme as beerme

try:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
except Error as e:
    print(f"Error: {DB_FILENAME} {e}")
    exit()
# logger = logging.getLogger(__name__)
    # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
if __name__ == "__main__":
    try:
        # log_file = "main.log"
        logger = getLogger(__name__)
        # logger.basicConfig(level=logging.DEBUG)
        fh = FileHandler('beerme.log',mode='w', encoding='utf-8', delay=False)
        fh.setLevel(logging.INFO)
        # fh.setLevel(DEBUG)
        # fh.setLevel(NOSET)
        # fh.setLevel(logging.ERROR)
        ch = StreamHandler()
        # ch.setLevel(ERROR)
        formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        # logger.error(f"Logging to {log_file}")
        # logger.setLevel(logging.DEBUG)
        # handler = logging.StreamHandler(sys.stdout)
        # logging.basicConfig(level=logging.DEBUG)
        # logging.root.setLevel(logging.NOTSET)
        # os.makedirs(os.path.dirname(log_file), exist_ok=True) if os.path.dirname(log_file) else None
        # logging.basicConfig(filename=log_file, level=logging.DEBUG, filemode='w',
        #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                            # handlers=[
                            #     # logging.StreamHandler,
                            #           logging.FileHandler(log_file, mode='w', encoding='utf-8')])
        # logging.error('Started')
        # logging.critical('Critical')
    except PermissionError as e:
        error(f"Error: __main__ {e}")
        exit()
    try:
        year = int(sys.argv[1])
    except IndexError as e:
        year = datetime.now().year
        # logger.error(f"Error: __main__ {e}")

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


    url = f"{ESPN_RACING_RESULTS}/{year}"
    # logger.info(f"Getting tracks from {url}")
    # logger.error(f"Getting tracks from {url}")
    # try:
    # create a list of races for the year
    list_of_races = beerme.get_race_data_espn(url, year)
    for race in list_of_races:
        race.cursor = cursor
        race.connection = conn
        # race.track.db_get_race_track_id()
        race.track.db_insert_track()
        race.db_insert_race()
        race.db_insert_race_results()
        race.csv_create_file()
        copy_race_results_csv([race.race_csv_filename])
        # print(race)
        exit()
