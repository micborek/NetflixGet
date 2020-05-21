import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.filmweb.pl/ranking/vod/netflix').text
soup = BeautifulSoup(r, 'lxml')


def get_movies_soup():

    rank = soup.find('div', class_='ranking__list')
    positions = rank.find_all('div', class_='item place')

    return positions


def parse_movie_soup(movie_in: BeautifulSoup):
    movie_dict = {}
    x = movie_in.find('div', class_='ranking__position')
    foo = 'bar'


raw_list = get_movies_soup()

for movie in raw_list:
    parse_movie_soup(movie)

print(raw_list)