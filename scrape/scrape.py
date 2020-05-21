import requests
from bs4 import BeautifulSoup

movies_rank_link = 'https://www.filmweb.pl/ranking/vod/netflix'
tv_series_link = 'https://www.filmweb.pl/ranking/vod/netflix/serial'

r = requests.get(movies_rank_link).text
soup = BeautifulSoup(r, 'lxml')


def get_movies_soup():

    rank = soup.find('div', class_='ranking__list')
    positions = rank.find_all('div', class_='item place')

    return positions


def parse_movie_soup(movie_in: BeautifulSoup):
    """This one is for parsing film info to a dictionary"""

    movie_data = {}
    movie_data['position'] = movie_in.find('div', class_='ranking__position').text
    movie_data['title'] = movie_in.find('a', class_='film__link').text.strip()
    if movie_in.find('div', class_='film__original'):
        movie_data['original_title'] = movie_in.find('div', class_='film__original').text.strip()
    movie_data['year'] = movie_in.find(class_='film__production-year').text.strip().replace(')', '').replace('(', '')
    return movie_data


raw_list = get_movies_soup()

movies = []
for movie in raw_list:
    movies.append(parse_movie_soup(movie))

print(movies)
