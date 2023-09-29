"""
Fiona Wong

Maddelin Maddelin
"""
from challenge_modules import player_attack

import random


def check_for_challenges(board: dict, character: dict) -> bool:
    """
    Verify if character has encountered an enemy.

    :param board: a dictionary that contains rows * columns keys, where each key is a tuple that contains a set of
                  coordinates, and each value is a random short string description
    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :precondition: board must be a non-empty dictionary containing the necessary key-value pairs
    :precondition: character must be a non-empty dictionary containing the necessary key-value pairs
    :postcondition: check if character has encountered an opponent in a 25% chance
    :return: True if the randomly generated number is the same as the mock integer, else False
    """
    user_coord = (character['X-coordinate'], character['Y-coordinate'])
    system_roll = random.randint(1, 4)
    if system_roll == 1:
        appearance = True
        print(f"\n=======================================================================\n"
              f"{board[user_coord]} slime has appeared!\nThe slime wants to play with you."
              f"\n=======================================================================\n")
    else:
        appearance = False
    return appearance


def execute_challenge_protocol(character: dict) -> None:
    """
    Determine what type of challenge the player will be facing.

    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :precondition: character must be a non-empty dictionary containing the necessary key-value pairs
    :postcondition: calls the function of the challenge decided randomly based on a 50% chance
    """
    if random.randint(1, 2) == 1:
        guessing_game(character)
    else:
        level_battle(character)


def level_battle(character: dict) -> None:
    """
    Initiate a user-interactive battle of which difficulty is based on the character's level.

    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :precondition: character must be a non-empty dictionary containing the necessary key-value pairs
    :postcondition: accepts user input in determining whether to escape or fight the battle, then decrements the
                    character's HP value and/or increments the character's EXP value accordingly
    """
    enemy = {'HP': 100, 'Critical attack chance':
             character['LEVEL'], 'Miss attack chance': 10 - character['LEVEL']}
    while enemy['HP'] > 0 and character['HP'] > 0:
        player_choice = input(f'Would you like to fight or run?'
                              f"\n1. Attack the enemy, of course!"
                              f"\n2. Run\n"
                              f"\n[Traveler {character['Name']}]:\t")
        if player_choice != '1':
            print("You have chosen to run away from the enemy.")
            break
        player_attack.player_attack(enemy)
        if enemy['HP'] > 0:
            character['HP'] -= random.randint(character['LEVEL'],
                                              10 * character['LEVEL'])
            print(f"Ouch! You have been attacked by the enemy.\n"
                  f"\nCharacter HP: {character['HP']}\n")
    if enemy['HP'] <= 0:
        exp_gained = random.randint(50, 150)
        print("You did it! You killed the enemy!\n"
              f"\nYou gained {exp_gained} EXP!\n")
        character['EXP'] += exp_gained


def guessing_game(character: dict) -> None:
    """
    Prompt the player to guess a randomly generated integer between one and ten inclusive.

    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :precondition: character must be a non-empty dictionary containing the necessary key-value pairs
    :postcondition: prompts the player to guess a randomly generated integer between one and ten inclusive, then
                    decrements the character's HP by 10 if the guess is wrong
    """
    secret_number = str(random.randint(1, 5))
    guess = input(f"\t[Slime]: Pick a number between 1 and 5 inclusive: \n"
                  f"\t[Traveler {character['Name']}]: ")
    if guess == secret_number:
        print("\t[Slime]: You're right! Thank you for playing with me.\n")
        exp_gained = random.randint(50, 150)
        print(f"\tYou gained {exp_gained} EXP!\n")
        character['EXP'] += exp_gained

    else:
        print(f"\t[Slime]: Wrong! {secret_number} is the correct number!\n"
              f"\n\tSlime shoots slime mucus to the Player. Player loses 10 HP.\n")
        character["HP"] -= 10
    print(f"\tCurrent HP: {character['HP']}\n")
