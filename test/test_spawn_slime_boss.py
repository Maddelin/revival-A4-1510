"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from challenge_modules import boss_battle


class TestSpawnSlimeBoss(TestCase):
    @patch('random.randint', side_effect=[1, 80, 3, 1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1,
                                          1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1,
                                          1, 80, 1, 1, 80, 1, 1, 80, 1])
    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_spawn_slime_boss_win_return_True(self, _, __, ___):
        test_character = {'Name': 'Oak', 'Partner Name': 'Woods', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        expected = True
        actual = boss_battle.spawn_slime_boss(test_character)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[10, 50, 10, 50])
    @patch('builtins.input', side_effect=['1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_spawn_slime_boss_lose_return_False(self, _, __, ___):
        test_character = {'Name': 'Oak', 'Partner Name': 'Woods', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        expected = False
        actual = boss_battle.spawn_slime_boss(test_character)
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 80, 2, 1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1,
                                          1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1,
                                          1, 80, 1, 1, 80, 1, 1, 80, 1])
    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_spawn_slime_boss_win_gain_1000000_exp(self, _, __, ___):
        test_character = {'Name': 'Oak', 'Partner Name': 'Woods', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        boss_battle.spawn_slime_boss(test_character)
        expected = {'Name': 'Oak', 'Partner Name': 'Woods', 'X-coordinate': 1, 'Y-coordinate': 1,
                    'LEVEL': 1, 'HP': 93, 'EXP': 1000000}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 80, 5, 1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1,
                                          1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1,
                                          1, 80, 1, 1, 80, 1, 1, 80, 1])
    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_spawn_slime_boss_win_decrement_HP_by_16(self, _, __, ___):
        test_character = {'Name': 'Bessy', 'Partner Name': 'Betty', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        boss_battle.spawn_slime_boss(test_character)
        expected = {'Name': 'Bessy', 'Partner Name': 'Betty', 'X-coordinate': 1, 'Y-coordinate': 1,
                    'LEVEL': 1, 'HP': 90, 'EXP': 1000000}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[10, 50, 10, 50])
    @patch('builtins.input', side_effect=['1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_spawn_slime_boss_lose_zero_HP(self, _, __, ___):
        test_character = {'Name': 'Jones', 'Partner Name': 'Jack', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 5, 'HP': 100, 'EXP': 0}
        boss_battle.spawn_slime_boss(test_character)
        expected = {'Name': 'Jones', 'Partner Name': 'Jack', 'X-coordinate': 1, 'Y-coordinate': 1,
                    'LEVEL': 5, 'HP': 0, 'EXP': 0}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1,
                                          1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1, 1, 80, 1,
                                          1, 80, 1, 1, 80, 2, 1, 80, 1])
    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                          '1', '1', '1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_spawn_slime_boss_win(self, the_game_printed_this, _, __):
        test_character = {'Name': 'Jackson', 'Partner Name': 'Jill', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        boss_battle.spawn_slime_boss(test_character)
        expected = "\t                           +++ \n" \
                   "\t                           \#/ \n" \
                   "\t            %%   %   %%    //   \n" \
                   "\t             \* /*\ */    //    \n" \
                   "\t     ^        \* * */  +.##3\     \n" \
                   "\t   -< >-       \* *.+######33\    ))\n" \
                   "\t     V       .++###########33\   ))\n" \
                   "\t          .++###########33333333. \n" \
                   "\t       .++++##############333333333. \n" \
                   "\t    :::+++|  |#######|  |#####333333.  )) ))\n" \
                   "\t   ::+++++|  |#######|  |########33333.   ))\n" \
                   "\t  ::::////|__|#######|__|//////####33333. \n" \
                   "\t::::////################/////######333333. \n" \
                   "\t``:::################################333333  )))\n" \
                   "\t''''/\########/\######/\########/\######333.   ))) ))\n" \
                   "\t\..../  \######/  \####/  \######/  \#####3     ))  ))\n" \
                   "\t \@@/    \@@@@/    \@@/    \@@@@/    \@@@/ ???     )) )) \n" \
                   "\t  ::?     :::?     ?::      ::??      :::  ??????? ??? ?? ?? ? ??? ?\n" \
                   "\t  ??  ?? ? ?? ?????? ????   ?? ? ??    ???  ? ?? ? ? ????? ?? ???? ????\n\n" \
                   "You spotted a giant slime from afar. What's this?! It has a crown on top.\n" \
                   "This can't be the rumor slime that was left in the world for thousand and thousand of years!\n" \
                   "============================================================================================\n" \
                   "\t\t\t\t\t\t\t\t\tKing Slime-a-lot IX\n\t\t\t\t\t\t\t\t\t\tHP: 500\n" \
                   "============================================================================================\n\n" \
                   "That was a critical attack!\n" \
                   "\nEnemy HP: 420\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 99\n\n" \
                   "That was a critical attack!\n" \
                   "\nEnemy HP: 340\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 98\n\n" \
                   "That was a critical attack!\n" \
                   "\nEnemy HP: 260\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 97\n\n" \
                   "That was a critical attack!\n" \
                   "\nEnemy HP: 180\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 96\n\n" \
                   "That was a critical attack!\n" \
                   "\nEnemy HP: 100\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 95\n\n" \
                   "That was a critical attack!\n" \
                   "\nEnemy HP: 20\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 94\n\n" \
                   "That was a critical attack!\n" \
                   "\nEnemy HP: -60\n\n" \
                   "You did it! You killed the enemy!\n" \
                   "\nYou gained 1000000 EXP!\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[10, 50, 10, 50])
    @patch('builtins.input', side_effect=['1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_spawn_slime_boss_fight_lose(self, the_game_printed_this, _, __):
        test_character = {'Name': 'Jackson', 'Partner Name': 'Jill', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        boss_battle.spawn_slime_boss(test_character)
        expected = "\t                           +++ \n" \
                   "\t                           \#/ \n" \
                   "\t            %%   %   %%    //   \n" \
                   "\t             \* /*\ */    //    \n" \
                   "\t     ^        \* * */  +.##3\     \n" \
                   "\t   -< >-       \* *.+######33\    ))\n" \
                   "\t     V       .++###########33\   ))\n" \
                   "\t          .++###########33333333. \n" \
                   "\t       .++++##############333333333. \n" \
                   "\t    :::+++|  |#######|  |#####333333.  )) ))\n" \
                   "\t   ::+++++|  |#######|  |########33333.   ))\n" \
                   "\t  ::::////|__|#######|__|//////####33333. \n" \
                   "\t::::////################/////######333333. \n" \
                   "\t``:::################################333333  )))\n" \
                   "\t''''/\########/\######/\########/\######333.   ))) ))\n" \
                   "\t\..../  \######/  \####/  \######/  \#####3     ))  ))\n" \
                   "\t \@@/    \@@@@/    \@@/    \@@@@/    \@@@/ ???     )) )) \n" \
                   "\t  ::?     :::?     ?::      ::??      :::  ??????? ??? ?? ?? ? ??? ?\n" \
                   "\t  ??  ?? ? ?? ?????? ????   ?? ? ??    ???  ? ?? ? ? ????? ?? ???? ????\n\n" \
                   "You spotted a giant slime from afar. What's this?! It has a crown on top.\n" \
                   "This can't be the rumor slime that was left in the world for thousand and thousand of years!\n" \
                   "============================================================================================\n" \
                   "\t\t\t\t\t\t\t\t\tKing Slime-a-lot IX\n\t\t\t\t\t\t\t\t\t\tHP: 500\n" \
                   "============================================================================================\n\n" \
                   "Your attack missed!\n" \
                   "\nEnemy HP: 500\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 50\n\n" \
                   "Your attack missed!\n" \
                   "\nEnemy HP: 500\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 0\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[10, 50, 10, 50])
    @patch('builtins.input', side_effect=['2', '1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_spawn_slime_boss_run_attempt_once_then_lose(self, the_game_printed_this, _, __):
        test_character = {'Name': 'Jackson', 'Partner Name': 'Jill', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        boss_battle.spawn_slime_boss(test_character)
        expected = "\t                           +++ \n" \
                   "\t                           \#/ \n" \
                   "\t            %%   %   %%    //   \n" \
                   "\t             \* /*\ */    //    \n" \
                   "\t     ^        \* * */  +.##3\     \n" \
                   "\t   -< >-       \* *.+######33\    ))\n" \
                   "\t     V       .++###########33\   ))\n" \
                   "\t          .++###########33333333. \n" \
                   "\t       .++++##############333333333. \n" \
                   "\t    :::+++|  |#######|  |#####333333.  )) ))\n" \
                   "\t   ::+++++|  |#######|  |########33333.   ))\n" \
                   "\t  ::::////|__|#######|__|//////####33333. \n" \
                   "\t::::////################/////######333333. \n" \
                   "\t``:::################################333333  )))\n" \
                   "\t''''/\########/\######/\########/\######333.   ))) ))\n" \
                   "\t\..../  \######/  \####/  \######/  \#####3     ))  ))\n" \
                   "\t \@@/    \@@@@/    \@@/    \@@@@/    \@@@/ ???     )) )) \n" \
                   "\t  ::?     :::?     ?::      ::??      :::  ??????? ??? ?? ?? ? ??? ?\n" \
                   "\t  ??  ?? ? ?? ?????? ????   ?? ? ??    ???  ? ?? ? ? ????? ?? ???? ????\n\n" \
                   "You spotted a giant slime from afar. What's this?! It has a crown on top.\n" \
                   "This can't be the rumor slime that was left in the world for thousand and thousand of years!\n" \
                   "============================================================================================\n" \
                   "\t\t\t\t\t\t\t\t\tKing Slime-a-lot IX\n\t\t\t\t\t\t\t\t\t\tHP: 500\n" \
                   "============================================================================================\n\n" \
                   "You cannot run away!\n" \
                   "Your attack missed!\n" \
                   "\nEnemy HP: 500\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 50\n\n" \
                   "Your attack missed!\n" \
                   "\nEnemy HP: 500\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 0\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[10, 50, 10, 50])
    @patch('builtins.input', side_effect=['2', 'not 1', '1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_spawn_slime_boss_run_attempt_twice_then_lose(self, the_game_printed_this, _, __):
        test_character = {'Name': 'Jackson', 'Partner Name': 'Jill', 'X-coordinate': 1, 'Y-coordinate': 1,
                          'LEVEL': 1, 'HP': 100, 'EXP': 0}
        boss_battle.spawn_slime_boss(test_character)
        expected = "\t                           +++ \n" \
                   "\t                           \#/ \n" \
                   "\t            %%   %   %%    //   \n" \
                   "\t             \* /*\ */    //    \n" \
                   "\t     ^        \* * */  +.##3\     \n" \
                   "\t   -< >-       \* *.+######33\    ))\n" \
                   "\t     V       .++###########33\   ))\n" \
                   "\t          .++###########33333333. \n" \
                   "\t       .++++##############333333333. \n" \
                   "\t    :::+++|  |#######|  |#####333333.  )) ))\n" \
                   "\t   ::+++++|  |#######|  |########33333.   ))\n" \
                   "\t  ::::////|__|#######|__|//////####33333. \n" \
                   "\t::::////################/////######333333. \n" \
                   "\t``:::################################333333  )))\n" \
                   "\t''''/\########/\######/\########/\######333.   ))) ))\n" \
                   "\t\..../  \######/  \####/  \######/  \#####3     ))  ))\n" \
                   "\t \@@/    \@@@@/    \@@/    \@@@@/    \@@@/ ???     )) )) \n" \
                   "\t  ::?     :::?     ?::      ::??      :::  ??????? ??? ?? ?? ? ??? ?\n" \
                   "\t  ??  ?? ? ?? ?????? ????   ?? ? ??    ???  ? ?? ? ? ????? ?? ???? ????\n\n" \
                   "You spotted a giant slime from afar. What's this?! It has a crown on top.\n" \
                   "This can't be the rumor slime that was left in the world for thousand and thousand of years!\n" \
                   "============================================================================================\n" \
                   "\t\t\t\t\t\t\t\t\tKing Slime-a-lot IX\n\t\t\t\t\t\t\t\t\t\tHP: 500\n" \
                   "============================================================================================\n\n" \
                   "You cannot run away!\n" \
                   "You cannot run away!\n" \
                   "Your attack missed!\n" \
                   "\nEnemy HP: 500\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 50\n\n" \
                   "Your attack missed!\n" \
                   "\nEnemy HP: 500\n\n" \
                   "\t                        _+++++.     \n" \
                   "\t                      //        `.    \n" \
                   "\t      *++++++*       //   00/``\ /   \n" \
                   "\t    //         \    //   000'   v      \n" \
                   "\t   //   000     \__//   000'                         \n" \
                   "\t  //  0000  \        0000'       ||  ||  ||  ||||||  \n" \
                   "\t // 00000    ++++``00000`        ||==||  ||    ||         \n" \
                   "\t// 00000      ```00000`          ||  ||  ||    ||        \n\n" \
                   "Ouch! You have been attacked by King Slime-a-lot IX's slimy tentacle whip." \
                   "\nCharacter HP: 0\n\n"
        actual = the_game_printed_this.getvalue()
        self.assertEqual(expected, actual)
