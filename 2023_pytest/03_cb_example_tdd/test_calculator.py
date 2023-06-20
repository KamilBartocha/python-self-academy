from calculator import calculator
import pytest

def test_add_two_numbers():
    num1 = 2
    num2 = 6
    operator = "+"
    assert calculator(num1, num2, operator) == 5