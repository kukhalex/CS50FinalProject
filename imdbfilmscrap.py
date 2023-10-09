import requests
from bs4 import BeautifulSoup


def films_scrap(mood: str):
    """
        Based on the param, - which is the users actual mood.
        Scrap some films from the IMDB web-site.
        :param: mood
        :type: str
        :raise: ...
        :return: ...
        :rtype: ...
        """

    # Target URL (IMDB). Based on the users mood it consists of a different genres.
    if mood == "HAPPY":
        # Getting text response from url.
        happy_url = "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=adventure&sort=user_rating,desc"
        html_text = requests.get(happy_url).text
    if mood == "CALM":
        # Getting text response from url.
        calm_url = "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=drama&sort=user_rating,desc"
        html_text = requests.get(calm_url).text
    if mood == "SAD":
        sad_url = "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=comedy&sort=user_rating,desc"
        html_text = requests.get(sad_url).text

    # Creating object of the BeautifulSoup.
    soup = BeautifulSoup(html_text, "lxml")
    # Getting films on the first page.
    films = soup.find_all("div", class_="lister-item-content")

    # Loop over each film in films variable and getting details for each film, such as genre, length etc.
    for film in films:
        # Getting film name.
        film_name = " ".join(
            i for i in (film.find("h3", class_="lister-item-header").text.split())[1:-1]
        )
        # Getting film IMDB rating.
        film_rating = film.find("strong", class_="").text
        # Getting film genre / lenghth.
        film_details = film.find("p", "text-muted").text.split()
        # Here we're checking if first index responds for the availability of the PG status and based
        # on that detecting genre and length values indexes, then declaring them in the variables.
        if film_details[0] in ["18", "ZA", "R", "G", "PG", "PG-13", "NC-17"]:
            film_genre = " ".join(i for i in film_details[5::])
            film_length = " ".join(i for i in film_details[2:4])
        else:
            film_genre = " ".join(i for i in film_details[3::])
            film_length = " ".join(i for i in film_details[0:2])
        # Getting film director and starring actors.
        film_director_actors = " ".join(i for i in (film.find("p", class_="").text.split()))

        print(
            f"""
        🪄Movie suggestion for you:
        🎬Film title: {film_name}
        ⭐IMDB Rating: {film_rating}
        🎭Genre: {film_genre}
        ⌛Length: {film_length} 
        🧑‍🎤{film_director_actors}
        """
        )
