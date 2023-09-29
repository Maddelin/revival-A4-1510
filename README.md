# 1510-Assignment-04

Every program needs a README.md

This is written in markdown. Read about markdown here: [markdowncheatsheet](https://www.markdownguide.org/cheat-sheet/)

## Your names:
Fiona Wong <br>
Maddelin Maddelin
## Your GitHub account ID:
fwwong <br>
Maddelin

## Any important comments you'd like to make about your work:
The objective of this game, Revival, is to defeat the king slime in the game board.
There is a level up system that can assist your adventure. <br>
For better experience turn on capitals lock.


### Decomposition:
We broke down our code into smaller files in different folder in order to keep track of which functions we are using.
Each function has less than 15 lines of code beside the game function, ASCII art functions, and story narrations.

### Pattern matching:
We recognize a pattern going on for the battle functions in our game. The normal battle system is the original function
we use for combat. We apply the pattern matching concept in order to implement the boss fight battle system. 

### Abstraction:
In our functions, we generally focus on one or two aspect of the dictionary. Take character dictionary for example we 
usually use character dictionary to refer to its keys such as "LEVEL" or "HP". We take that key and modify its value 
by using arithmetic operators from modules leveling.py in execute_glow_up_protocol function . Other information 
of the character dictionary is ignored until it is called.

### Automation and algorithms:
We assume that there is an infinite loop going over the game loop. Until the player either kills the boss monster 
or get kill by monsters in the game. Within, the game loop the player will have to move around to search for monsters 
to kill in order to level up and get stronger. Once the player has encounter a monster they will either play a guessing
game where they have to guess a number from 1 to 5 inclusively in order to escape. The battle system is also another 
algorithm we use. This algorithm relies on the random module to the loss of HP and the amount of damage dealt.


<br>

| Requirements                                                       |        Module        | Line  |    Function Name    |
|:-------------------------------------------------------------------|:--------------------:|:-----:|:-------------------:|
| (a) Code compiles and executes without issues.                     |       main.py        |  14   |        game         |
| (b) Efficiently manage 10 x 10 game board.                         |    make_board.py     |  11   |     make_board      |
| (c) Gameplay ends appropriately.                                   |       main.py        | 41-45 |        game         |
| (d) Error-free character movement within game boundaries.          |  character_move.py   |  37   |    validate_move    |
| (e) Diverse challenges, achievable difficulty, balanced scaling.   | normal_challenges.py |  85   |    guessing_game    |
|                                                                    |    boss_battle.py    |  60   |     boss_battle     |
| (f) Minimal mutability.                                            |    make_board.py     |  11   |     make_board      | 
| (g) Reduced scope of mutable variables.                            |  make_character.py   |  10   |   make_character    |
| (h) Code employs list/dict comprehensions for concise readability. |    make_board.py     |  33   |     make_board      |
| (i) If-statements are used for selection.                          |   player_attack.py   |  21   |    player_attack    | 
| (j) Repetitive for/while loops. Flat is better than nested.        |    make_board.py     |  33   |     make_board      | 
| (k) Membership operator used correctly.                            |  character_move.py   |  66   |    validate_move    |
| (l) Range function used efficiently for improved code performance. |     leveling.py      |  53   | display_level_chart |
| (m) Thoughtful use of itertools functions observed.                |     leveling.py      |  53   | display_level_chart |
| (n) Correct usage of the random module observed.                   | normal_challenges.py |  72   |    level_battle     |
| (o) Output uses f-strings, str-string, or %-string                 |     ascii_art.py     |  39   |     slime_boss      |



