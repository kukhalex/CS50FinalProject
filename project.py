from art import *
from tabulate import tabulate


def main():
    # Output programs logo/name in ascii format.
    intro = welcome()
    print(intro)
    print(type(intro))

    # Calling user to choose current type of the mood.
    mood = get_mood()
    print(mood)
    print(type(mood))


def welcome():
    """
    Converts program name into ascii art.
    :param: None
    :type: None
    :raise: None
    :return: Program name in ascii formatted art.
    :rtype: str
    """

    # Sets logo output name. Changeable - could be any other name.
    ascii_logo: str = "MOODIFY"

    # Sets font for logo name output. Changeable - look for 'art' library documentation.
    ascii_font: str = "starwards"

    # Creating an object with attributes.
    intro = text2art(ascii_logo, ascii_font)

    # Returns str to main function.
    return intro


def get_mood():
    """
    Calling user to make a choice of his current mood based on 3 options.
    :param: None
    :type: None
    :raise: None
    :return: User mood based on his choice.
    :rtype: str
    """

    # Sets tabulation raws filled with the options that user should choose.
    HEADERS: list = ["PRESS BUTTON:", "'1'", "'2'", "'3'"]
    TABLE: list = [["IF YOU:", "HAPPY", "CALM", "SAD"]]

    # Sets tabulation font. Changeable - look for 'tabulate' library documentation.
    TABLEFMT: str = "rounded_outline"
    return tabulate(TABLE, HEADERS, tablefmt="rounded_outline")


if __name__ == "__main__":
    main()
