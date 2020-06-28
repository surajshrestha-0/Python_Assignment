"""
Write a Python program to slice a tuple.
"""


def sliceTuple(input_tuple, start, end):
    return input_tuple[start: end]


# tuple and integer inputs only
print(sliceTuple((2, 4, 5, 6, 7), 0, 3))
