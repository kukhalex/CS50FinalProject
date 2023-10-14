import pytest
from art import text2art
from tabulate import tabulate
from project import program_logo, mood_menu, get_mood


# Testing 'program_logo' function.
def test_program_logo():
    # Testing if function returns ASCII art of the program name with valid arguments.
    assert program_logo("Moodify", "varsity") == text2art("Moodify", "varsity")
    assert program_logo("anynewname", "epic") == text2art("anynewname", "epic")
    # Test if function raises ValueError with invalid arguments for example: name = 50, font = 250 both integers.
    with pytest.raises(ValueError):
        assert program_logo(50, 250)


# Testing 'mood_menu' function.
def test_mood_menu():
    # Testing if function returns valid formatted text.
    expected_output = f"\n💭Mood menu:\n" + tabulate(
        [
            ["TYPE:", "1️⃣", "IF YOU FEELING", "😁", "HAPPY"],
            ["TYPE:", "2️⃣", "IF YOU FEELING", "😌", "CALM"],
            ["TYPE:", "3️⃣", "IF YOU FEELING", "😔", "SAD"],
        ],
        [],
        "pretty",
    )
    assert mood_menu() == expected_output


def test_get_mood():
    ...
