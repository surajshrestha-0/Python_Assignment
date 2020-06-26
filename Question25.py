"""
Write a Python program to check whether all dictionaries in a list are empty or not.
"""


def emptyDictionaryEmpty(list_dict):
    for i in list_dict:
        if not any(i):
            return True
        else:
            return False


print(emptyDictionaryEmpty([{}, {}, {}]))
print(emptyDictionaryEmpty([{1, 2}, {}, {}]))
