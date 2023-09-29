"""
Fiona Wong

Maddelin Maddelin
"""


def opening() -> None:
    """
    Print welcome message to the player.

    :postcondition: display welcome message to the player
    """
    print(f"\nYou woke up all sweaty, thinking it was all some sort of dream.\n"
          f"You got out of bed, brush your teeth, drank some coffee, and ran out the door knowing that you will be late"
          f" for work again.\nYou step outside the door and onto the road. You have a sparkle of a moment and realized "
          f"that you forgot something very important in your house. \nIt was your phone!\n"
          f"You stop in the middle of the road and turn back....   \n\n"
          f"A truck appear in front of you and you don't know what to do.\nYou froze for a quick second....\n"
          f"And you realize that you are not in your sweet hometown anymore.\n")
    print(f"==========================================================================\n"
          f"/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n\n"
          f"   $$$$$$    $$$$$$   $$  $$   $$   $$  $$     $$     $$          ^      \n"
          f"   $$    $   $$       $$  $$   $$   $$  $$   $$  $$   $$         | |     \n"
          f"   $$$$$$    $$$$$    $$  $$   $$   $$  $$   $$$$$$   $$         |||    \n"
          f"   $$  $$    $$       $$  $$   $$   $$  $$   $$  $$   $$        _|||_     \n"
          f"   $$   $$   $$$$$$     $$     $$     $$     $$  $$   $$$$$$$$    v      \n\n"
          f"/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n"
          f"==========================================================================\n")
    print(f"[Mayor Queenie]: Welcome to Sparktown, Traveler. \n"
          f"[Humble Shoemaker Tom]: 50% off on your next purchase, come visit Solemate in The Alley!\n"
          f"[Gossip Baker Sarah]: So, did you know that my husband walked out to the forest and left without saying a "
          f"word to me?\n"
          f"                      So unacceptable! Girls you need to know how to choose your men. Otherwise "
          f"the forest gods will get upset.\n"
          f"[Gossip Storekeeper Annie]: I heard last night there was a rumor that a king slime has appeared.\n"
          f"                            They take on different elements depending on the region they live in.\n"
          f"[Gossip Priest Judy]: The father was once approached by it and he ran away! It was a very huge slime.\n"
          f"                      Father called it 'King Slime-a-lot IX' because of the ooze it left behind.\n"
          f"[Gossip Baker Sarah]: Oh dear, my husband told me that slime has some sort of whip that it forms.\n"
          f"[Gossip Storekeeper Annie]: King Slimy can turn his jelly into a tentacle.\n"
          f"                            I heard an author in town made a fan fictional story out of it..\n")


def game_introduction(character):
    """
    Print a short dialogue between the player's character and their partner.

    :param character: a dictionary containing character information and stats
    :precondition: character must be a dictionary that contains the key-value pairs for character's name and their
                   partner's name
    :postcondition: prints a short dialogue between player's chosen names for the character and the character's partner
    """
    print('\n"Caw!"\n'
          '\nYou jolted up, disconcerted.'
          '\nConfused.'
          '\nYou seem to have woken up in an unfamiliar place and...in an unfamiliar body?'
          '\nThis body is not yours!\n'
          f'\n"{character["Name"]}!" a sweet voice yelled.'
          '\n"Are you okay?"'
          '\nYou are even more confused. That is not your name.'
          '\nAnd you have never met this person before!\n'
          '\n"Who...are you?" you asked, unsure.'
          f'\nThey look hurt. "I am {character["Partner Name"]}, remember?"'
          f'\n"We have been in this together for 3 moons! Remember...?"\n')


def boss_encounter(monster: dict) -> None:
    """
    Print boss encounter message to the player.

    :postcondition: display boss encounter message to the player
    """
    print(f"You spotted a giant slime from afar. What's this?! It has a crown on top.\n"
          f"This can't be the rumor slime that was left in the world for thousand and thousand of years!\n"
          f"============================================================================================\n"
          f"\t\t\t\t\t\t\t\t\t{monster['Name']}\n\t\t\t\t\t\t\t\t\t\tHP: {monster['HP']}\n"
          f"============================================================================================\n")


def display_death_message() -> None:
    """
    Print game over message to the player.

    :postcondition: display game over message to the player
    """
    print(f"\n=============================================================================================\n"
          f"[SYSTEM]: YOU HAVE DIED. THE KING SLIME HAS DEVOUR YOUR CORPSE AND SPIT OUT YOUR REMAINS.\n\n"
          f"      $$$$$      $$$$    $$        $$  $$$$$$      $$$$   $$   $$  $$$$$$  $$$$$   \n"
          f"    $$$   $$   $$    $$  $$$      $$$  $$         $    $  $$   $$  $$      $$   $$ \n"
          f"    $$         $$    $$  $$ $    $ $$  $$$$$      $    $  $$   $$  $$$$$   $$    $ \n"
          f"    $$   $$$$  $$$$$$$$  $$  $  $  $$  $$         $    $  $$   $$  $$      $$ $$$   \n"
          f"    $$    $$   $$    $$  $$   $$   $$  $$         $    $  $$   $$  $$      $$   $$   \n"
          f"      $$$$     $$    $$  $$        $$  $$$$$$      $$$$      $$    $$$$$$  $$    $$    \n"
          f"\n============================================================================================\n\n")


def display_win_message() -> None:
    """
    Print a win message to the player.

    :precondition: display win message to the player
    """
    print(f"==================================================================\n"
          f"CONGRATULATION! YOU HAVE DEFEATED KING SLIME-A-LOT IX! \n"
          f"PLEASE MAKE YOUR WAY BACK HOME \n"
          f"==================================================================\n\n"
          f"You cheer for joy that you defeat the King Slime. A magical portal appears in front of you\n"
          f"You see pitch darkness and open your eyes for a quick second.... \n "
          f"You felt a squishy touch from your cat??\n")
