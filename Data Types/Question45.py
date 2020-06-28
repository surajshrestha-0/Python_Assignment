"""
Write a Python program to find the index of an item of a tuple.
"""


def indexOfTuple(input_tuple, item):
    return 'Index: {}'.format(input_tuple.index(item))


num_tuple = (1, 2, 3, 4, 5)
print(indexOfTuple(num_tuple, 2))
