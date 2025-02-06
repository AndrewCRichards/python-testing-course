import pytest

# Import the add function so the test can use it
from calculator import add, multiply, divide

def test_add():
   # Check that it adds two positive integers
   assert add(1, 2) == 3

   # Check that it adds zero
   assert add(5, 0) == 5

   # Check that it adds two negative integers
   assert add(-1, -2) == -3

def test_multiply():
   assert multiply(5, 0) == 0
   assert multiply(5, 1) == 5
   assert multiply(5, 2) == 10
   assert multiply(0, 5) == 0
   assert multiply(1, 5) == 5
   assert multiply(2, 5) == 10

def test_divide():
    with pytest.raises(ZeroDivisionError) as e:
        divide(5,0)
    assert str(e.value) == "Cannot divide by zero!"
