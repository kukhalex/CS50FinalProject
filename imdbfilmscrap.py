import random
import re
import requests
from bs4 import BeautifulSoup


def films_scrap(mood: str) -> list:
    """
    Scraps films from th IMDB web-site.
    :param: mood
    :type: str
    :return: list of films dictionaries
    :rtype: list
    """

    # Defines target URL based on 'user_mood' argument.
    if mood == "HAPPY":
        html_url = (
            "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,"
            "&genres=comedy&genres=!drama,!adventure"
            "&release_date=2015-01-01,2023-10-31"
            "&count=100"
            "&sort=user_rating,desc"
        )
    elif mood == "CALM":
        html_url = (
            "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,"
            "&genres=adventure&genres=!drama,!comedy"
            "&release_date=2015-01-01,2023-10-31"
            "&count=100"
            "&sort=user_rating,desc"
        )
    elif mood == "SAD":
        html_url = (
            "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,"
            "&genres=drama&genres=!adventure,!comedy"
            "&release_date=2015-01-01,2023-10-31"
            "&count=100"
            "&sort=user_rating,desc"
        )

    # Getting response from the target link in a text format.
    html_text = requests.get(html_url).text
    # Parsing html text to the BeautifulSoup object.
    soup = BeautifulSoup(html_text, "lxml")
    # Getting all films from the soup object.
    films = soup.find_all("div", class_="lister-item-content")

    # Declaring empty list for films dictionaries.
    formatted_films_list = []
    # Declaring number of films to get from the all scraped films.
    films_n = 5

    # At each iteration sequence we're getting random film from the films list.
    for film in random.sample(films, films_n):
        # At each iteration sequence we're getting current film name.
        film_name = " ".join(
            i for i in (film.find("h3", class_="lister-item-header").text.split())[1:-1]
        )

        # At each iteration sequence we're getting current film year.
        film_year = "".join(
            film.find("span", class_="lister-item-year text-muted unbold")
            .text.replace("(", "")
            .replace(")", "")
        )

        # At each iteration sequence we're getting current film rating.
        film_rating = film.find("strong", class_="").text

        # At each iteration sequence we're getting current film details.
        film_details = film.find("p", "text-muted").text.split()

        # At each iteration sequence we're checking if first index corresponds for of the PG status.
        # If it does, we're getting film genre from index 5 to the end of the list.
        # Also getting film length from index 2 to 4.
        if match := re.search(r"[0-9]{2}[A-Z]?", film_details[0]):
            film_genre = " ".join(i for i in film_details[5::])
            film_length = " ".join(i for i in film_details[2:4])
        else:
            # If first index doesn't correspond for of the PG status.
            # We're getting film genre from index 3 to the end of the list.
            # Also getting film length from index 0 to 2.
            film_genre = " ".join(i for i in film_details[3::])
            film_length = " ".join(i for i in film_details[0:2])

        # At each iteration sequence we're getting current film director and actors.
        film_director_actors = " ".join(
            i for i in (film.find("p", class_="").text.split())
        )

        # At each iteration sequence we're appending film name, rating, genre, length, director and actors to the
        # formatted_films_list.
        formatted_films_list.append(
            {
                "Title": film_name,
                "Year": film_year,
                "IMDB Rating": film_rating,
                "Genre": film_genre,
                "Length": film_length,
                "By": film_director_actors,
            }
        )
    return formatted_films_list
