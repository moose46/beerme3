import collections
import sqlite3
from sqlite3 import Error

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

DB_FILENAME = "../bets.db"
collections.Callable = collections.abc.Callable

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 "
                  "Safari/537.36 Edg/147.0.0.0"
}

try:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
except Error as e:
    print(f"Error: {DB_FILENAME} {e}")
    exit()


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


def get_drivers(soup):
    driver_dict = {}
    drivers = []
    # for team in soup.find_all(_class="benefit-card-title"):
    # for team in soup.find_all("h3"):
    # for team in soup.find_all("div", {"class": "automated-entry-list-driver"}):
    # for team in soup.find_all("div"):
    # for driver in soup.find_all("div", "automated-entrylist-driver"):
    for driver in soup.find_all("div", "automated-entrylist-row-content-item"):
        # x = soup.findAll('h3', {'class', "benefit-card-title"})
        # driver_nascar_url = driver.find_all("div", "automated-entrylist-driver")
        try:
            driver_nascar_url = driver.find("a", target="_blank").attrs["href"]
        except Exception as e:
            print(f"Error: {driver_nascar_url}")
            # exit(f"Error: {driver_nascar_url} {e.__str__()}")
        driver_name = driver.find("div", "automated-entrylist-driver").get_text()
        driver_team = driver.find("div", "automated-entrylist-driver-team").get_text()
        driver_crew_chief = driver.find("div", "automated-entrylist-driver-crew-chief").get_text()
        driver_home_town = driver.find("div", "automated-entrylist-driver-hometown").get_text()
        driver_home_sponser = driver.find("div", "automated-entrylist-driver-sponsor").get_text()
        driver_age = driver.find("div", "automated-entrylist-driver-age").get_text()
        driver_dict["driver-name"] = driver_name
        driver_dict["sponsor"] = driver_home_sponser
        driver_dict["driver-age"] = driver_age
        driver_dict["crew-chief"] = driver_crew_chief
        driver_dict["driver-team"] = driver_team
        driver_dict["driver-nascar-url"] = driver_nascar_url
        driver_dict["driver-home-town"] = driver_home_town
        drivers.append(driver_dict)
        driver_dict = {}
        pass
    for driver in drivers:
        print(driver)
    return drivers


def insert_teams_into_db(drivers):
    update_query = """update drivers
                      set crew_chief=?,
                          team=?,
                          nascar_driver_url=?,
                          age=?,
                          home_town=?, sponsor=?

                      where driver_name = ?"""

    for driver in drivers:
        try:
            driver_tuple = (driver["crew-chief"], driver["driver-team"], driver["driver-nascar-url"], driver["driver-age"], driver["driver-home-town"],
                            driver["sponsor"],driver["driver-name"],)
            cursor.execute(update_query, driver_tuple)
            conn.commit()
        except Error as e:
            pass


if __name__ == "__main__":
    driver = webdriver.Chrome()
    # driver.get("https://www.nascar.com/news-media/2026/08/10/2026-nascar-cup-series-entry-list-for-richmond-raceway/")
    driver.get("https://www.nascar.com/news-media/2026/08/03/2026-nascar-cup-series-entry-list-for-iowa-speedway/")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    race_drivers = get_drivers(soup)
    insert_teams_into_db(race_drivers)
    driver.quit()
# insert_teams_into_db(teams=get_teams(soup=soup))
