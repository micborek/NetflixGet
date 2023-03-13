from constants import (
    TV_SOURCE_URL,
    MOVIES_SOURCE_URL,
    TV_REQUEST_TYPE,
    MOVIES_REQUEST_TYPE
)
from utils import (
    get_ranks
)


class Scraper:
    """Scraper class"""

    def __init__(self, request_type):
        self.request_type = request_type
        self.movies_list = []
        self.tv_list = []

    def scrape(self):
        """Scrape data for request types"""

        if self.request_type == TV_REQUEST_TYPE:
            self.tv_list = get_ranks(TV_SOURCE_URL)
            print(self.tv_list)
        elif self.request_type == MOVIES_REQUEST_TYPE:
            self.movies_list = get_ranks(MOVIES_SOURCE_URL)
        else:
            print('Wrong request type.')

    def export_json_to_file(self):
        """Additional method for json export"""

        #TODO: develop this
