# https://stackoverflow.com/questions/69515086/error-attributeerror
# -collections-has-no-attribute-callable-using-beautifu

"""
Create YYYY_bets.json file for the year provided

"""

import collections
import datetime as datetime
import logging
import logging.config
import re
import sys
from dataclasses import dataclass, asdict
from typing import Any

import json
from data_operations.race import Race, RaceDB
from data_operations.track import TrackDB

# from data_operations.track import Track

# error_handler = logging.FileHandler("scrape_espn_races.log")
# error_handler.setLevel(logging.DEBUG)
collections.Callable = collections.abc.Callable
from settings import HEADERS
import requests
from bs4 import BeautifulSoup
from data_operations.track import Track

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


@dataclass
class TrackData:
    race_track_name: str
    race_date: str
    race_results_url: str
    race_name: str


def get_race_details(psoup, year):
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
        # get the race track name
        pattern = r"(?<=br\/>).*(?=<)"
        match = re.search(pattern, str(track_name[1]))
        # end of get race track name
        trackData = TrackData(race_name=track_name[1].find_all("a")[0].text,
                              race_track_name=match.group(),
                              race_date=race_date.strftime("%m/%d/%Y"),
                              race_results_url=track_name[1].find_all("a")[0]["href"], )
        logger.info(f"{asdict(trackData)}")
        races.append(asdict(trackData))
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
        if soup := bs(url):
            race_details = get_race_details(soup, year=year)

        for race in race_details:
            assert isinstance(race, object)
            # the_track.track_name = race["race_track_name"]
            the_track = Track(track_name=race["race_track_name"], )
            track_db = TrackDB()
            track_id = track_db.insert_track(the_track)
            # track_id = track_db.get_track_id(the_track)
            logger.info(f"{race["race_date"]:16} {race["race_track_name"]}")
            race = Race(race_name=race["race_name"], race_track_id=track_id, race_date=race["race_date"],
                        race_track_name=race["race_track_name"], race_results_url=race["race_results_url"])
            race_db = RaceDB()
            race_db.insert_race(race)
            # creates a YYYY_races.json file

        for race in race_details:
            if soup := bs(race["race_results_url"]):
                race_results = get_race_results(soup)

        logger.info(f"Saving {year}_races.json")
        with open(f"{year}_races.json", "w") as file:
            json.dump(race_details, file, indent=4)


def get_race_results(soup: BeautifulSoup) -> Any:
    rows = soup.find_all("tr")
    skip = 1
    for row in rows:
        table_data = row.find_all("td")
        if skip <= 2:
            skip += 1
            continue
        position = table_data[0].text
        driver = table_data[1].text
        car = table_data[2].text
        manufacturer = table_data[3].text
        laps = table_data[4].text
        start = table_data[5].text
        led = table_data[6].text
        pts = table_data[7].text
        bonus = table_data[8].text
        penality = table_data[9].text
        driver_url = "http://www.espn.com/racing/" +  table_data[1].find("a")["href"]
        pass


if __name__ == "__main__":
    run()
