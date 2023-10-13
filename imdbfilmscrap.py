import random
import requests
from bs4 import BeautifulSoup


def films_scrap(user_mood: str) -> list:
    """
    Scraps films from th IMDB web-site. Currently, only from the first page for each genre.
    :param: user_mood
    :type: str
    :return: list of films dictionaries
    :rtype: list
    """

    # Target URL, based of the 'user_mood' attribute.
    # Getting response from the target link in a text format.
    if user_mood == "HAPPY":
        happy_url = "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=comedy&sort=user_rating,desc"
        html_text = requests.get(happy_url).text
    if user_mood == "CALM":
        calm_url = "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=adventure&sort=user_rating,desc"
        html_text = requests.get(calm_url).text
    if user_mood == "SAD":
        sad_url = "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=drama&sort=user_rating,desc"
        html_text = requests.get(sad_url).text

    # Creating object of the BeautifulSoup. Must have attributes - of the target URL and parser type.
    soup = BeautifulSoup(html_text, "lxml")
    # Getting html data of the first page of the target URL.
    films = soup.find_all("div", class_="lister-item-content")

    # Holding 'n' numbers of the films. 'n' could be set to any int value in 'films_n' variable.
    formatted_films_list = []
    films_n = 5

    # Loop over each film in films variable and getting details for each film, such as genre, length etc.
    # Here we're using in-built func sample() of random module to take 5 random films out of our films list.
    for film in random.sample(films, films_n):
        # At each iteration sequence we're getting current film name.
        film_name = " ".join(
            i for i in (film.find("h3", class_="lister-item-header").text.split())[1:-1]
        )
        # At each iteration sequence we're getting current film IMDB rating.
        film_rating = film.find("strong", class_="").text
        # At each iteration sequence we're getting current film details (genre,length).
        film_details = film.find("p", "text-muted").text.split()
        # At each iteration sequence we're checking if first index corresponds for the availability
        # of the PG status and based on that, - detecting genre and length values indexes,
        # then declaring them in the variables.
        if film_details[0] in [
            "12",
            "16",
            "18",
            "ZA",
            "R",
            "G",
            "PG",
            "PG-13",
            "NC-17",
        ]:
            film_genre = " ".join(i for i in film_details[5::])
            film_length = " ".join(i for i in film_details[2:4])
        else:
            film_genre = " ".join(i for i in film_details[3::])
            film_length = " ".join(i for i in film_details[0:2])
        # At each iteration sequence we're getting current film director and stars(actors).
        film_director_actors = " ".join(
            i for i in (film.find("p", class_="").text.split())
        )
        # At each iteration sequence we're appending formatted data to out formatted films list.
        formatted_films_list.append(
            {
                "Title": film_name,
                "IMDB Rating": film_rating,
                "Genre": film_genre,
                "Length": film_length,
                "By": film_director_actors,
            }
        )
    return formatted_films_list
