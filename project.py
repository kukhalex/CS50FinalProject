import sys
from art import *
from tabulate import tabulate
from imdbfilmscrap import films_scrap


def main():
    # Outputs program name in ascii format.
    print(program_logo())
    # Outputs program mood menu and prompts to chose menu option.
    print(mood_menu())
    mood: str = get_mood_option()
    # Outputs 5 films, then outputs navigation menu and prompts to chose menu option.
    get_films(mood)
    print(navigation_menu())
    get_navigation_option(mood)


def program_logo():
    """
    Converts name of the program from text format to ASCII format.
    :return: text in ASCII format.
    :rtype: str
    """
    # Defines program name that will be formatted to ASCII format.
    ascii_logo: str = "MOODIFY"
    # Defines font that will be used while formatting text to ASCII.
    ascii_font: str = "varsity"
    # Defines object of art class, params must include 'text' and 'font'.
    intro = text2art(ascii_logo, ascii_font)
    # Returns formatted text to main module.
    return intro


def mood_menu():
    """
    Simple user-friendly menu, created with tabulate library.
    :return: 'Mood menu' with a few options to choose from.
    :rtype: fstr
    """
    # Headers for table. Not used in our case. Must remain as empty list.
    HEADERS: list = []
    # Table rows with option per each row.
    TABLE: list = [
        ["PRESS BUTTON:", "1️⃣", "IF YOU FEELING", "😁", "HAPPY"],
        ["PRESS BUTTON:", "2️⃣", "IF YOU FEELING", "😌", "CALM"],
        ["PRESS BUTTON:", "3️⃣", "IF YOU FEELING", "😔", "SAD"],
    ]
    # Defines table font.
    TABLEFMT: str = "pretty"
    # Defines object of the tabulate class.
    md_menu = tabulate(TABLE, HEADERS, TABLEFMT)
    # Return tabulated choices for user.
    return f"\n💭Mood menu:\n{md_menu}"


def get_mood_option():
    """
    Prompts user to type his actual mood, based on the mood_menu function.
    :return: user current mood. '1' = 'HAPPY', '2' = 'CALM', '3' = 'SAD'.
    :rtype: str
    """
    # Prompts user for the input, until conditions satisfied.
    while True:
        user_mood = input("\nType the number, followed by the 'Enter' button: ").strip()
        # Checking if user input matching to the conditions and if 'True' returns corresponding value.
        if not user_mood or user_mood not in ["1", "2", "3"]:
            print("\nPlease enter valid number:\n", mood_menu())
        if user_mood == "1":
            return "HAPPY"
        if user_mood == "2":
            return "CALM"
        if user_mood == "3":
            return "SAD"


def navigation_menu():
    """
    Navigation menu.
    :param: user current mood.
    :type: str
    :return: 'Navigation menu' with a few options to choose from.
    :rtype: fstr
    """
    # Defines header for the table. Must remain as empty list.
    HEADERS: list = []
    # Defines table raw's with option per each row.
    TABLE: list = [
        ["PRESS BUTTON:", "1️⃣", "TO FIND MORE FILMS FOR YOUR ACTUAL MOOD"],
        ["PRESS BUTTON:", "2️⃣", "TO CHANGE MOOD"],
        ["PRESS BUTTON:", "3️⃣", "TO EXIT THE PROGRAM"],
    ]
    # Defines table font.
    TABLEFMT: str = "pretty"
    # Defines object of the tabulate class.
    navi_menu = tabulate(TABLE, HEADERS, TABLEFMT)
    # Outputs tabulated choices for user.
    return f"🧭Navigation menu:\n,{navi_menu}"


def get_navigation_option(user_mood):
    """
    Prompts user to type option he would like to chose from navigation menu.
    :return: user navigation menu option.
    :rtype: ...
    """
    # Prompts user for the input, until conditions satisfied.
    while True:
        menu_option = input("\nType a number, followed by 'Enter' button: ")
        if not menu_option or menu_option not in ["1", "2", "3"]:
            print("\nPlease enter valid number:\n", navigation_menu())
        if menu_option == "1":
            get_films(user_mood) # Generates new films with the originally passed attribute.
            print(navigation_menu()) # Outputs navigation menu.
        if menu_option == "2":
            print(mood_menu())
            user_mood = get_mood_option()
            get_films(user_mood)
            print(navigation_menu())
            get_navigation_option(user_mood)
        if menu_option == "3":
            print("Successful shutdown. See you later! 👋")
            sys.exit(0)


def get_films(user_mood: str) -> str:
    """
    Generating 5 films for the user.
    :param: user current mood.
    :type: str
    :return: 5 films with description for each one.
    :rtype: str
    """
    # Using 'imdbfilmscrap.py' module to get films.
    films = films_scrap(user_mood)

    # Returns 5 scrapped films.
    print(f"\n🪄Here are five films to watch while you feeling {user_mood.lower()}:\n")
    for film in films:
        print(
            f'📽️Title: {film["Title"]}\n'
            f'⭐IMDB Rating: {film["IMDB Rating"]}\n'
            f'⌛Length: {film["Length"]}\n'
            f'🎭Genre: {film["Genre"]}\n'
            f'🎬By: {film["By"]}\n'
        )


if __name__ == "__main__":
    main()
