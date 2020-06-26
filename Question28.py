"""
Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""


def addToDictinary(input_dict, key, value):
    input_dict[key] = value
    return input_dict


print(addToDictinary({0: 10, 1: 20}, 2, 30))