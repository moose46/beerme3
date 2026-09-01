# https://stackoverflow.com/questions/69515086/error-attributeerror
# -collections-has-no-attribute-callable-using-beautifu

"""
Create YYYY_bets.json file for the year provided

"""

import collections
import datetime as datetime
import re
import sys

from data_operations.race import Race
from data_operations.track import Track
import json
import logging
import logging.config

# error_handler = logging.FileHandler("scrape_espn_races.log")
# error_handler.setLevel(logging.DEBUG)
collections.Callable = collections.abc.Callable
from settings import HEADERS
import requests
from bs4 import BeautifulSoup

ESPN_RACING_RESULTS = "https://www.espn.com/racing/results/_/year/"


#  python scrape_espn.py

logger = logging.getLogger(__name__)
def bs(url):
    response = requests.get(url, headers=HEADERS)
    # print(f"{response}")
    if response.status_code in [200]:
        soup_is_ready = BeautifulSoup(response.content, "html.parser")
        logger.info(f"Response Code: {response.status_code}")
        return soup_is_ready
    elif response.status_code == 202:
        logger.info(f"{url} Response Code: {response.status_code}")
        exit(f"No data found for {url}, response_code = {response.status_code}")
    else:
        logging.exception(f"Failed to retrieve data from {url}")
        return None


def get_track_name(psoup, year):
    """

    :param psoup:
    :param year:
    :return: dictionary containing: race_name, race_date, race_track,race_results url
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
        race_track1 = re.sub(f"{race_name}", "", race_track)
        race_track = re.match(f'(\/>).(?=<)',  str(track_name[1]))
        race_track1 = re.sub(f"{race_name}", "", race_track1)
        race_results_url = track_name[1].find_all("a")[0]["href"]
        races.append(
            {"race_date": race_date.strftime("%m/%d/%Y"), "race_track_name": race_track, "race_results_url": race_results_url,
             "race_name": race_name, })
    return races

def run():
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("scrape_espn_races")
    race_dates = []
    try:
        year = int(sys.argv[1])
    except Exception as e:
        year = 2025  # exit(f"Enter a valid race year: Example: python scrape_espn.py 2025  # \n{e.__str__()}")

    for year in range(year, year + 1):
        logger.info(f"Processing year: {year}")
        # url is an espn nascar list of all races completed for that year
        url = f"{ESPN_RACING_RESULTS}{year}"
        try:
            if soup := bs(url):
                track_names = get_track_name(soup, year=year)

                for track in track_names:
                    assert isinstance(track, object)
                    the_track = Track()
                    the_track.track_name = track["race_track_name"]
                    the_track.db_insert_track(the_track.track_name)
                    logger.info(f"{track["race_date"]:16} {track["race_track_name"]}")
                    race = Race()
                    race.race_name = track["race_name"]
                    race.race_date = track["race_date"]
                    race.race_results_url = track["race_results_url"]
                    race.track.race_track_id = the_track.race_track_id
                    race.race_track_name = track["race_track_name"]
                    # race.db_insert_race()
                # creates a YYYY_races.json file
                logger.info(f"Saving {year}_races.json")
                with open(f"{year}_races.json", "w") as file:
                    json.dump(track_names, file, indent=4)
        except Exception as e:
            logging.exception(f"Failed to process year: {year} {e}")
            exit(e.__str__())

if __name__ == "__main__":
    run()
