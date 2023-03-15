import time
import json
from bs4 import BeautifulSoup
import requests
from random import randint

from constants import (
    EXPORT_PATH,
    TV_REQUEST_TYPE,
    MOVIES_REQUEST_TYPE
)


def export_json_to_file(json_content, request_type):
    """This method saves json data to a file"""

    current_date = time.strftime("%Y%m%dT%H%M%S")

    if request_type in (TV_REQUEST_TYPE, MOVIES_REQUEST_TYPE):
        export_file_path = f'{EXPORT_PATH}{request_type}_{current_date}.json'
        with open(export_file_path, 'w', encoding='utf8') as outfile:
            json.dump(json_content, outfile, ensure_ascii=False)
        #TODO: logger instead of print
        print(f'Netflix {request_type} charts exported to \'{export_file_path}\'.')
    else:
        print('Wrong request type passed.')


def parse_rank_position_soup(rank_position_html_src: BeautifulSoup):
    """This one is for parsing film/tv series rank info to a dictionary"""

    movie_data = {}
    movie_data['position'] = rank_position_html_src.find('span', class_='rankingType__position').text
    movie_data['title'] = rank_position_html_src.find('h2', class_='rankingType__title').text.strip()
    # movie_data['year'] = rank_position_div_src.find(class_='film__production-year').text.strip().replace(')', '').replace('(','')
    # movie_data['rating'] = rank_position_div_src.find(class_='rate__value').text
    # raw_rate_count = rank_position_div_src.find(class_='rate__count').text
    # clean_rate_count = raw_rate_count.replace('oceny', '').replace('ocen', '').strip().replace(' ', '')
    # movie_data['rate_count'] = clean_rate_count
    return movie_data


def get_ranks(rank_site_url: str):
    """This method returns a list of dictionaries for positions in a rank """

    print(f'Connecting to {rank_site_url}') # change to log debug
    get_html = requests.get(rank_site_url).text
    soup = BeautifulSoup(get_html, 'lxml')

    rank = soup.find('div', class_='page__container rankingTypeSection__container')
    raw_movies_list = rank.find_all('div', class_='rankingType hasVod')

    return [parse_rank_position_soup(raw_movie) for raw_movie in raw_movies_list]


def choose_random_position(positions: list) -> dict:
    """Choose random position from a given list"""

    if positions:
        random_position = randint(1, len(positions)-1)
        return positions[random_position]
    else:
        #log error
        return
