"""
Fiona Wong

Maddelin Maddelin
"""
from game_creation import ascii_art


def character_has_leveled(character: dict, level_chart: dict) -> bool:
    """
    Return True if character has leveled up based on a dictionary of set level EXP, else False.

    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :param level_chart: a dictionary that contains the attainable levels and the EXP value required for each level
    :precondition: character must be a non-empty dictionary containing the necessary key-value pairs
    :return: True if character has leveled up based on a dictionary of set level EXP, else False

    >>> test_character = {'Name': 'Hunter', 'Partner Name': 'Killua', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
    ... 'HP': 100, 'EXP': 0}
    >>> test_level_chart = {1: 1, 2: 5, 3: 25, 4: 125, 5: 625}
    >>> character_has_leveled(test_character, test_level_chart)
    False
    >>> test_character = {'Name': 'Raon', 'Partner Name': 'Gon', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
    ... 'HP': 100, 'EXP': 125}
    >>> test_level_chart = {1: 1, 2: 5, 3: 25, 4: 125, 5: 625}
    >>> character_has_leveled(test_character, test_level_chart)
    True
    """
    result = False
    next_exp = level_chart[character['LEVEL'] + 1]
    if character['LEVEL'] and character['EXP'] >= next_exp:
        result = True
    return result


def display_level_chart() -> dict:
    """
    Create and print a dictionary that contains the attainable levels and the EXP value required for each level.

    :postcondition: creates and prints a dictionary that contains the attainable levels and the EXP value required for
                    each level.
    :return: a dictionary that contains the attainable levels and the EXP value required for each level

    >>> level_chart = display_level_chart()
    >>> level_chart
    {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 7: 700, 8: 800, 9: 900, 10: 1000}
    """
    return {level: exp for level, exp in enumerate(range(100, 1100, 100), start=1)}


def execute_glow_up_protocol(character: dict) -> None:
    """
    Display the corresponding ASCII art and increment the character level by 1 and HP by 100.

    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :precondition: character must be a non-empty dictionary containing the necessary key-value pairs
    :postcondition: displays the corresponding ASCII art and increments the character level by 1 and HP by 100

    >>> test_character = {'Name': 'Jess', 'Partner Name': 'Bess', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
    ... 'HP': 100, 'EXP': 25}
    >>> execute_glow_up_protocol(test_character)
    ========================================================================
    +.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.
       |||     |||||   ||   ||   ||||||  |||         ||    ||  |||||||
       |||     ||      ||   ||   ||      |||         ||    ||  ||     ||
       |||     |||||   ||   ||   |||||   |||         ||    ||  |||||||
       |||     ||       |   |    ||      |||         ||    ||  ||
       ||||||  |||||     |||     ||||||  |||||||      ||||||   ||
    +.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.
    ========================================================================
    <BLANKLINE>
        Current Status:
        LEVEL: 2
        HP: 300
        EXP: 25
    <BLANKLINE>

    >>> test_character = {'Name': 'Hiu', 'Partner Name': 'Paus', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 3,
    ... 'HP': 1, 'EXP': 125}
    >>> execute_glow_up_protocol(test_character)
    ========================================================================
    +.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.
       |||     |||||   ||   ||   ||||||  |||         ||    ||  |||||||
       |||     ||      ||   ||   ||      |||         ||    ||  ||     ||
       |||     |||||   ||   ||   |||||   |||         ||    ||  |||||||
       |||     ||       |   |    ||      |||         ||    ||  ||
       ||||||  |||||     |||     ||||||  |||||||      ||||||   ||
    +.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.
    ========================================================================
    <BLANKLINE>
        Current Status:
        LEVEL: 4
        HP: 201
        EXP: 125
    <BLANKLINE>
    """
    ascii_art.level_up_message()
    character['LEVEL'] += 1
    character['HP'] += 200
    print(f"\tCurrent Status:\n"
          f"\tLEVEL: {character['LEVEL']}\n"
          f"\tHP: {character['HP']}\n"
          f"\tEXP: {character['EXP']}\n")
