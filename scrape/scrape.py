import requests
from bs4 import BeautifulSoup

"""This part is for developing/testing offline"""
with open('scrape/movies.html', "r", encoding="utf-8") as file:
    movies_html = file.read()
with open('scrape/tv_series.html', "r", encoding="utf-8") as file:
    tv_series_html = file.read()


class Scrape:

    # MOVIES_SOURCE = 'https://www.filmweb.pl/ranking/vod/netflix'
    # TV_SOURCE = 'https://www.filmweb.pl/ranking/vod/netflix/serial'
    MOVIES_SOURCE = movies_html
    TV_SOURCE = tv_series_html

    def get_ranks_list(self, req_type: str):
        """This is the main method - it returns list of dictionaries
        for a requested type - either movies - 'movie' or tv series - 'tv'"""

        if req_type.upper() == 'TV':
            movies_list = self.get_movies(self.TV_SOURCE)
        elif req_type.upper() == 'MOVIE':
            movies_list = self.get_movies(self.MOVIES_SOURCE)
        else:
            print(f'The given parameter {req_type} is incorrect.')

        return movies_list

    def get_movies(self, soup_source: str):
        """This method returns a list of dictionaries for positions in a rank"""

        # get_html = requests.get(soup_source).text
        # soup = BeautifulSoup(get_html, 'lxml')
        soup = BeautifulSoup(soup_source, 'lxml')
        rank = soup.find('div', class_='ranking__list')
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
        movie_data['year'] = movie_in.find(class_='film__production-year').text.strip().replace(')', '').replace('(', '')
        return movie_data


scraper = Scrape()
result = scraper.get_ranks_list('movie')

print(result)
