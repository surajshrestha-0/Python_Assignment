"""
Write a Python program to unpack a tuple in several variables.
"""


def unpackTuple(input_tuple):
    for tuple_variable in range(len(input_tuple)):
        print(input_tuple[tuple_variable])


input_tuple = ('physics', 'chemistry', 1997, 2000)
print(unpackTuple(input_tuple))
