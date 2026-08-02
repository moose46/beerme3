# https://stackoverflow.com/questions/69515086/error-attributeerror
# -collections-has-no-attribute-callable-using-beautifu

"""
this will create ../json/YYYY_bets.json file for the year provided on the command line
or default to the current year
after running this program, then run load_tracks_db.py
"""

import collections
import json
import sys
import datetime as datetime
import re
# from bs4 import BeautifulSoup as bs
collections.Callable = collections.abc.Callable
from settings import SOURCE_BEERME_BET_DATA2026, HEADERS
import requests
from bs4 import BeautifulSoup as bs

ESPN_RACING_RESULTS = "https://www.espn.com/racing/results/_/year/"


#  python scrape_espn.py


def get_track_names(psoup, year):
    """
    returns a list of track names
    :param psoup:
    :param year:
    :return:
    """
    rows = psoup.find_all("tr")
    races = []
    skip = 1
    for row in rows:
        track_name = row.find_all("td")
        if skip <= 2:
            skip += 1
            continue
        race_date = datetime.datetime.strptime(track_name[0].text + f" {year}", "%a, %b %d %Y").date()

        race_name = track_name[1].find_all("a")[0].text
        # get the race track name
        race_track = track_name[1].text
        # remove the race name, and only the track name is left
        race_track = re.sub(f"{race_name}", "", race_track)
        race_results = track_name[1].find_all("a")[0]["href"]
        races.append(
            {"race_date": race_date.strftime("%m/%d/%Y"), "race_track": race_track, "race_results": race_results,
             "race_name": race_name,
             "greg": {'driver': '', 'finish': 0}, "bob": {'driver': '', 'finish': 0}})
    return races



if __name__ == "__main__":
    pass
