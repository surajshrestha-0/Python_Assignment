"""
Write a Python program to get the smallest number from a list.
"""


def smallestNumber(input_list):
    smallest_number = sorted(input_list)[0]
    return 'Smallest number in the given list : %s' % smallest_number


print(smallestNumber([27, 192, 168, 1, 404]))
