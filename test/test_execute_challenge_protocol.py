"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from unittest.mock import patch, Mock

from challenge_modules import normal_challenges


class TestExecuteChallengeProtocol(TestCase):
    @patch('random.randint', return_value=1)
    def test_execute_challenge_protocol_call_guessing_game(self, _):
        test_character = {'Name': 'Tatiana', 'Partner Name': 'Tabitha', 'X-coordinate': 0, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        mock_function_called = Mock()
        normal_challenges.guessing_game = mock_function_called
        normal_challenges.execute_challenge_protocol(test_character)
        mock_function_called.assert_called_once()

    @patch('random.randint', return_value=2)
    def test_execute_challenge_protocol_call_level_battle(self, _):
        test_character = {'Name': 'Pedro', 'Partner Name': 'Matthew', 'X-coordinate': 0, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        mock_function_called = Mock()
        normal_challenges.level_battle = mock_function_called
        normal_challenges.execute_challenge_protocol(test_character)
        mock_function_called.assert_called_once()
