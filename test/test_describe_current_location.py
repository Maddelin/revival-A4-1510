"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from io import StringIO
from unittest.mock import patch

from board import describe_current_location


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_describe_current_location_first_location(self, the_game_printed_this):
        test_board = {(0, 0): "Earth", (0, 1): "Air", (1, 1): "Water"}
        test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 0,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        describe_current_location.describe_current_location(
            test_board, test_character)
        expected = "You have entered Earth area." \
                   "\nThe home of the Earth slimes.\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_describe_current_location_middle_location(self, the_game_printed_this):
        test_board = {(0, 0): "Fire", (0, 1): "Air", (1, 1): "Water"}
        test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        describe_current_location.describe_current_location(
            test_board, test_character)
        expected = "You have entered Air area." \
                   "\nThe home of the Air slimes.\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_describe_current_location_last_location(self, the_game_printed_this):
        test_board = {(0, 0): "Earth", (0, 1): "Fire", (1, 1): "Water"}
        test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        describe_current_location.describe_current_location(
            test_board, test_character)
        expected = "You have entered Water area." \
                   "\nThe home of the Water slimes.\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    def test_describe_current_all_location_coordinate_not_within_bounds(self):
        with self.assertRaises(ValueError):
            test_board = {(0, 0): "Earth", (0, 1): "Fire", (1, 1): "Water"}
            test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': -1, 'Y-coordinate': 2,
                              'LEVEL': 1, 'HP': 100, 'EXP': 0}
            describe_current_location.describe_current_location(
                test_board, test_character)

    def test_describe_current_location_x_coordinate_not_within_bounds(self):
        with self.assertRaises(ValueError):
            test_board = {(0, 0): "Earth", (0, 1): "Fire", (1, 1): "Water"}
            test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 3, 'Y-coordinate': 0,
                              'LEVEL': 1, 'HP': 100, 'EXP': 0}
            describe_current_location.describe_current_location(
                test_board, test_character)

    def test_describe_current_location_y_coordinate_not_within_bounds(self):
        with self.assertRaises(ValueError):
            test_board = {(0, 0): "Earth", (0, 1): "Fire", (1, 1): "Water"}
            test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 1, 'Y-coordinate': 2,
                              'LEVEL': 1, 'HP': 100, 'EXP': 0}
            describe_current_location.describe_current_location(
                test_board, test_character)
