"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from io import StringIO
from unittest.mock import patch

from challenge_modules import normal_challenges


class TestGuessingGame(TestCase):
    @patch('builtins.input', return_value='3')
    @patch('random.randint', side_effect=[3, 80])
    @patch('sys.stdout', new_callable=StringIO)
    def test_guessing_game_correct_guess(self, the_game_printed_this, _, __):
        test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 0,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.guessing_game(test_character)
        expected = "\t[Slime]: You're right! Thank you for playing with me.\n\n" \
                   "\tYou gained 80 EXP!\n\n" \
                   "\tCurrent HP: 100\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=StringIO)
    def test_guessing_game_wrong_guess(self, the_game_printed_this, _, __):
        test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 0,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.guessing_game(test_character)
        expected = "\t[Slime]: Wrong! 3 is the correct number!\n" \
                   "\n\tSlime shoots slime mucus to the Player. Player loses 10 HP.\n\n" \
                   "\tCurrent HP: 90\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3')
    @patch('random.randint', side_effect=[3, 50])
    @patch('sys.stdout', new_callable=StringIO)
    def test_guessing_game_correct_guess_increment_EXP_by_50(self, _, __, ___):
        test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 0,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.guessing_game(test_character)
        expected = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 0,
                    'LEVEL': 1, 'HP': 100, 'EXP': 50}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3')
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=StringIO)
    def test_guessing_game_correct_guess_same_hp_no_EXP_gained(self, _, __, ___):
        test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 0,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.guessing_game(test_character)
        expected = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 0,
                    'LEVEL': 1, 'HP': 100, 'EXP': 3}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3')
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=StringIO)
    def test_guessing_game_wrong_guess_decrement_hp(self, _, __, ___):
        test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 0,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.guessing_game(test_character)
        expected = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 0,
                    'LEVEL': 1, 'HP': 90, 'EXP': 0}
        actual = test_character
        self.assertEqual(expected, actual)
