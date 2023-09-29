"""
Fiona Wong

Maddelin Maddelin
"""
from unittest import TestCase
from unittest.mock import patch

from board import make_board


class TestMakeBoard(TestCase):
    @patch('random.choice', side_effect=["\nThe room is cold and dark.", "\nThe room is cold and dark.",
                                         "\nThe room is cold and dark.", "\nThe room is cold and dark."])
    def test_make_board_two_by_two(self, _):
        expected = {(0, 0): "\nThe room is cold and dark.", (0, 1): "\nThe room is cold and dark.",
                    (1, 0): "\nThe room is cold and dark.", (1, 1): "\nThe room is cold and dark."}
        actual = make_board.make_board(2, 2)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["\nThe room is cold and dark.", "\nThe room is cold and dark.",
                                         "\nThe room is cold and dark.", "\nThe room is cold and dark.",
                                         "\nThe room is cold and dark.", "\nThe room is cold and dark.",
                                         "\nThe room is cold and dark.", "\nThe room is cold and dark.",
                                         "\nThe room is cold and dark."])
    def test_make_board_three_by_three(self, _):
        expected = {(0, 0): "\nThe room is cold and dark.", (0, 1): "\nThe room is cold and dark.",
                    (0, 2): "\nThe room is cold and dark.", (1, 0): "\nThe room is cold and dark.",
                    (1, 1): "\nThe room is cold and dark.", (1, 2): "\nThe room is cold and dark.",
                    (2, 0): "\nThe room is cold and dark.", (2, 1): "\nThe room is cold and dark.",
                    (2, 2): "\nThe room is cold and dark."}
        actual = make_board.make_board(3, 3)
        self.assertEqual(expected, actual)

    def test_make_board_raise_value_error_if_all_not_equal_to_or_greater_than_two(self):
        with self.assertRaises(ValueError):
            test_rows = 1
            test_columns = 1
            make_board.make_board(test_rows, test_columns)

    def test_make_board_raise_value_error_if_one_not_equal_to_or_greater_than_two(self):
        with self.assertRaises(ValueError):
            test_rows = 1
            test_columns = 2
            make_board.make_board(test_rows, test_columns)

    def test_make_board_raise_value_error_if_not_equal_to_each_other(self):
        with self.assertRaises(ValueError):
            test_rows = 3
            test_columns = 2
            make_board.make_board(test_rows, test_columns)
