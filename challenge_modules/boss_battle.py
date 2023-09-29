"""
Fiona Wong

Maddelin Maddelin
"""
from game_creation import ascii_art, story
from challenge_modules import player_attack

import random


def check_if_goal_attained(board: dict, character: dict) -> bool:
    """
    Verify if character has defeated the boss in the last most bottom right position of the board.

    :param board: a dictionary that contains rows * columns keys, where each key is a tuple that contains a set of
                  coordinates, and each value is a random short string description
    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :precondition: board must be a non-empty dictionary containing the necessary key-value pairs
    :precondition: character must be a non-empty dictionary containing the necessary key-value pairs
    :postcondition: checks if the character has defeated the boss in the last most bottom right position of the board
    :return: True if the character has defeated the boss in the last most bottom right position of the board, else False
    """
    if (character["X-coordinate"], character["Y-coordinate"]) == max(board):
        status = spawn_slime_boss(character)
    else:
        status = False
    return status


def spawn_slime_boss(character: dict) -> bool:
    """
    Evaluate the slime boss status on a fixed position of the game board.

    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :precondition: character must be a non-empty dictionary containing the necessary key-value pairs
    :precondition: check if slime boss is alive
    :return: a boolean value of True or False
    """
    slime = {'Name': 'King Slime-a-lot IX', 'HP': 500,
             'Critical attack chance': character['LEVEL'],
             'Miss attack chance': 10 - character['LEVEL']}
    dead = False
    ascii_art.slime_boss()
    story.boss_encounter(slime)
    user_option = input("\n 1. Fight \n\n")
    while user_option != '1':
        print(f"You cannot run away!")
        user_option = input("\n 1. Fight \n\n")
    while slime['HP'] > 0 and character['HP'] > 0:
        dead = boss_battle(slime, character)
    return dead


def boss_battle(boss: dict, character: dict) -> bool:
    """
    Engage battle with a boss monster.

    :param boss: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'HP', 'Critical attack chance' and 'Miss attack chance'
    :param character: a dictionary that contains the following keys (each with possibly modified values):
                      'Name', 'Partner Name', 'X-coordinate', 'Y-coordinate', 'LEVEL', 'HP', and 'EXP'
    :precondition: boss must be a non-empty dictionary containing the necessary key-value pairs
    :precondition: character must be a non-empty dictionary containing the necessary key-value pairs
    :postcondition: battle against a boss monster
    :return: a boolean value of True or False
    """
    defeat = False
    input("\n 1. Attack \n\n")
    player_attack.player_attack(boss)
    if boss['HP'] > 0:
        character['HP'] -= random.randint(character['LEVEL'],
                                          10 * character['LEVEL'])
        ascii_art.slime_attack_tentacle_whip()
        print(f"Ouch! You have been attacked by {boss['Name']}'s slimy tentacle whip."
              f"\nCharacter HP: {character['HP']}\n")
    if boss['HP'] <= 0:
        exp_gained = 1000000
        character['EXP'] += exp_gained
        defeat = True
        print("You did it! You killed the enemy!\n"
              f"\nYou gained {exp_gained} EXP!\n")
    return defeat
