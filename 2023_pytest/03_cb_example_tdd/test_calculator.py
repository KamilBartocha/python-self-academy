from calculator import calculator
import pytest

def test_add_two_numbers():
    number1 = 2
    number2 = 6
    operator = "+"
    assert calculator(number1, number2, operator) == 8

def test_sub_two_numbers():
    number1 = 6
    number2 = 2
    operator = "-"
    assert calculator(number1, number2, operator) == 4
