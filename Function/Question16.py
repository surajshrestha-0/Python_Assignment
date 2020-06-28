"""
Write a Python program to square and cube every number in a given list of integers using Lambda.
"""

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_numbers = list(map(lambda x: x ** 2, numbers_list))
cube_numbers = list(map(lambda x: x ** 3, numbers_list))
print('Given List: %s' % numbers_list)
print('Square numbers: %s' % square_numbers)
print('Cube numbers: %s' % cube_numbers)
