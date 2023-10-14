import sys
from art import *
from tabulate import tabulate
from imdbfilmscrap import films_scrap


def main():
    # Outputs program logo.
    print(program_logo(), end="")
    # Outputs program menu of the moods.
    print(mood_menu(), end="")
    # Prompts user to type his actual mood by corresponding number.
    mood: str = get_mood()
    # Outputs 5 films, then outputs navigation menu and prompts to chose menu option.
    get_films(mood)
    print(navigation_menu())
    get_navigation_option(mood)


def program_logo(name: str = "Moodify", font: str = "varsity"):
    """
    Converts name of the program from text format to ASCII format.
    By the default, converts 'MOODIFY' to ASCII art using 'varsity' font.
    :param name: The text to be converted to ASCII art.
    :type name: str
    :param font: The font to be used for text convert.
    :type font: str
    :raises ValueError: If name or font is not valid.
    :return: ASCII art of the program name.
    :rtype: str
    """

    # Try-except block to handle ValueError exception.
    try:
        # Defines object of the art class with name and font attributes.
        intro = text2art(name, font)
    except:
        # Raises ValueError if name or font is not valid.
        raise ValueError("Please enter valid name or font while calling 'program_logo' function.")
    # If name and font are valid, returns ASCII art of the program name.
    return intro


def mood_menu() -> str:
    """
    Skeleton of the mood menu.
    :return: 'Mood menu' with a few options to choose from.
    :rtype: fstr
    """

    # Headers for table. Must remain as empty list.
    headers: list = []
    # Table raw's with option per each row.
    table: list = [
        ["TYPE:", "1️⃣", "IF YOU FEELING", "😁", "HAPPY"],
        ["TYPE:", "2️⃣", "IF YOU FEELING", "😌", "CALM"],
        ["TYPE:", "3️⃣", "IF YOU FEELING", "😔", "SAD"],
    ]
    # Table font.
    tablefmt: str = "pretty"

    # Defines object of the tabulate class.
    md_menu = tabulate(table, headers, tablefmt)
    # Returns formatted text to main module.
    return f"\n💭Mood menu:\n{md_menu}"


def get_mood() -> str:
    """
    Prompts user to type his actual mood by corresponding number.
    :return: User current mood. "1" -> "HAPPY", "2 -> "CALM", "3" -> "SAD".
    :rtype: str
    """

    # Defines dictionary with mood options.
    mood_dict = {"1": "HAPPY", "2": "CALM", "3": "SAD"}
    # Defines number of attempts to type valid option.
    attempts = 5
    # Prompts user for the input, until conditions satisfied.
    while attempts > 0:
        user_mood = input("\nType the number, followed by the 'Enter' button: ").strip()
        #
        if attempts > 0:
            # Checking if user input is in mood_dict.
            if user_mood in mood_dict:
                # If user input is in mood_dict, returns corresponding value.
                return mood_dict[user_mood]
            # If not, outputs mood menu and prompts user to type valid option.
            elif user_mood not in mood_dict:
                # Decreases number of attempts by 1.
                attempts -= 1
                # If user input is not in mood_dict, prompts user to type valid option.
                print(f"\nOption doesn't exist. Please type valid option number.\n{mood_menu()}")


def navigation_menu():
    """
    Navigation menu.
    :param: user current mood.
    :type: str
    :return: 'Navigation menu' with a few options to choose from.
    :rtype: fstr
    """
    # Defines header for the table. Must remain as empty list.
    headers: list = []
    # Defines table raw's with option per each row.
    table: list = [
        ["TYPE:", "1️⃣", "TO FIND MORE FILMS FOR YOUR ACTUAL MOOD"],
        ["TYPE:", "2️⃣", "TO CHANGE MOOD"],
        ["TYPE:", "3️⃣", "TO EXIT THE PROGRAM"],
    ]
    # Defines table font.
    tablefmt: str = "pretty"
    # Defines object of the tabulate class.
    navi_menu = tabulate(table, headers, tablefmt)
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
            get_films(
                user_mood
            )  # Generates new films with the originally passed attribute.
            print(navigation_menu())  # Outputs navigation menu.
        if menu_option == "2":
            print(mood_menu())
            user_mood = get_mood()
            get_films(user_mood)
            print(navigation_menu())
            get_navigation_option(user_mood)
        if menu_option == "3":
            print("Successful shutdown. See you later! 👋")
            sys.exit(0)


def get_films(user_mood):
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
