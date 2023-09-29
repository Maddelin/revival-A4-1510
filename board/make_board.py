"""
Fiona Wong

Maddelin Maddelin
"""
import random


def make_board(rows: int, columns: int) -> dict:
    """
    Create a dictionary that visualizes a grid board of size rows by columns, with each position in the board containing
    a random description of the position.

    :param rows: a positive non-zero integer representing the number of rows on the board
    :param columns: a positive non-zero integer representing the number of columns on the board
    :precondition: rows must be a positive integer that is equal to or greater than 10
    :precondition: columns must be a positive integer that is equal to or greater than 10
    :precondition: rows and columns must be the same integer value to ensure that the board as a game space is square
    :postcondition: creates a dictionary that contains rows * columns keys, where each key is a tuple that contains a
                    set of coordinates, and each value is a random short string description
    :return: a dictionary that contains rows * columns keys, where each key is a tuple that contains a set of
             coordinates, and each value is a random short string description
    :raises TypeError: if rows or columns is not an integer
    :raises ValueError: if rows or columns is not equal to or greater than 10
    :raises ValueError: if rows and columns are not the same value
    """
    if rows < 2 or columns < 2 or rows != columns:
        raise ValueError(
            "Board must have rows and columns be equal to or greater than 10")
    else:
        description = ["Forest", "Lava", "Swamp",
                       "Sky", "Sea", "Earth", "Mountain"]
        grid = {(x_coord, y_coord): random.choice(description)
                for x_coord in range(rows) for y_coord in range(columns)}
        return grid
