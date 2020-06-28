"""
Write a Python program to iterate over dictionaries using for loops.
"""


def itrateDict(input_dict):
    for key, value in input_dict.items():
        print('{}:{}'.format(key, value))


number_dict = {'one': 1, 'two': 2, 'three': 3}
itrateDict(number_dict)
