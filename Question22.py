"""
Write a Python program to remove duplicates from a list.
"""


def removeDuplicate(input_list):
    return list(set(input_list))


print(removeDuplicate([12, 12, 13, 14, 14, 6, 7, 8]))
