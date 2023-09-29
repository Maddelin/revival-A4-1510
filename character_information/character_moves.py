"""
Fiona Wong

Maddelin Maddelin
"""


def get_user_choice() -> tuple:
    """
    Prompt the user to choose from an ordered list of directions they wish to travel to and return the chosen movement.

    :postcondition: print an ordered list of directions and prompts the user to enter the direction they want to go
    :return: a tuple that contains integers representing the x-coordinate and y-coordinate of the character move in the
             format of (x, y)
    """
    status = 0
    movement = {'W': (0, 1), 'S': (0, -1), 'A': (-1, 0), 'D': (1, 0)}
    step = 0
    while status != 1:
        user_input = input("To move, type:"
                           "\n\t 'W' : Up"
                           "\n\t 'S' : Down"
                           "\n\t 'A' : Left"
                           "\n\t 'D' : Right \n\n"
                           "Enter your response:  ")
        if user_input in movement.keys():
            print(
                f"\nYou have chosen to move {movement[user_input]} spaces.\n")
            status += 1
            step = movement[user_input]
        else:
            print(f"\nNot a valid option. Sorry please try again!\n")
    return step


def validate_move(board: dict, character: dict, direction: tuple) -> bool:
    """
    Validate that the character's location after moving is within the bounds of the board.

    :param board: a dictionary that contains rows * columns keys, where each key is a tuple that contains a set of
                  coordinates, and each value is a random short string description
    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :param direction: a tuple that contains a pair of integers representing the number of move(s) along the x-axis and
                      y-axis in that order
    :precondition: board must be a dictionary with valid key and value pairs
    :precondition: character must be a dictionary with valid key and value pairs
    :precondition: direction must be a tuple with valid move values
    :postcondition: validates that the character's location after moving is within the bounds of the board
    :return: True if the character's location after moving is within the bounds of the board, else False

    >>> test_board = {(0, 0): "This room is not a scary room!", (0, 1): "This room is a testing room."}
    >>> test_character = {'Name': 'Louie', 'Partner Name': 'Patricia', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
    ...                   'HP': 100, 'EXP': 0}
    >>> test_direction = (0, -1)
    >>> validate_move(test_board, test_character, test_direction)
    False
    >>> test_board = {(0, 0): "This room is not a scary room!", (0, 1): "This room is a testing room."}
    >>> test_character = {'Name': 'Marjorie', 'Partner Name': 'Rez', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
    ...                   'HP': 100, 'EXP': 0}
    >>> test_direction = (0, 1)
    >>> validate_move(test_board, test_character, test_direction)
    True
    """
    return (character["X-coordinate"] + direction[0], character["Y-coordinate"] + direction[1]) in board


def move_character(character: dict, direction: tuple) -> None:
    """
    Print the character's new location after moving the character based on the direction being passed.

    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :param direction: a tuple that contains a pair of integers representing the number of move(s) along the x-axis and
                      y-axis in that order
    :precondition: character must be a dictionary with valid key and value pairs
    :precondition: direction must be a tuple with valid move values
    :postcondition: prints the character's new location represented in x-coordinate and y-coordinate after each
                    coordinate value is added with the matching coordinate value in the tuple assigned to the direction

    >>> test_character = {'Name': 'Jagger', 'Partner Name': 'Erin', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
    ...                   'HP': 100, 'EXP': 0}
    >>> test_direction = (0, 2)
    >>> move_character(test_character, test_direction)
    You are now at (0, 2).
    >>> test_character = {'Name': 'Mick', 'Partner Name': 'Stephan', 'X-coordinate': 1, 'Y-coordinate': 0, 'LEVEL': 1,
    ...                   'HP': 100, 'EXP': 0}
    >>> test_direction = (1, 1)
    >>> move_character(test_character, test_direction)
    You are now at (2, 1).
    """
    character["X-coordinate"] += direction[0]
    character["Y-coordinate"] += direction[1]
    print(
        f"You are now at {(character['X-coordinate'], character['Y-coordinate'])}.")
