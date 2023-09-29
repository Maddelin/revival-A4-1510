"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase

from character_information import character_moves


class TestValidateMove(TestCase):
    def test_validate_move_all_invalid_coordinate_move(self):
        test_board = {(0, 0): "This room is not a scary room!", (0, 1): "This room is a testing room.",
                      (1, 0): "This is the last room.", (1, 1): "This is the last room."}
        test_character = {"X-coordinate": 0,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (-1, -1)
        expected = False
        actual = character_moves.validate_move(
            test_board, test_character, test_direction)
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_x_coordinate_move(self):
        test_board = {(0, 0): "This room is not a scary room!", (0, 1): "This room is a testing room.",
                      (1, 0): "This is the last room.", (1, 1): "This is the last room."}
        test_character = {"X-coordinate": 0,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (-1, 0)
        expected = False
        actual = character_moves.validate_move(
            test_board, test_character, test_direction)
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_y_coordinate_move(self):
        test_board = {(0, 0): "This room is not a scary room!", (0, 1): "This room is a testing room.",
                      (1, 0): "This is the last room.", (1, 1): "This is the last room."}
        test_character = {"X-coordinate": 0,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (0, 2)
        expected = False
        actual = character_moves.validate_move(
            test_board, test_character, test_direction)
        self.assertEqual(expected, actual)

    def test_validate_move_all_valid_coordinate_move(self):
        test_board = {(0, 0): "This room is not a scary room!", (0, 1): "This room is a testing room.",
                      (1, 1): "This is the last room."}
        test_character = {"X-coordinate": 0,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (1, 1)
        expected = True
        actual = character_moves.validate_move(
            test_board, test_character, test_direction)
        self.assertEqual(expected, actual)

    def test_validate_move_valid_x_coordinate_move(self):
        test_board = {(0, 0): "This room is not a scary room!", (0, 1): "This room is a testing room.",
                      (1, 0): "This is the last room.", (1, 1): "This is the last room."}
        test_character = {"X-coordinate": 0,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (1, 0)
        expected = True
        actual = character_moves.validate_move(
            test_board, test_character, test_direction)
        self.assertEqual(expected, actual)

    def test_validate_move_valid_y_coordinate_move(self):
        test_board = {(0, 0): "This room is not a scary room!", (0, 1): "This room is a testing room.",
                      (1, 0): "This is the last room.", (1, 1): "This is the last room."}
        test_character = {"X-coordinate": 0,
                          "Y-coordinate": 0, "Current HP": 5}
        test_direction = (0, 1)
        expected = True
        actual = character_moves.validate_move(
            test_board, test_character, test_direction)
        self.assertEqual(expected, actual)
