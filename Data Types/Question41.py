"""
Write a Python program to convert a tuple to a string.
"""


def convertTuple(input_tuple):
    converted_string = ''.join(input_tuple)
    return converted_string


tuple_hello = ('H', 'E', 'L', 'L', 'O')
print(convertTuple(tuple_hello))
