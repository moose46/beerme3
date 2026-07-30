import sqlite3
from sqlite3 import Error
import json
def hydrate_tracks_db(conn,cursor, data):
    insert_query = """
        INSERT into tracks (track_name)
        VALUES (?)
    """
    data_tuple = (data["race_track"],)
    try:
        cursor.execute(insert_query, data_tuple)
        conn.commit()
    except Error as e:
        print(e)

if __name__ == "__main__":
    conn = sqlite3.connect('./data/bets.db')
    cursor = conn.cursor()
    with open('./json/2026_races.json') as f:
        data = json.load(f)
        for race in data:
            print(race["race_track"])
            hydrate_tracks_db(conn, cursor, race)
    cursor.close()
    conn.close()
