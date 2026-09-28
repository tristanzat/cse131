from sudoku import *

def test_convert_to_coordinate():
    CONVERT_ERROR = (-1, -1)
    # Test cases:
    # Input | Expected Out
    # A4 | (3, 0)
    assert convert_to_coordinate("A4") == (3, 0)
    # 4A | (3, 0)
    assert convert_to_coordinate("4A") == (3, 0)
    # b7 | (6, 1)
    assert convert_to_coordinate("b7") == (6, 1)
    # 2e | (1, 4)
    assert convert_to_coordinate("2e") == (1, 4)
    # A1 | (0, 0)
    assert convert_to_coordinate("A1") == (0, 0)
    # I9 | (8, 8)
    assert convert_to_coordinate("I9") == (8, 8)
    # A0 | (-1, -1)
    assert convert_to_coordinate("A0") == CONVERT_ERROR
    # banana | (-1, -1)
    assert convert_to_coordinate("banana") == CONVERT_ERROR
    # B3qwerty | (-1, -1)
    assert convert_to_coordinate("B3qwerty") == CONVERT_ERROR