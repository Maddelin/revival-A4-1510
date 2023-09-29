"""
Fiona Wong

Maddelin Maddelin
"""
import random


def player_attack(enemy: dict) -> None:
    """
    Determine and inflict the type of attack and its associated damage points based on a set probability on the enemy.

    :param enemy: a dictionary that contains the following keys (each with possibly modified values):
                    'HP', 'Critical attack chance', and 'Miss attack chance'
    :precondition: enemy must be a non-empty dictionary containing the necessary key-value pairs
    :postcondition: decrements the enemy's HP by the damage points of the determined type of attack
    """
    attack_chance = random.randint(1, 10)
    if attack_chance >= enemy['Miss attack chance']:
        print("Your attack missed!")
        print(f"\nEnemy HP: {enemy['HP']}\n")
    elif attack_chance <= enemy['Critical attack chance']:
        enemy['HP'] -= random.randint(50, 80)
        print("That was a critical attack!")
        print(f"\nEnemy HP: {enemy['HP']}\n")
    else:
        enemy['HP'] -= random.randint(20, 49)
        print("The attack was successful!")
        print(f"\nEnemy HP: {enemy['HP']}\n")
