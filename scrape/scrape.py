from Scraper import Scraper
from constants import (
    TV_REQUEST_TYPE,
    MOVIES_REQUEST_TYPE
)


def user_io_handler():
    while True:
        users_choice = input('Would you like to choose a random (T)v-series or a (M)ovie? You can also(Q)uit').strip().lower()
        if users_choice in ('m', 't'):
            if users_choice == 't':
                scraper = Scraper(TV_REQUEST_TYPE)
            else:
                scraper = Scraper(MOVIES_REQUEST_TYPE)
            scraper.scrape()
        elif users_choice == 'q':
            print('Program stopped.')
            break
        else:
            print('Wrong command entered. Try again.')


if __name__ == "__main__":
    user_io_handler()
