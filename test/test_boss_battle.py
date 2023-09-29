"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from challenge_modules import boss_battle


class TestBossBattle(TestCase):
    @patch('random.randint', side_effect=[1, 50, 1])
    @patch('builtins.input', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_boss_battle_attack_boss_not_defeated(self, the_game_printed_this, _, __):
        test_character = {'Name': 'May', 'Partner Name': 'Peter', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        test_boss = {'Name': 'King Slime-a-lot IX', 'HP': 500,
                     'Critical attack chance': test_character['LEVEL'],
                     'Miss attack chance': 10 - test_character['LEVEL']}
        boss_battle.boss_battle(test_boss, test_character)
        expected = "That was a critical attack!\n" \
                   "\nEnemy HP: 450\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 99\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 50, 1])
    @patch('builtins.input', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_boss_battle_attack_boss_not_defeated_return_False(self, _, __, ___):
        test_character = {'Name': 'Gill', 'Partner Name': 'Massey', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        test_boss = {'Name': 'King Slime-a-lot IX', 'HP': 500,
                     'Critical attack chance': test_character['LEVEL'],
                     'Miss attack chance': 10 - test_character['LEVEL']}
        expected = False
        actual = boss_battle.boss_battle(test_boss, test_character)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 50])
    @patch('builtins.input', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_boss_battle_attack_boss_defeated(self, the_game_printed_this, _, __):
        test_character = {'Name': 'May', 'Partner Name': 'Peter', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        test_boss = {'Name': 'King Slime-a-lot IX', 'HP': 50,
                     'Critical attack chance': test_character['LEVEL'],
                     'Miss attack chance': 10 - test_character['LEVEL']}
        boss_battle.boss_battle(test_boss, test_character)
        expected = "That was a critical attack!\n" \
                   "\nEnemy HP: 0\n\n" \
                   "You did it! You killed the enemy!\n" \
                   "\nYou gained 1000000 EXP!\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 50])
    @patch('builtins.input', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_boss_battle_attack_boss_defeated_return_True(self, _, __, ___):
        test_character = {'Name': 'Gill', 'Partner Name': 'Honey', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        test_boss = {'Name': 'King Slime-a-lot IX', 'HP': 50,
                     'Critical attack chance': test_character['LEVEL'],
                     'Miss attack chance': 10 - test_character['LEVEL']}
        expected = True
        actual = boss_battle.boss_battle(test_boss, test_character)
        self.assertEqual(expected, actual)
