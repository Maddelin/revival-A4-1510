"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from challenge_modules import boss_battle


class TestCheckIfGoalAttained(TestCase):
    @patch('random.randint', side_effect=[1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1,
                                          1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1,
                                          1, 80, 1, 1, 80, 1, 1, 80, 1])
    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_if_goal_attained_return_True_if_last_location_but_win_battle(self, _, __, ___):
        test_board = {(0, 0): "Mischievous", (0, 1): "Yummy", (1, 1): "GUI"}
        test_character = {'Name': 'Tithalia', 'Partner Name': 'Terabithia', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        expected = True
        actual = boss_battle.check_if_goal_attained(test_board, test_character)
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                                          10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_if_goal_attained_return_False_if_last_location_but_lose_battle(self, _, __, ___):
        test_board = {(0, 0): "Boss", (0, 1): "Defeated", (1, 1): "GUI"}
        test_character = {'Name': 'Tithalia', 'Partner Name': 'Terabithia', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        expected = False
        actual = boss_battle.check_if_goal_attained(test_board, test_character)
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_return_False_if_middle_location_not_last_location(self):
        test_board = {(0, 0): "No", (0, 1): "Boss", (1, 1): "GUI"}
        test_character = {'Name': 'Timothy', 'Partner Name': 'Trish', 'X-coordinate': 0, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        expected = False
        actual = boss_battle.check_if_goal_attained(test_board, test_character)
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_return_False_if_first_location_not_last_location(self):
        test_board = {(0, 0): "Slime", (0, 1): "Not", (1, 1): "GUI"}
        test_character = {'Name': 'Timothy', 'Partner Name': 'Trish', 'X-coordinate': 0, 'Y-coordinate': 0,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        expected = False
        actual = boss_battle.check_if_goal_attained(test_board, test_character)
        self.assertEqual(actual, expected)
