"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase

from character_information import is_alive


class TestIsAlive(TestCase):
    def test_is_alive_return_True_if_starting_hp(self):
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "HP": 5}
        expected = True
        actual = is_alive.is_alive(test_character)
        self.assertEqual(expected, actual)

    def test_is_alive_return_True_if_lower_than_starting_hp_but_not_zero(self):
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "HP": 3}
        expected = True
        actual = is_alive.is_alive(test_character)
        self.assertEqual(expected, actual)

    def test_is_alive_return_False_if_zero(self):
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "HP": 0}
        expected = False
        actual = is_alive.is_alive(test_character)
        self.assertEqual(expected, actual)
