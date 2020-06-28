"""
Write a Python program to sort a list of tuples using Lambda.
"""


def sortTuple(input_tuple):
    return sorted(input_tuple, key=lambda x: x[1])


tup = [('ram', 30), ('hari', 50), ('shyam', 20), ('gaurav', 15)]
print(sortTuple(tup))
