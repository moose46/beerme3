import shutil
from pathlib import Path
import sqlite3
# https://stackoverflow.com/questions/69515086/error-attributeerror-collections-has-no-attribute-callable-using-beautifu
import collections
collections.Callable = collections.abc.Callable

import requests
from bs4 import BeautifulSoup
from html_table_parser.parser import HTMLTableParser

#  python scrape_espn.py


TARGET_RESULTS = (
    r"C:\Users\me\PycharmProjects\BeerMe3\data"
)
TARGET_RESULTS_BEER_ME = (
    r"C:\Users\me\Documents\VisualCodeSource\beerme2\data"
)
HOST = "https://www.espn.com/racing/raceresults/_/series/sprint/raceId/202404280004"
HOST = "https://www.espn.com/racing/results/_/year/"
# HOST = "https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI"
PORT = 80
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def bs(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup_is_ready = BeautifulSoup(response.text,
                             "html.parser")
        # print(response.status_code)
        return soup_is_ready
    else:
        print(f"Failed to retrieve data from {url}")
        return None


def process_results(psoup):
    race_dates = []
    # https://www.geeksforgeeks.org/python/extract-all-the-urls-from-the-webpage-using-python/
    urls = []
    year = ""
    if psoup:
        urls.extend(
            link.get("href")
            for link in psoup.find_all("a")
            if link.get("href").__contains__("/racing/raceresults/")
        )
    for the_url in urls:
        # Filter out URLs that do not match the expected pattern
        # print(f"Processing URL: {the_url.split('/')[-1]}")
        url_id = the_url.split("/")[-1]
        year = url_id[:4]
        month = url_id[4:6]
        day = url_id[6:8]
        # print(f"year={year} month={month} day={day}")
        output_file_name = f"{TARGET_RESULTS}/{month}-{day}-{year}.csv"
        # Create a list of race dates
        race_dates.append(f"{month}-{day}-{year}.csv")

        my_file = Path(output_file_name)
        if my_file.is_file():
            # file exists
            # print(f"{my_file} exists {Path(output_file_name).stat().st_size} bytes")
            if my_file.stat().st_size > 5:
                # print(f"{my_file} > 5")
                continue
        hot_soup = bs(the_url)
        cnt = 0
        if hot_soup:
            f = open(output_file_name, "w")
            if table_rows := hot_soup.find_all("tr"):
                for tr in table_rows:
                    for data_cell in tr.find_all("td"):
                        if cnt == 0:
                            cnt = 1
                            continue
                            # print(child)
                        cnt += 1
                        # print(data_cell.get_text(strip=True), end="\t")
                        f.write(data_cell.get_text(strip=True) + "\t")
                    if cnt > 1:
                        f.write("\n")
    else:
        print(f"End of {year} results.")
    return race_dates
def copy_race_dates(prace_dates: list):
    for race in prace_dates:
        # print(f"{TARGET_RESULTS_BEER_ME}\\{race}")
        my_file = Path(f"{TARGET_RESULTS_BEER_ME}\\{race}")
        if not my_file.is_file():
           print(f"-- Copying {Path(my_file)} to \n {TARGET_RESULTS_BEER_ME}\\{race}")
           shutil.copy2(f"{TARGET_RESULTS}\\{race}", f"{TARGET_RESULTS_BEER_ME}")  # copy2 preserves metadata


if __name__ == "__main__":
    race_dates = []
    for year in range(2026, 2027):
        print(f"Processing year: {year}")
        url = f"{HOST}{year}"
        try:
            if soup := bs(url):
                race_dates = process_results(soup)
            else:
                print(f"No data found for year {year}")
        except Exception as e:
            print(f"Exception: {e}")
    copy_race_dates(race_dates)