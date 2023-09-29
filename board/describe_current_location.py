"""
Fiona Wong

Maddelin Maddelin
"""


def describe_current_location(board: dict, character: dict) -> None:
    """
    Print out the description of the character's current location.

    :param board: a dictionary that contains rows * columns keys, where each key is a tuple that contains a set of
                  coordinates, and each value is a random short string description
    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :precondition: must be a non-empty dictionary containing key value pairs
    :postcondition: prints out string description of the character's current location
    :raises ValueError: if character's coordinate is outside the bound of the board

    >>> test_board = {(0, 0): "empty", (0, 1): "white"}
    >>> test_character = {'Name': 'Jeremiah', 'Partner Name': 'Nick', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
    ...                   'HP': 100, 'EXP': 0}
    >>> describe_current_location(test_board, test_character)
    You are currently at (0, 0). You have entered empty area.
    The home of the empty slimes.
    <BLANKLINE>
    >>> test_board = {(0, 0): "puppy", (0, 1): "duck"}
    >>> test_character = {'Name': 'Lisa', 'Partner Name': 'Sam', 'X-coordinate': 0, 'Y-coordinate': 1, 'LEVEL': 1,
    ...                   'HP': 100, 'EXP': 0}
    >>> describe_current_location(test_board, test_character)
    You are currently at (0, 1). You have entered duck area.
    The home of the duck slimes.
    <BLANKLINE>
    """
    user_coord = (character['X-coordinate'], character['Y-coordinate'])
    if user_coord not in board:
        raise ValueError(
            "Character coordinates must be in the board's coordinate")
    print(f"You have entered {board[user_coord]} area.\n"
          f"The home of the {board[user_coord]} slimes.\n")
