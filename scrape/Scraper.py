from constants import (
    TV_SOURCE_URL,
    MOVIES_SOURCE_URL,
    TV_REQUEST_TYPE,
    MOVIES_REQUEST_TYPE
)
from utils import (
    get_ranks,
    choose_random_position
)

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class Scraper:
    """Scraper class"""

    def __init__(self):
        self.movies_list = []
        self.tv_list = []
        self.random_choice = {}

    def scrape(self, request_type):
        """Scrape data for request types"""

        if request_type == TV_REQUEST_TYPE and not self.tv_list:
            self.tv_list = get_ranks(TV_SOURCE_URL)
        elif request_type == MOVIES_REQUEST_TYPE and not self.movies_list:
            self.movies_list = get_ranks(MOVIES_SOURCE_URL)
        else:
            log.debug('Using already scraped data.')

    def randomize_tv(self):
        """Choose random position for TV series"""
        self.random_choice = choose_random_position(self.tv_list)

    def randomize_movies(self):
        """Choose random position for movies"""
        self.random_choice = choose_random_position(self.movies_list)

    def print_result(self):
        """Print random position result"""
        print(self.random_choice)

    def export_json_to_file(self):
        """Export scraped data to json"""

        # TODO: develop this
