"""
Fiona Wong

Maddelin Maddelin
"""


def make_character() -> dict:
    """
    Create a new character dictionary that represents the name of the character and their default character stats.

    :postcondition: creates a dictionary with keys of X-coordinate, Y-coordinate, LEVEL, HP, and EXP paired with
                    default positive integer values and names paired with user input string value
    :return: a dictionary that contains 7 key-value pairs representing default character stats
    """
    player_name = input("Please enter your name:   ")
    partner_name = input("What is your partner's name:   ")
    user = {'Name': player_name, 'Partner Name': partner_name, 'X-coordinate': 0, 'Y-coordinate': 0,
            'LEVEL': 1, 'HP': 100, 'EXP': 0}
    return user
