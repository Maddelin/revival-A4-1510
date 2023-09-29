"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from io import StringIO
from unittest.mock import patch

from character_information import leveling


class TestExecuteGlowUpProtocol(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_execute_glow_up_protocol_print_result(self, the_game_printed_this):
        test_character = {'Name': 'Jess', 'Partner Name': 'Bess', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 1,
                          'HP': 100, 'EXP': 200}
        leveling.execute_glow_up_protocol(test_character)
        expected = "========================================================================\n" \
                   "+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.\n" \
                   "   |||     |||||   ||   ||   ||||||  |||         ||    ||  |||||||\n" \
                   "   |||     ||      ||   ||   ||      |||         ||    ||  ||     ||\n" \
                   "   |||     |||||   ||   ||   |||||   |||         ||    ||  |||||||\n" \
                   "   |||     ||       |   |    ||      |||         ||    ||  ||\n" \
                   "   ||||||  |||||     |||     ||||||  |||||||      ||||||   ||\n" \
                   "+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.\n" \
                   "========================================================================\n\n" \
                   "\tCurrent Status:\n" \
                   "\tLEVEL: 2\n" \
                   "\tHP: 300\n" \
                   "\tEXP: 200\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_execute_glow_up_protocol_increment_level_and_HP(self, _):
        test_character = {'Name': 'Lawliet', 'Partner Name': 'Light', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 2,
                          'HP': 100, 'EXP': 300}
        leveling.execute_glow_up_protocol(test_character)
        expected = {'Name': 'Lawliet', 'Partner Name': 'Light', 'X-coordinate': 0, 'Y-coordinate': 0, 'LEVEL': 3,
                    'HP': 200, 'EXP': 300}
        actual = test_character
        self.assertEqual(expected, actual)
