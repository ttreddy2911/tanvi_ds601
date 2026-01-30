msg="Testing Calculator App"
print (msg)

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 4) == 6
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(4, 2) == 2
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 6) == 12
    assert multiply(-1, 5) == -5 
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(8, 2) == 4
    assert divide(10, 5) == 2
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    # Use pytest.raises to check if the correct exception is raised
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)