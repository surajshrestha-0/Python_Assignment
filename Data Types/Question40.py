"""
Write a Python program to add an item in a tuple.
"""


def addItemToTuple(input_tuple, *item):
    input_tuple = input_tuple + (*item,)
    return input_tuple


even_tuple = (2, 4, 6, 8, 14, 16)
print(addItemToTuple(even_tuple, 10, 12))
