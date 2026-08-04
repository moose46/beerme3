import sqlite3
from sqlite3 import Error
import json
"""
run beerme.py first to create YYYY_races.json file
reads json\YYYY_races.json files for input
populates data/bets.db
"""

def hydrate_races_db(conn, cursor, race, track_id):
    insert_query = """
                   INSERT INTO races (race_date,race_results, track_id)  VALUES (?, ?,?)
                   """
    data_tuple = (race["race_date"],race["race_results"], track_id)
    try:
        cursor.execute(insert_query, data_tuple)
        conn.commit()
    except Error as e:
        print(e)


def hydrate_tracks_db(conn, cursor, data):
    insert_query = """
                   INSERT into tracks (track_name)
                   VALUES (?) \
                   """
    data_tuple = (data["race_track"],)
    try:
        ret = cursor.execute(insert_query, data_tuple)
        conn.commit()
    except Error as e:
        # print(e)
        pass
    select_query = """
    SELECT track_id from tracks where track_name = ?
    """
    track_name_tuple = (data["race_track"],)

    try:
        cursor.execute(select_query, track_name_tuple)
        track_id = cursor.fetchone()
    except Error as e:
        print(e)
    hydrate_races_db(conn, cursor, race,track_id[0])


def hydrate_race_results(conn, cursor, race):
    pass

def process_year_to_date_results(psoup):
    """
     Create mm-dd-yyyy.csv race results file
     returns a list of mm-dd-yyyy.csv filenames

    """
    race_dates = []
    # https://www.geeksforgeeks.org/python/extract-all-the-urls-from-the
    # -webpage-using-python/
    urls = []
    year = ""
    if psoup:
        urls.extend(
            link.get("href")
            for link in psoup.find_all("a")
            if link.get("href").__contains__("/racing/raceresults/_")
        )
        # get all table rows
        race_track = psoup.find_all("tr")
    for the_url in urls:
        # Filter out URLs that do not match the expected pattern
        # print(f"Processing URL: {the_url.split('/')[-1]}")
        url_id = the_url.split("/")[-1]
        year = url_id[:4]
        month = url_id[4:6]
        day = url_id[6:8]
        # print(f"year={year} month={month} day={day}")
        # output_file_name = f"{TARGET_RESULTS}/{month}-{day}-{year}.csv"
        # Create a list of race dates
        # race_dates.append(f"{month}-{day}-{year}.csv")

        # my_file = Path(output_file_name)
        # if my_file.is_file():
            # file exists
            # print(f"{my_file} exists {Path(output_file_name).stat(
            # ).st_size} bytes")
            # if my_file.stat().st_size > 5:
                # print(f"{my_file} > 5")
                # continue
        hot_soup = bs(the_url)
        cnt = 0
        if hot_soup:
            # csv_file = open(output_file_name, "w")
            if table_rows := hot_soup.find_all("tr"):
                for tr in table_rows:
                    for data_cell in tr.find_all("td"):
                        if cnt == 0:
                            cnt = 1
                            continue
                            # print(child)
                        cnt += 1
                        # print(data_cell.get_text(strip=True), end="\t")
                        # csv_file.write(data_cell.get_text(strip=True) + "\t")
                    # if cnt > 1:
                        # csv_file.write("\n")
    else:
        print(f"End of {year} results.")
    return race_dates

if __name__ == "__main__":
    conn = sqlite3.connect('bets.db')
    cursor = conn.cursor()
    with open('./json/2026_races.json') as f:
        data = json.load(f)
        for race in data:
            print(race["race_track"])
            hydrate_tracks_db(conn, cursor, race)
            hydrate_race_results(conn, cursor, race)
    cursor.close()
    conn.close()
