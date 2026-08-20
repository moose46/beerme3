import sqlite3
from sqlite3 import Error

from .track import Track

DB_FILENAME = "bets.db"
# import logging

# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='db_hydrate.log', level=logging.INFO, filemode='w')
# logger.info('Started')

try:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
except Error as e:
    print(f"Error: {DB_FILENAME} {e}")
    exit()


# def hydrate_race_results(races):
#     hot_soup = bs(the_url)
#     cnt = 0
#     if hot_soup:
#         csv_file = open(output_file_name, "w")
#         if table_rows := hot_soup.find_all("tr"):
#             for tr in table_rows:
#                 for data_cell in tr.find_all("td"):
#                     if cnt == 0:
#                         cnt = 1
#                         continue
#                         # print(child)
#                     cnt += 1
#                     # print(data_cell.get_text(strip=True), end="\t")
#                     csv_file.write(data_cell.get_text(strip=True) + "\t")
#                 if cnt > 1:
#                     csv_file.write("\n")
#     else:
#         print(f"End of {year} results.")
#     return race_dates


def hrydrate_race_result(data):
    insert_query = """"""
    pass


from .race import Race


def hydrate_races(races):
    race_list = []
    for race in races:
        # race_instance = Race()
        # race_instance.race_date = race.race_date
        # race_instance.race_name = race.race_name
        # race_instance.track_name = race.track_name
        race.db_insert_race()
        # race_list.append(race)
    #     data_tuple = (race["race_date"], race["race_results_url"], race["race_name"], track_id[0])
    #     try:
    #         cursor.execute(insert_query, data_tuple)
    #         conn.commit()
    #         pass
    #     except Error as e:
    #         # print(f"{data_tuple} {e}")
    #         logger.error(f"{data_tuple} {e}")
    #     cursor.execute(select_race_id_query, data_tuple)
    #     ret = cursor.fetchone()
    #     race_ids.append(ret[0])
    return races


def hydrate_driver(driver_name, driver_url):
    insert_query = """insert into drivers (driver_name, drivers_url)
                      VALUES (?, ?)"""
    select_query = """select driver_id
                      from drivers
                      where driver_name = ? """
    try:
        cursor.execute(insert_query, (driver_name, driver_url))
        conn.commit()
        cursor.execute(select_query, (driver_name,))
        driver_id = cursor.fetchone()

        # logger.info(f"{driver_name} {driver_id} driver created!")
        return driver_id[0]
    except Error as e:
        # logger.error(f"{driver_name} {driver_url} already exists!")
        pass

def hydrate_tracks(races):
    insert_query = """
                   INSERT into tracks (track_name)
                   VALUES (?) \
                   """
    fetch_query = """select * from tracks where track_name = ?"""
    pass
    for race in races:
        data_tuple = (race.race_track_name,)
        pass
        try:
            ret = cursor.execute(insert_query, data_tuple)
            conn.commit()
            print(f"{race.track_name} Created")
        except Error as e:
            # print(f"{hydrate_tracks} {data_tuple} {e}")
            # logger.error(f"{hydrate_tracks} {data_tuple} {e}")
            pass
        cursor.execute(fetch_query, data_tuple)
        track = cursor.fetchone()
        # race.track_name = track["track_name"]
        race.track.race_track_id = track[0]
        pass
    # hydrate_races_db(conn, cursor, race,track_id[0])
