"""
Write a Python script to check whether a given key already exists in a dictionary.
"""


def checkKey(input_dict, input_key):
    if bool(input_dict.get(input_key)):
        return 'key Exists !'
    else:
        return 'Key does not exists'


dict = {'one': 1, 'two': 2}
print(checkKey(dict, 'three'))
