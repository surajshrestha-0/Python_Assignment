"""
Write a Python script to merge two Python dictionaries.
"""


def mergeDict(dict_1, dict_2):
    dict_1.update(dict_2)
    return dict_1


num1_dict = {'one': 1, 'two': 2, 'three': 3}
num2_dict = {'four': 4, 'five': 5, 'six': 6}
print(mergeDict(num1_dict, num2_dict))
