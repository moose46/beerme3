# from bs4 import BeautifulSoup
# from settings import SOURCE_BEERME_BET_DATA2026, HEADERS
from datetime import datetime
import json
import sys
import collections
# import requests
from settings import TRACK_HOST
ESPN_RACING_RESULTS = "https://www.espn.com/racing/results/_/year/"
collections.Callable = collections.abc.Callable
import data_operations.beerme as beerme
import data_operations.db_hydrate as db_hyd
if __name__ == "__main__":
    year = datetime.now().year
    try:
        year = int(sys.argv[1])
    except IndexError as e:
        pass

    url = f"{ESPN_RACING_RESULTS}/{year}"
    print(url)
    try:
        # create json/YYYY_races.json
        track_names = beerme.get_track_names( url, year)
        db_hyd.hydrate_tracks(track_names)
        db_hyd.hydrate_races(track_names)
        for track_name in track_names:
            race_results = beerme.get_race_results(track_name["race_results_url"])
        # for track in track_names:
        #     print(track)
        with open(f"json/{year}_races.json", "w") as file:
            json.dump(track_names, file, indent=4)
    except Exception as e:
        exit(e.__str__())