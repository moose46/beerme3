import collections

# Needed for BeautifulSoup
collections.Callable = collections.abc.Callable
import requests
from bs4 import BeautifulSoup
import logging
import logging.config

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 "
                  "Safari/537.36 Edg/147.0.0.0"
}



def bs(url):
    response = requests.get(url, headers=HEADERS)
    # print(f"{response}")
    if response.status_code in [200]:
        soup_is_ready = BeautifulSoup(response.content, "html.parser")
        logger.info(f"Response Code: {response.status_code}")
        return soup_is_ready
    elif response.status_code == 202:
        logger.info(f"{url} Response Code: {response.status_code}")
        exit(f"No data found for {url}, response_code = {response.status_code}")
    else:
        logging.exception(f"Failed to retrieve data from {url}")
        return None


if __name__ == "__main__":
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger(__name__)
    logger.info(f"Entered driver.py {logger.name}")
    soup = bs("https://www.espn.com/racing/raceresults/_/series/sprint/raceId/202608290009")
    if soup:
        logger.debug(f"{soup}")

