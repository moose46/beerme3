# https://stackoverflow.com/questions/69515086/error-attributeerror
# -collections-has-no-attribute-callable-using-beautifu

"""
this will create ../json/YYYY_bets.json file for the year provided on the command line
or default to the current year
after running this program, then run load_tracks_db.py
"""

import collections
import datetime as datetime
import json
import logging
import re
import sys

from data_operations.race import Race
# from .db_hydrate import hydrate_driver

collections.Callable = collections.abc.Callable
from settings import HEADERS
import requests
from bs4 import BeautifulSoup

ESPN_RACING_RESULTS = "https://www.espn.com/racing/results/_/year/"
POS = 0
DRIVER = 1
CAR = 2
MANUFACTURER = 3
LAPS = 4
START = 5
LED = 6
PTS = 7
BONUS = 8
PENALITY = 9


#  python scrape_espn.py
def bs(url):
    response = requests.get(url, headers=HEADERS)
    print(f"{response}")
    if response.status_code in [200]:
        soup_is_ready = BeautifulSoup(response.content, "html.parser")
        # print(response.status_code)
        return soup_is_ready
    elif response.status_code == 202:
        exit(f"No races found for {url}, response_code = {response.status_code}")
    else:
        print(f"Failed to retrieve races from {url}")
        return None


def get_race_results(url):
    hot_soup = bs(url)
    cnt = 0
    if hot_soup:
        row = 0
        # csv_file = open(output_file_name, "w")
        if table_rows := hot_soup.find_all("tr"):
            for tr in table_rows:
                row += 1
                if row < 3:
                    continue
                try:
                    # tr.find_all('td')
                    # position =  tr.find_all('a')[POS].get_text()
                    # tr.find_all('td')[1].find('a').get('href')
                    # todo: add hydrate_driver()
                    # hydrate_driver(tr.find_all('td')[DRIVER].get_text(),
                    #                tr.find_all('td')[DRIVER].find('a').get('href'))

                    # print(
                    #     f"{tr.find_all('td')[POS].get_text()} {tr.find_all('td')[DRIVER].get_text()} "
                    #     f"{tr.find_all('td')[CAR].get_text()} {tr.find_all('td')[MANUFACTURER].get_text()} "
                    #     f"{tr.find_all('td')[LAPS].get_text()} {tr.find_all('td')[START].get_text()} "
                    #     f"{tr.find_all('td')[LED].get_text()} {tr.find_all('td')[PTS].get_text()} "
                    #     f"{tr.find_all('td')[BONUS].get_text()} {tr.find_all('td')[PENALITY].get_text()}", end="")
                    # if row > 2:
                    #     print(f"{tr.find_all('td')[DRIVER].find('a').get('href')}")
                    # elif row == 2:
                    #     print(f" URL")
                    # else:
                    #     print()

                except Exception as e:
                    logging.debug(f"Failed to retrieve {tr[POS]} {e.__repr__()}")
                    exit(e.__str__())
                # for data_cell in tr.find_all("td"):
                #     if cnt == 0:
                #         cnt = 1
                #         continue
                #         # print(child)
                #     cnt += 1
                #     print(data_cell.get_text(strip=True), end="\t")
                #     # csv_file.write(data_cell.get_text(strip=True) + "\t")
                # if cnt > 1:
                #     pass
                #     print()
                #     # csv_file.write("\n")
    else:
        print(f"End of {url} results.")
    return


def get_race_data_espn(url, year):
    """

    :param url: 'https://www.espn.com/racing/results/_/year//2026'
    :param year:
    :return: a dict list of race_dates, race_track_name, race_results_url, with the bet races
    """
    psoup = bs(url)
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
        # race_track = re.sub(f"{race_name}", "", race_track)
        # race_results = track_name[1].find_all("a")[0]["href"]
        race = Race()
        race.race_date = race_date.strftime("%m/%d/%Y")
        race.race_track_name = re.sub(f"{race_name}", "", race_track)
        race.results_url = track_name[1].find_all("a")[0]["href"]
        race.race_name = race_name
        races.append(race)
    return races


def hydrate_race_json():
    race_dates = []
    try:
        year = int(sys.argv[1])
    except Exception as e:
        year = datetime.datetime.now().year
        # year = 2025  # exit(f"Enter a valid race year: Example: python scrape_espn.py 2025  # \n{e.__str__()}")

    for year in range(year, year + 1):
        print(f"Processing year: {year}")
        url = f"{ESPN_RACING_RESULTS}{year}"
        try:
            if soup := bs(url):
                track_names = get_track_name(soup, year=year)

                for track in track_names:
                    print(track)

                with open(f"../json/{year}_races.json", "w") as file:
                    json.dump(track_names, file, indent=4)
        except Exception as e:
            exit(e.__str__())


if __name__ == "__main__":
    hydrate_race_json()
