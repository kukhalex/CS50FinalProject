from art import *
from tabulate import tabulate
from imdbfilmscrap import films_scrap


def main():
    # Output programs logo/name in ascii format.
    print(welcome())

    # Calling user to choose current type of the mood.
    mood = get_mood()

    # Looking for the activities based on users mood.
    if mood:
        films = films_scrap(mood)
        print(f'\n🪄Here are five films to watch while you feeling {mood.lower()}:\n')
        for film in films:
            print(
                f'🎬Title: {film["Title"]}\n'
                f'⭐IMDB Rating: {film["IMDB Rating"]}\n'
                f'⌛Length: {film["Length"]}\n'
                f'🎭Genre: {film["Genre"]}\n'
                f'🧑‍🎤By: {film["By"]}\n'
            )


def welcome():
    """
    Converts program name into ascii art.
    :param: None
    :type: None
    :raise: artError,...
    :return: Program name in ascii formatted art.
    :rtype: str
    """

    # Sets logo output name. Changeable - could be any other name.
    ascii_logo: str = "MOODIFY"
    # Sets font for logo name output. Changeable - look for 'art' library documentation.
    ascii_font: str = "varsity"
    # Creating an object with attributes.
    intro = text2art(ascii_logo, ascii_font)
    # Returns str to main function.
    return intro

def get_mood():
    """
    Calling user to make a choice of his current mood based on 3 options.
    :param: None
    :type: None
    :raise: ...
    :return: User mood based on his choice 'HAPPY', 'CALM' or 'SAD'
    :rtype: str
    """

    # Remains to automatically create columns based on the raw's values.
    HEADERS: list = []
    # For each row sets str with an option to choose from.
    TABLE: list = [
        ["PRESS BUTTON:", "1️⃣", "IF YOU FEELING", "😁", "HAPPY"],
        ["PRESS BUTTON:", "2️⃣", "IF YOU FEELING", "😌", "CALM"],
        ["PRESS BUTTON:", "3️⃣", "IF YOU FEELING", "😔", "SAD"],
    ]
    # Sets tabulation font. Changeable - look for 'tabulate' library documentation.
    TABLEFMT: str = "pretty"
    # Outputs tabulated choices for user.
    choices = tabulate(TABLE, HEADERS, TABLEFMT)
    print(choices)
    # Waiting for user to input valid value.
    while True:
        user_choice = input("\nType the number, followed by the 'Enter' button: ").strip()
        # Checking correctness of the users input.
        if not user_choice or user_choice not in ["1", "2", "3"]:
            print("\nPlease enter valid number:\n", choices)
        if user_choice == "1":
            return "HAPPY"
        if user_choice == "2":
            return "CALM"
        if user_choice == "3":
            return "SAD"


if __name__ == "__main__":
    main()
