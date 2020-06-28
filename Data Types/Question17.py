"""
Write a Python program to multiplies all the items in a list.
"""


def multiplyListItem(input_list):
    total = 1
    for i in range(0, len(input_list)):
        total = total * input_list[i]
    return 'Multiplication of all items in the list : %s' % total


print(multiplyListItem([1, 2, 4, 5]))
