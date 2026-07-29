"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("num must be greater than 0")

def hypotenuse(a, b):
    return math.hypot(a,b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")

def logarithm(a, b):
    try:
        math.log(b, a)
    except ValueError:
        print("Value Error")

def exponent(a, b):
    return a ** b



