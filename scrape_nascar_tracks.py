# https://stackoverflow.com/questions/69515086/error-attributeerror
# -collections-has-no-attribute-callable-using-beautifu
import collections
import json
import os
import sys
from pathlib import Path

collections.Callable = collections.abc.Callable
from settings import SOURCE_BEERME_BET_DATA2026, HEADERS, FRCS_TRACK_HOST
import requests
from bs4 import BeautifulSoup
from logging import debug, Formatter, StreamHandler, getLogger, ERROR, error, DEBUG, FileHandler, INFO
import logging.config
from data_operations.track import Track

#  python scrape_espn.py
import re

logging.config.fileConfig('logging.conf')
logger = getLogger("track")
logger.debug(f"Track Initialized")


def remove_ellipsis(text: str) -> str:
    """
    Remove both ASCII '...' and Unicode ellipsis '…' from the given string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Regex pattern matches either three or more dots, or the Unicode ellipsis
    cleaned_text = re.sub(r"\.{3,}|…", "", text)
    cleaned_text1 = re.sub(u'\u2026', u'', cleaned_text)
    return cleaned_text1.strip()


def bs(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code in [200]:
        soup_is_ready = BeautifulSoup(response.text, "html.parser")
        # print(response.status_code)
        logging.info(f"Soup is ready: {response.status_code}")
        return soup_is_ready
    elif response.status_code == 202:
        exit(f"No races found for {url}, response_code = {response.status_code}")
    else:
        print(f"Failed to retrieve races from {url}")
        return None


def get_track_name(psoup):
    track_rows = psoup.find_all("td", {"data-column": "track"})
    date_rows = psoup.find_all("td", {"data-column": "date"}, "data-sort")
    race_rows = psoup.find_all("td", {"data-column": "race"},)
    tracks = []
    track_rows.__len__()
    for index, row in enumerate(track_rows):
        track_name = row.text
        track_url = row.find("a").get("href")
        race_date = date_rows[index]['data-sort'] # get the 12/20/2026 format from the date
        race_name = race_rows[index].text
        # race_dates = rows[1].find("td", {"data-column": "date"}).text
        # race_television = rows[1].find("td", {"data-column": "television"}).text
        # race_winner = rows[1].find("td", {"data-column": "winner"}).text
        # win_make = rows[1].find("td", {"data-column": "win_make"}).text
        # race_name = rows[1].find("td", {"data-column": "race"}).text
        tracks.append({"track":track_name, "race_date":race_date, "race_name":race_name,"track_url":track_url})
        # for index in range(len(race_dates)):
        #     a_track_dict = dict(track=track_name[index].get_text(strip=True), date=race_dates[index].get(
        #         "races-sort")[5:7] + "-" + race_dates[index].get("races-sort")[8:10] + "-" + race_dates[index].get(
        #         "races-sort")[0:4], time=race_dates[index].get("races-sort")[11:19],
        #                         television=race_television[index].get_text(), win_make=win_make[index].get_text(),
        #                         race_winner=race_winner[index].get_text(), race_name=race_name[index].get_text())
        #     a_track_dict["track"] = remove_ellipsis(a_track_dict["track"])
        # a_track_dict["race_name"] = remove_ellipsis(a_track_dict["race_name"])
        # tracks.append(a_track_dict)
            # tracks.append(race_dates[index].get_text(strip=True))  # x = data_cell  #
            # tracks.append( {"track": data_cell.get_text()})  # for race_date in race_dates:  #     tracks.add(
            # race_date.get_text())
    return tracks


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
            link.get("href") for link in psoup.find_all("a") if link.get("href").__contains__("/racing/raceresults/_"))
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
        output_file_name = f"{SOURCE_BEERME_BET_DATA2026}/{month}-{day}-{year}.csv"
        # Create a list of race dates
        race_dates.append(f"{month}-{day}-{year}.csv")

        my_file = Path(output_file_name)
        if my_file.is_file():
            # file exists
            # print(f"{my_file} exists {Path(output_file_name).stat(
            # ).st_size} bytes")
            if my_file.stat().st_size > 5:
                # print(f"{my_file} > 5")
                continue
        hot_soup = bs(the_url)
        cnt = 0
        if hot_soup:
            csv_file = open(output_file_name, "w")
            if table_rows := hot_soup.find_all("tr"):
                for tr in table_rows:
                    for data_cell in tr.find_all("td"):
                        if cnt == 0:
                            cnt = 1
                            continue  # print(child)
                        cnt += 1
                        # print(data_cell.get_text(strip=True), end="\t")'
                        tmp = remove_ellipsis(data_cell.get_text(strip=True))
                        csv_file.write(remove_ellipsis(data_cell.get_text(strip=True)) + "\t")
                    if cnt > 1:
                        csv_file.write("\n")
    else:
        print(f"End of {year} results.")
    return race_dates


if __name__ == "__main__":
    race_dates = []
    try:
        year = int(sys.argv[1])
    except Exception as e:
        year = 2026  # exit(f"Enter a valid race year: Example: python scrape_espn.py 2025  # \n{e.__str__()}")

    for year in range(year, year + 1):
        logging.info(f"Processing year: {year}")
        url = f"{FRCS_TRACK_HOST}{year}"
        logging.info(f"Getting tracks from {url}")
        try:
            if soup := bs(url):
                track_names = get_track_name(soup)

                for track_data in track_names:
                    print(track_data)
                    track = Track()
                    track.track_name = track_data['track']
                    track.db_insert_track()

                with open(f"{os.getcwd()}\\{year}_races.json", "w") as file:
                    json.dump(track_names, file, indent=4)
        except Exception as e:
            logging.info(e.__str__())
            exit(e)
        try:
            if soup := bs(url):
                race_dates = process_year_to_date_results(soup)
            else:
                logging.info(f"No races found for year {year}")
        except Exception as e:
            exit(e.__str__())
    # copy race dates to visual studio beerme2
    # copy_race_dates(race_dates)
