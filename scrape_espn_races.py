# https://stackoverflow.com/questions/69515086/error-attributeerror
# -collections-has-no-attribute-callable-using-beautifu
import collections
import json
import sys
import datetime as datetime

collections.Callable = collections.abc.Callable
from settings import SOURCE_BEERME_BET_DATA2026, HEADERS
import requests
from bs4 import BeautifulSoup

ESPN_RACING_RESULTS = "https://www.espn.com/racing/results/_/year/"


#  python scrape_espn.py


def bs(url):
    response = requests.get(url, headers=HEADERS)
    print(f"{response}")
    if response.status_code in [200]:
        soup_is_ready = BeautifulSoup(response.content, "html.parser")
        # print(response.status_code)
        return soup_is_ready
    elif response.status_code == 202:
        exit(f"No data found for {url}, response_code = {response.status_code}")
    else:
        print(f"Failed to retrieve data from {url}")
        return None


def get_track_name(psoup):
    rows = psoup.find_all("tr")
    races = []
    skip = 1
    for row in rows:
        track_name = row.find_all("td")
        if skip <= 2:
            skip += 1
            continue
        race_date = datetime.datetime.strptime(track_name[0].text + " 2026", "%a, %b %d %Y").date()
        race_name = track_name[1].find_all("a")[0].text
        race_results = track_name[1].find_all("a")[0]["href"]
        race_name = race_name.replace("NASCAR Cup Series at ", "")
        # replace the year with the query year
        # race_date = race_date.replace(year=datetime.datetime.now().year)
        races.append(
            {"race_date": race_date.strftime("%m/%d/%Y"), "race_name": race_name, "race_results": race_results,
             "greg": {'driver': '', 'finish': 0}, "bob": {'driver': '', 'finish': 0}})
    return races


if __name__ == "__main__":
    race_dates = []
    try:
        year = int(sys.argv[1])
    except Exception as e:
        year = 2026  # exit(f"Enter a valid race year: Example: python scrape_espn.py 2025  # \n{e.__str__()}")

    for year in range(year, year + 1):
        print(f"Processing year: {year}")
        url = f"{ESPN_RACING_RESULTS}{year}"
        try:
            if soup := bs(url):
                track_names = get_track_name(soup)

                for track in track_names:
                    print(track)

                with open(f"{year}_races.json", "w") as file:
                    json.dump(track_names, file, indent=4)
        except Exception as e:
            exit(e.__str__())
