import sys
from art import *
from tabulate import tabulate
from imdbfilmscrap import films_scrap


def main():
    # Outputs program logo in ascii format.
    program_logo()
    # Outputs program mood menu.
    mood_menu()
    # Getting users current mood.
    mood: str = get_mood()
    # Generate 5 films to watch based on the user mood.
    generate_films(mood)
    # Call navigation menu.
    navigation_menu(mood)


def program_logo() -> str:
    """
    Converts text to ASCII art.
    :param: None
    :type: None
    :raise: None
    :return: ASCII program logo.
    :rtype: str
    """
    # Sets string(program name) for ASCII output.
    ascii_logo: str = "MOODIFY"
    # Sets font for ASCII output.
    ascii_font: str = "varsity"
    # Creating object with pre-set attributes.
    intro: str = text2art(ascii_logo, ascii_font)
    # Return str to main function.
    return intro


def get_mood():
    """
    Prompts user for input (his actual mood).
    :param: None
    :type: None
    :raise: None
    :return: Users mood. '1' = 'HAPPY', '2' = 'CALM', '3' = 'SAD'.
    :rtype: str
    """
    while True:
        user_mood = input("\nType the number, followed by the 'Enter' button: ").strip()
        # Checking correctness of the users input.
        if not user_mood or user_mood not in ["1", "2", "3"]:
            print("\nPlease enter valid number:\n", mood_menu())
        if user_mood == "1":
            return "HAPPY"
        if user_mood == "2":
            return "CALM"
        if user_mood == "3":
            return "SAD"


def navigation_menu(mood):
    """
    Navigation menu.
    :param: None
    :type: None
    :raise: None
    :return: Program navigation menu.
    :rtype: str
    """
    # Remains to automatically create columns based on the raw's values.
    HEADERS: list = []
    # For each row sets str with an option to choose from.
    TABLE: list = [
        ["PRESS BUTTON:", "1️⃣", "TO FIND MORE FILMS FOR YOUR ACTUAL MOOD"],
        ["PRESS BUTTON:", "2️⃣", "TO CHANGE MOOD"],
        ["PRESS BUTTON:", "3️⃣", "TO EXIT THE PROGRAM"],
    ]
    # Sets tabulation font. Changeable - look for 'tabulate' library documentation.
    TABLEFMT: str = "pretty"
    # Creating tabulate object.
    navi_menu = tabulate(TABLE, HEADERS, TABLEFMT)
    # Outputs tabulated choices for user.
    print("🧭Navigation menu:\n", navi_menu)
    # Prompts user for input.
    while True:
        menu_option = input("Type a number, followed by 'Enter' button: ")

        if not menu_option or menu_option not in ["1", "2", "3"]:
            print("Please, type a valid number.")

        if menu_option == "1":
            generate_films(mood)
            navigation_menu(mood)

        if menu_option == "2":
            mood_menu()
            mood: str = get_mood()
            generate_films(mood)
            navigation_menu(mood)







def mood_menu():
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
    # Creating tabulate onject.
    md_menu = tabulate(TABLE, HEADERS, TABLEFMT)
    # Return tabulated choices for user.
    print("💭Mood menu:\n", md_menu)


def generate_films(user_mood: str) -> str:
    """
    Generating 5 films using imdb scrap module.
    :param: User mood.
    :type: str
    :raise: None
    :return: 5 films.
    :rtype: str
    """
    # Call to scrap module with 'mood' attribute.
    films = films_scrap(user_mood)
    # Output 5 films.
    print(f"\n🪄Here are five films to watch while you feeling {user_mood.lower()}:\n")
    for film in films:
        print(
            f'Title: {film["Title"]}\n'
            f'IMDB Rating: {film["IMDB Rating"]}\n'
            f'Length: {film["Length"]}\n'
            f'Genre: {film["Genre"]}\n'
            f'By: {film["By"]}\n'
        )


if __name__ == "__main__":
    main()
