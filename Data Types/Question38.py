"""
Write a Python program to remove a key from a dictionary.
"""


def removeKey(input_dict, key):
    if key in input_dict:
        input_dict.pop(key)
        print(input_dict)


dict_one = {'one': 1, 'two': 2, 'three': 3}
removeKey(dict_one, 'one')
