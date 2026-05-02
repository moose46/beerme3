# https://stackoverflow.com/questions/69515086/error-attributeerror
# -collections-has-no-attribute-callable-using-beautifu
import collections
import shutil
from pathlib import Path

collections.Callable = collections.abc.Callable
from settings import TARGET_RESULTS,TARGET_RESULTS_BEER_ME,HOST,HEADERS
import requests
from bs4 import BeautifulSoup

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
            link.get("href")
            for link in psoup.find_all("a")
            if link.get("href").__contains__("/racing/raceresults/_")
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
                            continue
                            # print(child)
                        cnt += 1
                        # print(data_cell.get_text(strip=True), end="\t")
                        csv_file.write(data_cell.get_text(strip=True) + "\t")
                    if cnt > 1:
                        csv_file.write("\n")
    else:
        print(f"End of {year} results.")
    return race_dates


def copy_race_dates(prace_dates: list):
    for race in prace_dates:
        # print(f"{TARGET_RESULTS_BEER_ME}\\{race}")
        my_file = Path(f"{TARGET_RESULTS_BEER_ME}\\{race}")
        if not my_file.is_file():
            print(
                f"-- Copying {Path(my_file)} to \n "
                f"{TARGET_RESULTS_BEER_ME}\\{race}")
            shutil.copy2(f"{TARGET_RESULTS}\\{race}",
                         f"{TARGET_RESULTS_BEER_ME}")  # copy2 preserves
            # metadata


if __name__ == "__main__":
    race_dates = []
    for year in range(2026, 2027):
        print(f"Processing year: {year}")
        url = f"{HOST}{year}"
        try:
            if soup := bs(url):
                race_dates = process_year_to_date_results(soup)
            else:
                print(f"No data found for year {year}")
        except Exception as e:
            exit(e.__str__())
    copy_race_dates(race_dates)
