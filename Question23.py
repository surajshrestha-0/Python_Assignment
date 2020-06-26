"""
Write a Python program to check a list is empty or not.
"""


def checkEmptyList(input_list):
    if len(input_list) == 0:
        return 'List is Empty'


print(checkEmptyList([]))
