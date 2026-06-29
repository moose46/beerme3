# https://stackoverflow.com/questions/69515086/error-attributeerror
# -collections-has-no-attribute-callable-using-beautifu
import collections
import json
import shutil
import sys
from pathlib import Path

collections.Callable = collections.abc.Callable
from settings import TARGET_RESULTS, TARGET_RESULTS_BEER_ME, HEADERS, TRACK_HOST
import requests
from bs4 import BeautifulSoup


#  python scrape_espn.py


def bs(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code in [200]:
        soup_is_ready = BeautifulSoup(response.text, "html.parser")
        # print(response.status_code)
        return soup_is_ready
    elif response.status_code == 202:
        exit(f"No data found for {url}, response_code = {response.status_code}")
    else:
        print(f"Failed to retrieve data from {url}")
        return None


def get_track_name(psoup):
    rows = psoup.find_all("tbody")
    tracks = []
    for row in rows:
        track_data = row.find_all("td", {"data-column": "track"})
        race_dates = row.find_all("td", {"data-column": "date"})
        race_television = row.find_all("td", {"data-column": "television"})
        race_winner = row.find_all("td", {"data-column": "winner"})
        win_make = row.find_all("td", {"data-column": "win_make"})
        for index in range(len(race_dates)):
            tracks.append({
                "track": track_data[index].get_text(strip=True),
                "date": race_dates[index].get(
                "data-sort")[5:7] + "-" + race_dates[index].get("data-sort")[8:10] + "-" + race_dates[index].get(
                "data-sort")[0:4],
                "time": race_dates[index].get("data-sort")[11:19],
                "television"  : race_television[index].get_text(),
                "win_make"  : win_make[index].get_text(),
                "race_winner"  : race_winner[index].get_text()})
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
        output_file_name = f"{TARGET_RESULTS}/{month}-{day}-{year}.csv"
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
                        # print(data_cell.get_text(strip=True), end="\t")
                        csv_file.write(data_cell.get_text(strip=True) + "\t")
                    if cnt > 1:
                        csv_file.write("\n")
    else:
        print(f"End of {year} results.")
    return race_dates


def copy_race_dates(prace_dates: list):
    return
    for race in prace_dates:
        # print(f"{TARGET_RESULTS_BEER_ME}\\{race}")
        my_file = Path(f"{TARGET_RESULTS_BEER_ME}\\{race}")
        if not my_file.is_file():
            print(f"-- Copying {Path(my_file)} to \n "
                  f"{TARGET_RESULTS_BEER_ME}\\{race}")
            shutil.copy2(f"{TARGET_RESULTS}\\{race}", f"{TARGET_RESULTS_BEER_ME}")  # copy2 preserves  # metadata


if __name__ == "__main__":
    race_dates = []
    try:
        year = int(sys.argv[1])
    except Exception as e:
        year = 2024  # exit(f"Enter a vaild race year: Example: python scrape_espn.py 2025  # \n{e.__str__()}")

    for year in range(year, year + 1):
        print(f"Processing year: {year}")
        url = f"{TRACK_HOST}{year}"
        try:
            if soup := bs(url):
                track_names = get_track_name(soup)
                for track_name in track_names:
                    print(track_name)
                with open(f"{TARGET_RESULTS}\\{year}_races.json", "w") as file:
                    json.dump(track_names, file, indent=4)
        except Exception as e:
            exit(e.__str__())
        try:
            if soup := bs(url):
                race_dates = process_year_to_date_results(soup)
            else:
                print(f"No data found for year {year}")
        except Exception as e:
            exit(e.__str__())
    # copy race dates to visual studio beerme2
    # copy_race_dates(race_dates)
