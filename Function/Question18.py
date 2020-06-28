"""
Write a Python program to check whether a given string is number or not using Lambda.
"""

checkNumber = lambda input_string: input_string.isnumeric()

input_string = input('Please enter string to check: ')
print(checkNumber(input_string))

