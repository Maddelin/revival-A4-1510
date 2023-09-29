"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from challenge_modules import normal_challenges


class TestCheckForChallenges(TestCase):
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_for_challenges_print_if_True(self, the_game_printed_this, _):
        test_board = {(0, 0): "Spooky", (0, 1): "Scary", (1, 1): "Skeleton"}
        test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        normal_challenges.check_for_challenges(test_board, test_character)
        expected = "\n=======================================================================\n" \
                   "Scary slime has appeared!\nThe slime wants to play with you." \
                   "\n=======================================================================\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_for_challenges_return_True(self, _, __):
        test_board = {(0, 0): "Spooky", (0, 1): "Scary", (1, 1): "Wednesday"}
        test_character = {'Name': 'Sushi', 'Partner Name': 'Sashimi', 'X-coordinate': 0, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        expected = True
        actual = normal_challenges.check_for_challenges(
            test_board, test_character)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_check_for_challenges_return_False(self, _):
        test_board = {(0, 0): "Funky", (0, 1): "Scary", (1, 1): "Wednesday"}
        test_character = {'Name': 'Sushi', 'Partner Name': 'Sashimi', 'X-coordinate': 0, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        expected = False
        actual = normal_challenges.check_for_challenges(
            test_board, test_character)
        self.assertEqual(expected, actual)
