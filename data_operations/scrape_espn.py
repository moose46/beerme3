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
from bs4 import BeautifulSoup

ESPN_RACING_RESULTS = "https://www.espn.com/racing/results/_/year/"


#  python scrape_espn.py
def bs(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code in [200]:
        soup_is_ready = BeautifulSoup(response.text,
                                      "html.parser")
        # print(response.status_code)
        return soup_is_ready
    elif response.status_code == 202:
        exit(f"No data found for {url}, response_code = {response.status_code}")
    else:
        print(f"Failed to retrieve data from {url}")
        return None


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
            {"race_date": race_date.strftime("%m/%d/%Y"), "race_track_name": race_track, "race_results": race_results,
             "race_name": race_name,
             "greg": {'driver': '', 'finish': 0}, "bob": {'driver': '', 'finish': 0}})
    return races

def get_race_results(url: str):
    hot_soup = bs(url)
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
                    print(data_cell.get_text(strip=True), end="\t")
                    # csv_file.write(data_cell.get_text(strip=True) + "\t")
                if cnt > 1:
                    print()
                    pass
                    # csv_file.write("\n")

            print()
    else:
        print(f"End of {url} results.")
    return None



if __name__ == "__main__":
    pass
