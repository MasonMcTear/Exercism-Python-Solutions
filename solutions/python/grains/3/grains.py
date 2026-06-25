def square(number):
    """
    Finds the amount of grain on a chosen tile on the chessboard

    The chessboard starts at one and doubles every following square
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return pow(2, number - 1)

def total():
    """
    Returns the total grain on the entire chessboard
    """
    return sum(square(num + 1) for num in range(64))