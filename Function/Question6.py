"""
Write a Python function to check whether a number is in a given range.
"""


def checkRange(range_start, range_end, check_number):
    if range_start <= check_number <= range_end:
        print('The number {} is in range ({}, {})'.format(check_number, range_start, range_end))
    else:
        print('The number {} is not in range ({}, {})'.format(check_number, range_start, range_end))


# input range
a = int(input("Enter start: "))
b = int(input("Enter end: "))
# given number
c = int(input("Enter number: "))
checkRange(a, b, c)
