"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from io import StringIO
from unittest.mock import patch

from character_information import character_moves


class TestGetUserChoice(TestCase):
    @patch('builtins.input', return_value='W')
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_north(self, the_game_printed_this, _):
        character_moves.get_user_choice()
        expected = "\nYou have chosen to move (0, 1) spaces.\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='A')
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_west(self, the_game_printed_this, _):
        character_moves.get_user_choice()
        expected = "\nYou have chosen to move (-1, 0) spaces.\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='S')
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_south(self, the_game_printed_this, _):
        character_moves.get_user_choice()
        expected = "\nYou have chosen to move (0, -1) spaces.\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='D')
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_east(self, the_game_printed_this, _):
        character_moves.get_user_choice()
        expected = "\nYou have chosen to move (1, 0) spaces.\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['g', 'A'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_invalid_input_once_then_valid_input(self, the_game_printed_this, _):
        character_moves.get_user_choice()
        expected = "\nNot a valid option. Sorry please try again!\n\n" \
                   "\nYou have chosen to move (-1, 0) spaces.\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['m', 't', 'S'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_invalid_input_twice_then_valid_input(self, the_game_printed_this, _):
        character_moves.get_user_choice()
        expected = "\nNot a valid option. Sorry please try again!\n\n" \
                   "\nNot a valid option. Sorry please try again!\n\n" \
                   "\nYou have chosen to move (0, -1) spaces.\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['', 'A'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_invalid_empty_input_once_then_valid_input(self, the_game_printed_this, _):
        character_moves.get_user_choice()
        expected = "\nNot a valid option. Sorry please try again!\n\n" \
                   "\nYou have chosen to move (-1, 0) spaces.\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(actual, expected)
