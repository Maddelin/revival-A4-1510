"""
Fiona Wong

Maddelin Maddelin
"""


def is_alive(character: dict) -> bool:
    """
    Verify that the character's HP is not zero, which means character is still alive.

    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :precondition: character must be a non-empty dictionary containing the necessary key-value pairs
    :postcondition: checks if character HP is still greater than 0
    :return: True if character HP is greater than 0, else false

    >>> test_character = {'Name': 'Misha', 'Partner Name': 'Panda', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
    ...                   'HP': 100, 'EXP': 0}
    >>> is_alive(test_character)
    True
    >>> test_character = {'Name': 'Uno', 'Partner Name': 'Dos', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
    ...                   'HP': 0, 'EXP': 0}
    >>> is_alive(test_character)
    False
    """
    return character['HP'] > 0
