import pytest
from art import text2art
from tabulate import tabulate
from project import program_logo, mood_menu, get_mood, navigation_menu


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
    expected_output = f"💭Mood menu:\n" + tabulate(
        [
            ["TYPE:", "1️⃣", "IF YOU FEELING", "😁", "HAPPY"],
            ["TYPE:", "2️⃣", "IF YOU FEELING", "😌", "CALM"],
            ["TYPE:", "3️⃣", "IF YOU FEELING", "😔", "SAD"],
        ],
        [],
        "pretty",
    )
    assert mood_menu() == expected_output


def test_navigation_menu():
    expected_output = f"🧭Navigation menu:\n" + tabulate(
        [
            ["TYPE:", "1️⃣", "TO FIND MORE FILMS FOR YOUR ACTUAL MOOD"],
            ["TYPE:", "2️⃣", "TO CHANGE MOOD"],
            ["TYPE:", "3️⃣", "TO EXIT THE PROGRAM"],
        ],
        [],
        "pretty",
    )
    assert navigation_menu() == expected_output


def test_get_mood(monkeypatch):
    # Testing if function returns valid mood with valid input.
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert get_mood() == 'HAPPY'
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert get_mood() == 'CALM'
    monkeypatch.setattr('builtins.input', lambda _: '3')
    assert get_mood() == 'SAD'

    # Testing case when user input invalid value five times straight.
    monkeypatch.setattr('builtins.input', lambda _: 'anything_besides_1_2_3_five_times_straight')
    with pytest.raises(SystemExit) as e:
        for _ in range(5):
            get_mood()
    assert str(e.value) == "0"



