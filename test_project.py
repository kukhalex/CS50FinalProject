import pytest
from art import text2art
from tabulate import tabulate
from project import program_logo, mood_menu, navigation_menu
from project import get_mood, get_navigation, get_films


# Testing 'program_logo' function.
def test_program_logo():
    # Testing if function returns ASCII art of the program name with valid arguments.
    assert program_logo("Moodify", "varsity") == text2art("Moodify", "varsity")
    assert program_logo("anynewname", "epic") == text2art("anynewname", "epic")
    # Test if function raises ValueError with invalid arguments for example: name = 50, font = 250 both passed as
    # integers.
    with pytest.raises(ValueError):
        assert program_logo(50, 250)


# Testing 'mood_menu' function.
def test_mood_menu():
    # Testing if function returns valid formatted text.
    expected_output = f"\n💭Mood menu: \n" + tabulate(
        [
            ["TYPE:", "1️⃣", "IF YOU FEELING", "😁", "HAPPY"],
            ["TYPE:", "2️⃣", "IF YOU FEELING", "😌", "CALM"],
            ["TYPE:", "3️⃣", "IF YOU FEELING", "😔", "SAD"],
        ],
        [],
        "pretty",
    )
    assert mood_menu() == expected_output


# Testing 'navigation_menu' function.
def test_navigation_menu():
    expected_output = f"\n🧭Navigation menu: \n" + tabulate(
        [
            ["TYPE:", "1️⃣", "TO FIND MORE FILMS"],
            ["TYPE:", "2️⃣", "TO CHANGE MOOD"],
            ["TYPE:", "3️⃣", "TO EXIT THE PROGRAM"],
        ],
        [],
        "pretty",
    )
    assert navigation_menu() == expected_output


# Testing 'get_mood' function with monkeypatch.
def test_get_mood(monkeypatch):
    # Testing if function returns valid mood with valid input.
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert get_mood() == "HAPPY"
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert get_mood() == "CALM"
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert get_mood() == "SAD"

    # Testing case when user input invalid value five times straight.
    monkeypatch.setattr(
        "builtins.input", lambda _: "anything_besides_1_2_3_five_times_straight"
    )
    with pytest.raises(SystemExit) as e:
        for _ in range(5):
            get_mood()
    assert str(e.value) == "0"


# Testing 'get_navigation' function with monkeypatch.
def test_get_navigation(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert get_navigation() == "1"
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert get_navigation() == "2"
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert get_navigation() == "3"

    # Testing case when user input invalid value five times straight.
    monkeypatch.setattr(
        "builtins.input", lambda _: "anything_besides_1_2_3_five_times_straight"
    )
    with pytest.raises(SystemExit) as e:
        for _ in range(5):
            get_mood()
    assert str(e.value) == "0"


# Testing 'get_films' function with monkeypatch.
def test_get_films(monkeypatch):
    # Define mock function for films_scrap function.
    def mock_films_scrap():
        return [
            {
                "Title": "Test Title",
                "Year": "Test Year",
                "IMDB Rating": "Test Rating",
                "Genre": "Test Genre",
                "Length": "Test Length",
                "By": "Test By",
            }
        ]

    # Patch films_scrap function with mock_films_scrap function.
    monkeypatch.setattr("project.films_scrap", mock_films_scrap)
    # Define expected output.
    expected_output = (
        "\n🪄Here are five films to watch while you feeling happy:\n\n"
        "🎬Title: Test Title\n"
        "📅Year: Test Year\n"
        "🎭Genre: Test Genre\n"
        "⌛ Length: Test Length\n"
        "🌟IMDB Rating: Test Rating\n"
        "📝By: Test By\n"
        "--------------------------------------------------\n"
    )

    # Сalling get_films function with mock_films_scrap function.
    result = get_films("HAPPY")

    # Checking if result is equal to expected output.
    assert result == expected_output
