def add(a, b):
  return a + b

def multiply(a, b):
  return a * b

def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return numerator / denominator
