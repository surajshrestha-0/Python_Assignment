"""
Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
"""
import random


def multiplyUnknown(inpnut_number):
    return inpnut_number * random.randint(0, 1000)


print(multiplyUnknown(5))
