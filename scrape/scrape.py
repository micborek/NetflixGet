import requests
from bs4 import BeautifulSoup
import json
import time

from constants import (
    TV_SOURCE,
    MOVIES_SOURCE
)


class Scraper:

    def scrape(self):
        """Main logic behind the scraper"""

        self.get_ranks(TV_SOURCE)

    def export_json(self, json_content, req_type):
        """This method saves json data to file"""

        path = 'scrape/export/'
        current_date = time.strftime("%Y%m%dT%H%M%S")

        if req_type.upper() == 'TV':
            file_dir_tv = f'{path}TV_SERIES_{current_date}.json'
            with open(file_dir_tv, 'w', encoding='utf8') as outfile:
                json.dump(json_content, outfile, ensure_ascii=False)
            print(f'Netflix Tv-series charts exported to \'{file_dir_tv}\'.')

        if req_type.upper() == 'MOVIE':
            file_dir_movie = f'{path}MOVIES_{current_date}.json'
            with open(file_dir_movie, 'w', encoding='utf8') as outfile:
                json.dump(json_content, outfile, ensure_ascii=False)
            print(f'Netflix movies charts exported to \'{file_dir_movie}\'.')

    def get_data_to_json(self, req_type: str = ''):
        """Export json file for tv series, films or both by default"""

        # this exports json if method called with a parameter
        if req_type.upper() == 'TV' or req_type.upper() == 'MOVIE':
            json_content = self.get_ranks_list(req_type)
            self.export_json(json_content, req_type)

        # this exports json if method called without a parameter
        else:
            for req_type in ['TV', 'MOVIE']:
                json_content = self.get_ranks_list(req_type)
                self.export_json(json_content, req_type)

    def get_ranks_list(self, req_type: str):
        """This is the main method - it returns list of dictionaries
        for a requested type - either movies - 'movie' or tv series - 'tv'"""

        if req_type.upper() == 'TV':
            movies_list = self.get_movies(TV_SOURCE)
        elif req_type.upper() == 'MOVIE':
            movies_list = self.get_movies(MOVIES_SOURCE)
        else:
            print(f'The given parameter {req_type} is incorrect.')

        if movies_list:
            return movies_list

        return False

    def get_ranks(self, rank_site_url: str):
        """This method returns a list of dictionaries for positions in a rank """

        get_html = requests.get(rank_site_url).text
        soup = BeautifulSoup(get_html, 'lxml')

        rank = soup.find('div', class_='page__container rankingTypeSection__container')
        raw_movies_list = rank.find_all('div', class_='rankingType hasVod')

        return [self.parse_rank_position_soup(raw_movie) for raw_movie in raw_movies_list]

    def parse_rank_position_soup(self, rank_position_div_src: BeautifulSoup):
        """This one is for parsing film/tv series rank info to a dictionary"""

        movie_data = {}
        movie_data['position'] = rank_position_div_src.find('span', class_='rankingType__position').text
        movie_data['title'] = rank_position_div_src.find('h2', class_='rankingType__title').text.strip()
        # movie_data['year'] = rank_position_div_src.find(class_='film__production-year').text.strip().replace(')', '').replace('(','')
        # movie_data['rating'] = rank_position_div_src.find(class_='rate__value').text
        # raw_rate_count = rank_position_div_src.find(class_='rate__count').text
        # clean_rate_count = raw_rate_count.replace('oceny', '').replace('ocen', '').strip().replace(' ', '')
        # movie_data['rate_count'] = clean_rate_count
        return movie_data


if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape()
