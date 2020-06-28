"""
Write a Python program to filter a list of integers using Lambda.
"""

numbers_list = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers_list))
print('Given List: %s' % numbers_list)
print('even numbers: %s' % even_numbers)
print('Odd numbers: %s' % odd_numbers)



