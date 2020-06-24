"""
Write a Python program to sum all the items in a list.
"""


def sumListItem(input_list):
    total = 0
    for i in range(0, len(input_list)):
        total = total + input_list[i]
    return 'Sum of all items in the list : %s' % total


print(sumListItem([1, 2, 3, 4, 5]))
