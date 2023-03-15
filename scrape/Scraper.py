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


class Scraper:
    """Scraper class"""

    def __init__(self):
        self.movies_list = []
        self.tv_list = []

    def scrape(self, request_type):
        """Scrape data for request types"""

        if request_type == TV_REQUEST_TYPE and not self.tv_list:
            self.tv_list = get_ranks(TV_SOURCE_URL)
        elif request_type == MOVIES_REQUEST_TYPE and not self.movies_list:
            self.movies_list = get_ranks(MOVIES_SOURCE_URL)
        else:
            print('Using already scraped data.') # log


    def randomize_tv(self):
        return choose_random_position(self.tv_list)

    def randomize_movies(self):
        return choose_random_position(self.movies_list)

    def print_result(self):
        pass


    def export_json_to_file(self):
        """Additional method for json export"""

        #TODO: develop this
