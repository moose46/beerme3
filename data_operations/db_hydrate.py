import logging
import sqlite3
from sqlite3 import Error
import json
DB_FILENAME = "bets.db"
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='db_hydrate.log', level=logging.INFO, filemode='w')
logger.info('Started')

try:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
except Error as e:
    print(f"Error: {DB_FILENAME} {e}")
    exit()

def hydrate_race_results(data):
    hot_soup = bs(the_url)
    cnt = 0
    if hot_soup:
        csv_file = open(output_file_name, "w")
        if table_rows := hot_soup.find_all("tr"):
            for tr in table_rows:
                for data_cell in tr.find_all("td"):
                    if cnt == 0:
                        cnt = 1
                        continue
                        # print(child)
                    cnt += 1
                    # print(data_cell.get_text(strip=True), end="\t")
                    csv_file.write(data_cell.get_text(strip=True) + "\t")
                if cnt > 1:
                    csv_file.write("\n")
    else:
        print(f"End of {year} results.")
    return race_dates


def hydrate_races(races):
    insert_query = """
                   INSERT INTO races (race_date,results_url,race_name, track_id)  VALUES (?, ?,?,?)
                   """
    select_query = """
    SELECT track_id from tracks where track_name = ?
    """
    for race in races:
        track_name_tuple = (race["race_track"],)

        try:
            cursor.execute(select_query, track_name_tuple)
            track_id = cursor.fetchone()
        except Error as e:
            print(e)
        data_tuple = (race["race_date"],race["race_results"],race["race_name"], track_id[0])
        try:
            cursor.execute(insert_query, data_tuple)
            conn.commit()
        except Error as e:
            # print(f"{data_tuple} {e}")
            logger.error(f"{data_tuple} {e}")

def hydrate_tracks(data):
    insert_query = """
                   INSERT into tracks (track_name)
                   VALUES (?) \
                   """
    for track in data:
        data_tuple = (track["race_track"],)
        try:
            ret = cursor.execute(insert_query, data_tuple)
            conn.commit()
            print(f"{track['race_track']} Created")
        except Error as e:
            # print(f"{hydrate_tracks} {data_tuple} {e}")
            logger.error(f"{hydrate_tracks} {data_tuple} {e}")
            # pass
    # hydrate_races_db(conn, cursor, race,track_id[0])
