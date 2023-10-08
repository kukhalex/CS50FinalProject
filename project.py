import sys
from art import *
from tabulate import tabulate


def main():
    # Output programs logo/name in ascii format.
    print(welcome())
    # Calling user to choose current type of the mood.
    mood: str = get_mood()
    # Looking for the activities based on users mood.

    if mood == "1":
        ...  # Should implement function to look for 5 films for happy mood.
    elif mood == "2":
        ...  # Should implement function to look for 5 films for calm mood.
    else:
        ...  # Should implement function to look for 5 films for sad mood.


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


def get_name():
    ...


def get_mood():
    """
    Calling user to make a choice of his current mood based on 3 options.
    :param: None
    :type: None
    :raise: ...
    :return: User mood based on his choice.
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
        user_choice = input("\nEnter the number followed by 'Enter' button: ").strip()

        if not user_choice or user_choice not in ["1", "2", "3"]:
            print("\nPlease enter valid number:\n", choices)
        else:
            return user_choice


if __name__ == "__main__":
    main()
