"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b):
    return a + b

    #def sub(a, b):
    #    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return b / a # raise ZeroDivisionError if a == 0

    #def log(a, b):
    #    try:
    #        math.log(a, b)
    #    except ValueError:
    #        print("ValueError")


def exp(a, b):
    return a**b

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

    #def multiply(a, b):
    #return a * b

def logarithm(a, b):
    try:
        math.log(b, a)
    except ValueError:
        print("Value Error")

d#ef exponent(a, b):
#   return a ** b



