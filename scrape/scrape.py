import requests
from bs4 import BeautifulSoup
import json
import time


class Scraper:

    def scrape(self):
        """Main logic behind the scraper"""
        self.get_movies()

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
            movies_list = self.get_movies(self.TV_SOURCE)
        elif req_type.upper() == 'MOVIE':
            movies_list = self.get_movies(self.MOVIES_SOURCE)
        else:
            print(f'The given parameter {req_type} is incorrect.')

        if movies_list:
            return movies_list

        return False

    def get_movies(self, soup_source: str):
        """This method returns a list of dictionaries for positions in a rank """

        get_html = requests.get(soup_source).text
        soup = BeautifulSoup(get_html, 'lxml')

        # this one is for testing offline
        # soup = BeautifulSoup(soup_source, 'lxml')

        rank = soup.find('div', class_='page__container rankingTypeSection__container')
        raw_movies_list = rank.find_all('div', class_='item place')

        movies_list = []
        for raw_movie in raw_movies_list:
            movies_list.append(self.parse_movie_soup(raw_movie))

        return movies_list

    def parse_movie_soup(self, movie_in: BeautifulSoup):
        """This one is for parsing film/tv series rank info to a dictionary"""

        movie_data = {}
        movie_data['position'] = movie_in.find('div', class_='ranking__position').text
        movie_data['title'] = movie_in.find('a', class_='film__link').text.strip()
        if movie_in.find('div', class_='film__original'):
            movie_data['original_title'] = movie_in.find('div', class_='film__original').text.strip()
        movie_data['year'] = movie_in.find(class_='film__production-year').text.strip().replace(')', '').replace('(',
                                                                                                                 '')
        movie_data['rating'] = movie_in.find(class_='rate__value').text
        raw_rate_count = movie_in.find(class_='rate__count').text
        clean_rate_count = raw_rate_count.replace('oceny', '').replace('ocen', '').strip().replace(' ', '')
        movie_data['rate_count'] = clean_rate_count
        return movie_data


if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape()
