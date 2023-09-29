"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase

from character_information import leveling


class TestCharacterHasLeveled(TestCase):
    def test_character_has_leveled_false(self):
        test_character = {'Name': 'Hunter', 'Partner Name': 'Killua', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
                          'HP': 100, 'EXP': 0}
        test_level_chart = {1: 1, 2: 5, 3: 25, 4: 125, 5: 625}
        expected = False
        actual = leveling.character_has_leveled(
            test_character, test_level_chart)
        self.assertEqual(expected, actual)

    def test_character_has_leveled_true(self):
        test_character = {'Name': 'Raon', 'Partner Name': 'Gon', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
                          'HP': 100, 'EXP': 125}
        test_level_chart = {1: 1, 2: 5, 3: 25, 4: 125, 5: 625}
        expected = True
        actual = leveling.character_has_leveled(
            test_character, test_level_chart)
        self.assertEqual(expected, actual)
