"""
Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
"""


def swap(x, y):
    a = y[:2] + x[2:]
    b = x[:2] + y[2:]
    return a + ' ' + b


print(swap('abc', 'xyz'))
