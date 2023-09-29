"""
Fiona Wong

Maddelin Maddelin
"""
from game_creation import story, ascii_art
from challenge_modules import boss_battle, normal_challenges
from board import make_board, describe_current_location
from character_information import make_character, is_alive, character_moves, leveling


def game():
    """
    Initiate game.
    """
    rows = 10
    columns = 10
    board = make_board.make_board(rows, columns)
    level_chart = leveling.display_level_chart()
    story.opening()
    character = make_character.make_character()
    story.game_introduction(character)

    achieved_goal = False
    while is_alive.is_alive(character) and not achieved_goal:
        direction = character_moves.get_user_choice()
        valid_move = character_moves.validate_move(board, character, direction)
        if valid_move:
            character_moves.move_character(character, direction)
            describe_current_location.describe_current_location(
                board, character)
            there_is_a_challenge = normal_challenges.check_for_challenges(
                board, character)
            if there_is_a_challenge:
                normal_challenges.execute_challenge_protocol(character)
                if leveling.character_has_leveled(character, level_chart):
                    leveling.execute_glow_up_protocol(character)
            achieved_goal = boss_battle.check_if_goal_attained(
                board, character)
        else:
            print(f"Not a valid move. You cannot go in this direction")
    if achieved_goal:
        story.display_win_message()
        ascii_art.cat_sleep()
    else:
        story.display_death_message()


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
