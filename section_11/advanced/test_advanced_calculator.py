import pytest
from advanced_calculator import power, is_prime

def test_power():
    """Test for the power function"""
    assert power(2, 3) == 8
    assert power(3, 3) == 27

@pytest.mark.parametrize(
   ("n, expected"),
   [
      pytest.param(0, False, id="zero"),
      pytest.param(1, False),
      pytest.param(2, True),
      pytest.param(3, True),
      pytest.param(4, False),
      pytest.param(5, True),
      pytest.param(6, False, id="six"),
      pytest.param(7, True),
   ]
)
def test_is_prime(n, expected):
    assert is_prime(n) == expected



#def is_prime(n: int) -> bool:
#    """Return True if n is a prime number, False otherwise"""
#    if n < 2:
#        return False
#    for i in range(2, int(n ** 0.5) + 1):
#        if n % i == 0:
#            return False
#    return True
