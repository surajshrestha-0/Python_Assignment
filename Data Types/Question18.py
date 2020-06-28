"""
Write a Python program to get the largest number from a list.
"""


def largestNumber(input_list):
    largest_number = max(input_list)
    return 'Largest number in the given list : %s' % largest_number


print(largestNumber([27, 192, 168, 1, 404]))
