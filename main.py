from data_operations import bs
from settings import SOURCE_BEERME_BET_DATA2026, HEADERS
from datetime import datetime
import json
import sys
import collections

from settings import TRACK_HOST
ESPN_RACING_RESULTS = "https://www.espn.com/racing/results/_/year/"
collections.Callable = collections.abc.Callable

if __name__ == "__main__":
    year = datetime.now().year
    try:
        year = int(sys.argv[1])
    except IndexError as e:
        pass

    url = f"{ESPN_RACING_RESULTS}{year}"
    try:
        if soup := bs(url):
            pass
            # track_names = get_track_name(soup, year=year)

            # for track in track_names:
            #     print(track)

            # with open(f"json/{year}_races.json", "w") as file:
            #     json.dump(track_names, file, indent=4)
    except Exception as e:
        exit(e.__str__())
