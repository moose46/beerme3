import collections
import sqlite3
from sqlite3 import Error

import requests
from bs4 import BeautifulSoup

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


def get_teams(soup):
    team_dict = {}
    teams = []
    # for team in soup.find_all(_class="benefit-card-title"):
    # for team in soup.find_all("h3"):
    for team in soup.findAll('div', {'class', "benefit-card"}):
        # x = soup.findAll('h3', {'class', "benefit-card-title"})
        # if team.get_text(strip=True) == "FAQs":
        #     break
        team_name = team.find('h3', {'class', "benefit-card-title"}).text
        # print(f"{teams}")
        team_dict["team_name"] = team_name
        for href in team.find_all(id="benefit-card-button"):
            www = href.get("href")
        team_dict["team_url"] = www
        teams.append(team_dict)
        team_dict = {}
        # teams.append(team)
        # teams["team_url"] = www
        pass
    for team in teams:
        print(team)
    return teams


def insert_teams_into_db(teams):
    insert_query = """insert or replace into teams (team_name, team_url)
                      VALUES (?, ?)"""
    for team in teams:
        try:
            cursor.execute(insert_query, (team["team_name"], team["team_url"]))
            conn.commit()
        except Error as e:
            pass


if __name__ == "__main__":
    soup = bs("https://www.nascar.com/nascar-cup-series-teams/")

    insert_teams_into_db(teams=get_teams(soup=soup))
