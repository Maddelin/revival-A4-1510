"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from challenge_modules import normal_challenges


class TestLevelBattle(TestCase):
    @patch('random.randint', side_effect=[1, 50, 1, 1, 50, 100])
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_battle_fight_win(self, the_game_printed_this, _, __):
        test_character = {'Name': 'Tithalia', 'Partner Name': 'Terabithia', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.level_battle(test_character)
        expected = "That was a critical attack!\n" \
                   "\nEnemy HP: 50\n\n" \
                   "Ouch! You have been attacked by the enemy.\n" \
                   "\nCharacter HP: 99\n\n" \
                   "That was a critical attack!\n" \
                   "\nEnemy HP: 0\n\n" \
                   "You did it! You killed the enemy!\n" \
                   "\nYou gained 100 EXP!\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 50, 1, 1, 50, 100])
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_battle_fight_win_gain_100_exp(self, _, __, ___):
        test_character = {'Name': 'Oak', 'Partner Name': 'Woods', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.level_battle(test_character)
        expected = {'Name': 'Oak', 'Partner Name': 'Woods', 'X-coordinate': 1, 'Y-coordinate': 1,
                    'LEVEL': 1, 'HP': 99, 'EXP': 100}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 50, 20, 1, 50, 100])
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_battle_fight_win_decrement_HP_by_20(self, _, __, ___):
        test_character = {'Name': 'Bessy', 'Partner Name': 'Betty', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.level_battle(test_character)
        expected = {'Name': 'Bessy', 'Partner Name': 'Betty', 'X-coordinate': 1, 'Y-coordinate': 1,
                    'LEVEL': 1, 'HP': 80, 'EXP': 100}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[10, 50, 10, 50])
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_battle_fight_lose(self, the_game_printed_this, _, __):
        test_character = {'Name': 'Bridget', 'Partner Name': 'Locke', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 5, 'HP': 100, 'EXP': 0}
        normal_challenges.level_battle(test_character)
        expected = "Your attack missed!\n" \
                   "\nEnemy HP: 100\n\n" \
                   "Ouch! You have been attacked by the enemy.\n" \
                   "\nCharacter HP: 50\n\n" \
                   "Your attack missed!\n" \
                   "\nEnemy HP: 100\n\n" \
                   "Ouch! You have been attacked by the enemy.\n" \
                   "\nCharacter HP: 0\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[10, 50, 10, 50])
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_battle_fight_lose_zero_HP(self, _, __, ___):
        test_character = {'Name': 'Jones', 'Partner Name': 'Jack', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 5, 'HP': 100, 'EXP': 0}
        normal_challenges.level_battle(test_character)
        expected = {'Name': 'Jones', 'Partner Name': 'Jack', 'X-coordinate': 1, 'Y-coordinate': 1,
                    'LEVEL': 5, 'HP': 0, 'EXP': 0}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value=2)
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_battle_run(self, the_game_printed_this, _):
        test_character = {'Name': 'Tithalia', 'Partner Name': 'Terabithia', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.level_battle(test_character)
        expected = "You have chosen to run away from the enemy.\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value=2)
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_battle_run_no_HP_lost_no_EXP_gained(self, _, __):
        test_character = {'Name': 'Tithalia', 'Partner Name': 'Terabithia', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.level_battle(test_character)
        expected = {'Name': 'Tithalia', 'Partner Name': 'Terabithia', 'X-coordinate': 1, 'Y-coordinate': 1,
                    'LEVEL': 1, 'HP': 100, 'EXP': 0}
        actual = test_character
        self.assertEqual(expected, actual)
