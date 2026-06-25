"""
This module contains the tools to calculate the amount of grain on the King's Chessboard

The chessboard has 64 squares, starting with 1 grain and doubling each following square
"""


def square(number):
    """
    Finds the amount of grain on a chosen tile on the chessboard
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return pow(2, number - 1)

def total():
    """
    Returns the total grain on the entire chessboard
    """
    return sum(square(num + 1) for num in range(64))