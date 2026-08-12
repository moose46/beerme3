import sqlite3
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup


from settings import HEADERS
import collections
collections.Callable = collections.abc.Callable
import sqlite3
from sqlite3 import Error
DB_FILENAME = "bets.db"
try:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
except Error as e:
    print(f"Error: {DB_FILENAME} {e}")
    exit()

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


@dataclass
class Schedule:
    soup: BeautifulSoup = bs("https://www.espn.com/racing/schedule")
    race_date : str = None
    results_url : str = None
    race_name : str = None
    track_name : str = None
    track_id: int = None
    starting_grid_url: str = None
    tv: str = None
    time: str = None
    race_track: str = None
    def scrape_schedule(self):
        if self.soup:
            for tr in self.soup.find_all("tr"):
                try:
                    print(tr.find_all('a')[0]['href'])
                except Exception as e:
                    continue
                try:
                    print(tr.find_all('a')[1]['href'])
                except Exception as e:
                    pass

                # print(tr.find("td").get_text())
                for td in tr.find_all("td"):
                    x = td.get_text(strip=True, separator='\n')
                    print(td.get_text(strip=True, separator=','))
                pass
                print()
if __name__ == "__main__":
    schedule = Schedule()
    schedule.scrape_schedule()
