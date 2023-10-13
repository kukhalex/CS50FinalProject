from art import text2art
from tabulate import tabulate
from project import program_logo, mood_menu, get_mood_option


# Testing 'program_logo' function.
def test_program_logo():
    assert program_logo() == text2art("MOODIFY", "varsity")


# Testing 'mood_menu' function.
def test_mood_menu():
    expected_output = "\n💭Mood menu:\n" + tabulate(
        [
            ["TYPE:", "1️⃣", "IF YOU FEELING", "😁", "HAPPY"],
            ["TYPE:", "2️⃣", "IF YOU FEELING", "😌", "CALM"],
            ["TYPE:", "3️⃣", "IF YOU FEELING", "😔", "SAD"],
        ],
        [],
        "pretty",
    )
    assert mood_menu() == expected_output


# Testing 'get_mood_option' function with emulation of the input.
def test_get_mood(monkeypatch):
    # 'Mock' test for the input '1'
    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = get_mood_option()
    assert result == "HAPPY"
    # 'Mock' test for the input '2'
    monkeypatch.setattr("builtins.input", lambda _: "2")
    result = get_mood_option()
    assert result == "CALM"
    # 'Mock' test for the input '3'
    monkeypatch.setattr("builtins.input", lambda _: "3")
    result = get_mood_option()
    assert result == "SAD"


# Testing 'navigation_menu" function
def test_navigation_menu():
    ...

