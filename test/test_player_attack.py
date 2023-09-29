"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from challenge_modules import player_attack


class TestPlayerAttack(TestCase):
    @patch('random.randint', return_value=9)
    @patch('sys.stdout', new_callable=StringIO)
    def test_player_attack_miss_attack(self, the_game_printed_this, _):
        test_enemy = {'HP': 100, 'Critical attack chance': 1,
                      'Miss attack chance': 10 - 1}
        player_attack.player_attack(test_enemy)
        expected = "Your attack missed!\n" \
                   "\nEnemy HP: 100\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 80])
    @patch('sys.stdout', new_callable=StringIO)
    def test_player_attack_critical_attack(self, the_game_printed_this, _):
        test_enemy = {'HP': 100, 'Critical attack chance': 1,
                      'Miss attack chance': 10 - 1}
        player_attack.player_attack(test_enemy)
        expected = "That was a critical attack!\n" \
                   "\nEnemy HP: 20\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[5, 49])
    @patch('sys.stdout', new_callable=StringIO)
    def test_player_attack_normal_attack(self, the_game_printed_this, _):
        test_enemy = {'HP': 100, 'Critical attack chance': 1,
                      'Miss attack chance': 10 - 1}
        player_attack.player_attack(test_enemy)
        expected = "The attack was successful!\n" \
                   "\nEnemy HP: 51\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)
