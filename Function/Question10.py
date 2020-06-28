"""
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""


def evenList(input_list):
    initial_num = 0
    while initial_num < len(input_list):
        if initial_num % 2 != 0:
            print(input_list[initial_num], end=" ")
        initial_num += 1


evenList([1, 2, 3, 4, 5, 6, 7, 8, 9])
