"""
Write a Python program to remove an item from a tuple.
"""


def removeitemFromTuple(input_tuple, item):
    list_tuple = list(input_tuple)
    list_tuple.remove(item)
    return tuple(list_tuple)


number_tuple = ('one', 'two', 'three', 'four')
# input arguments are a tuple and an item from the tuple to be removed.
print(removeitemFromTuple(number_tuple, 'one'))
