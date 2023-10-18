import sys
from art import *
from tabulate import tabulate
from imdbfilmscrap import films_scrap


def main():
    # Outputs program logo.
    print(program_logo(), end="")

    # Outputs program menu of the moods.
    print(mood_menu())
    # Prompts user to type his actual mood by corresponding number.
    mood: str = get_mood()
    # Outputs 5 films for the user.
    get_films(mood)

    # Outputs program navigation menu.
    print(navigation_menu())
    # Prompts user to type option number from navigation menu.
    option = get_navigation()
    #   If user typed "1", outputs 5 new films for the user.
    if option == "1":
        get_films(mood)
    #  If user typed "2", outputs program menu of the moods.
    elif option == "2":
        print(mood_menu())
        mood: str = get_mood()
        get_films(mood)
    # If user typed "3", outputs message and exits the program.
    elif option == "3":
        print("\nThank you for using Moodify. Program is shutting down.\n")
        sys.exit(0)


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
        raise ValueError(
            "Please enter valid name or font while calling 'program_logo' function."
        )
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
    return f"\n💭Mood menu: \n" f"{md_menu}"


def get_mood() -> str:
    """
    Prompts user to type his actual mood by corresponding number.
    :return: User current mood. "1" -> "HAPPY", "2 -> "CALM", "3" -> "SAD".
    :rtype: str
    :exits: If user exceeded number of attempts.
    """

    # Defines dictionary with mood options.
    mood_dict = {"1": "HAPPY", "2": "CALM", "3": "SAD"}
    # Defines number of attempts to type valid option.
    attempts = 5
    # Prompts user to type his actual mood by corresponding number from mood menu.
    for _ in range(attempts):
        user_mood = input("\nType the number, followed by the 'Enter' button: ").strip()
        # If user input is in mood_dict, calling get_films function with user_mood as an argument and na
        if user_mood in mood_dict:
            return mood_dict[user_mood]
        # If user input is not in mood_dict, outputs message and mood menu, then prompts user to type valid option.
        elif user_mood not in mood_dict:
            print(
                f"\nOption doesn't exist. Please type valid option number.\n"
                f"\n{mood_menu()}"
            )
    # If user exceeded number of attempts, outputs message and exits the program.
    print("\nYou have exceeded the number of attempts. Program is shutting down.\n")
    sys.exit(0)


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
        ["TYPE:", "1️⃣", "TO FIND MORE FILMS"],
        ["TYPE:", "2️⃣", "TO CHANGE MOOD"],
        ["TYPE:", "3️⃣", "TO EXIT THE PROGRAM"],
    ]
    # Defines table font.
    tablefmt: str = "pretty"
    # Defines object of the tabulate class.
    navi_menu = tabulate(table, headers, tablefmt)
    # Outputs tabulated choices for user.
    return f"\n🧭Navigation menu: \n" f"{navi_menu}"


def get_navigation():
    """
    Skeleton of the navigation menu.
    :return: User choice based on the navigation menu options.
    :rtype: ...
    """

    # Tuple with navigation options.
    navigation_options = ("1", "2", "3")
    # Defines number of attempts to type valid option.
    attempts = 5
    # Prompts user to type his actual mood by corresponding number from navigation menu.
    for _ in range(attempts):
        user_option = input("\nType a number, followed by 'Enter' button: ").strip()
        if user_option in navigation_options:
            return user_option
        else:
            print(
                "\nOption doesn't exist. Please type valid option number.\n",
                f"{navigation_menu()}",
            )
    # If user exceeded number of attempts, outputs message and exits the program.
    print("\nYou have exceeded the number of attempts. Program is shutting down.\n")
    sys.exit(0)


def get_films(mood: str):
    """
    Generating 5 films for the user in pretty format.
    :param: user current mood.
    :type: str
    :return: 5 films with description for each one.
    :rtype: str
    """
    # Using 'imdbfilmscrap.py' module to get films.
    films = films_scrap(mood)

    # Returns 5 scrapped films.
    print(f"\n🪄Here are five films to watch while you feeling {mood.lower()}: \n")
    for film in films:
        print(
            f'📽️Title: {film["Title"]} \n'
            f'⭐IMDB Rating: {film["IMDB Rating"]} \n'
            f'⌛Length: {film["Length"]} \n'
            f'🎭Genre: {film["Genre"]} \n'
            f'🎬By: {film["By"]} \n'
        )


if __name__ == "__main__":
    main()
