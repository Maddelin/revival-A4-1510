"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from unittest.mock import patch

from character_information import make_character


class TestMakeCharacter(TestCase):
    @patch('builtins.input', side_effect=["Chris", "Reese"])
    def test_make_character_all_valid(self, _):
        expected = {'Name': "Chris", 'Partner Name': "Reese", 'X-coordinate': 0, 'Y-coordinate': 0,
                    'LEVEL': 1, 'HP': 100, 'EXP': 0}
        actual = make_character.make_character()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Chris", "Reese"])
    def test_make_character_valid_number_of_elements(self, _):
        expected = 7
        actual = len(make_character.make_character())
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Chris", "Reese"])
    def test_make_character_valid_x_coordinate_value(self, _):
        expected = 0
        actual = make_character.make_character()['X-coordinate']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Chris", "Reese"])
    def test_make_character_valid_y_coordinate_value(self, _):
        expected = 0
        actual = make_character.make_character()['Y-coordinate']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Chris", "Reese"])
    def test_make_character_valid_current_hp_value(self, _):
        expected = 100
        actual = make_character.make_character()['HP']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Chris", "Reese"])
    def test_make_character_all_invalid(self, _):
        expected = {'X-coordinate': 6, 'Y-coordinate': 4, 'HP': 3}
        actual = make_character.make_character()
        self.assertNotEqual(expected, actual)

    @patch('builtins.input', side_effect=["Chris", "Reese"])
    def test_make_character_invalid_number_of_elements(self, _):
        expected = 5
        actual = len(make_character.make_character())
        self.assertNotEqual(expected, actual)

    @patch('builtins.input', side_effect=["Chris", "Reese"])
    def test_make_character_invalid_x_coordinate_value(self, _):
        expected = 9
        actual = make_character.make_character()['X-coordinate']
        self.assertNotEqual(expected, actual)

    @patch('builtins.input', side_effect=["Chris", "Reese"])
    def test_make_character_invalid_y_coordinate_value(self, _):
        expected = 7
        actual = make_character.make_character()['Y-coordinate']
        self.assertNotEqual(expected, actual)

    @patch('builtins.input', side_effect=["Chris", "Reese"])
    def test_make_character_invalid_current_hp_value(self, _):
        expected = 2
        actual = make_character.make_character()['HP']
        self.assertNotEqual(expected, actual)
