"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from io import StringIO
from unittest.mock import patch

from character_information import character_moves


class TestMoveCharacter(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_character_show_updated_location_move_by_x_axis(self, the_game_printed_this):
        test_character = {"X-coordinate": 1,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (1, 0)
        character_moves.move_character(test_character, test_direction)
        expected = "You are now at (2, 0).\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_move_character_show_updated_location_move_by_y_axis(self, the_game_printed_this):
        test_character = {"X-coordinate": 1,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (0, 2)
        character_moves.move_character(test_character, test_direction)
        expected = "You are now at (1, 2).\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_move_character_show_updated_location_move_by_both_axes(self, the_game_printed_this):
        test_character = {"X-coordinate": 1,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (1, 3)
        character_moves.move_character(test_character, test_direction)
        expected = "You are now at (2, 3).\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_move_character_update_character_location_move_by_x_axes(self, _):
        test_character = {"X-coordinate": 1,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (1, 0)
        character_moves.move_character(test_character, test_direction)
        expected = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_move_character_update_character_location_move_by_y_axes(self, _):
        test_character = {"X-coordinate": 1,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (0, 3)
        character_moves.move_character(test_character, test_direction)
        expected = {"X-coordinate": 1, "Y-coordinate": 3, "Current HP": 5}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_move_character_update_character_location_move_by_both_axes(self, _):
        test_character = {"X-coordinate": 1,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (3, 2)
        character_moves.move_character(test_character, test_direction)
        expected = {"X-coordinate": 4, "Y-coordinate": 2, "Current HP": 5}
        actual = test_character
        self.assertEqual(expected, actual)
