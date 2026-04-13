"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/oliverdescartes/lab11-PB-NA/blob/main/test_calculator.py
# Partner 1: Priyanshou bhattacharjee
# Partner 2: Not responsive

# First example
import math

# Basic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Logarithm
def logarithm(x, base):
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    if base <= 0 or base == 1:
        raise ValueError("Invalid base for logarithm")
    return math.log(x, base)


# Hypotenuse (Pythagoras)
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


# Square root
def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)