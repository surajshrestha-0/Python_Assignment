"""
Write a Python program to sum all the items in a dictionary.
"""


def sumDict(input_dict):
    return sum(input_dict.values())


sum_dict = {'value1': 10, 'value2': 20, 'value3': 30}
print(sumDict(sum_dict))
