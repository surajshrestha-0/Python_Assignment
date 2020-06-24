"""
Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
"""


def changeLastFirst(input_string):
    start_string = input_string[0]
    end_string = input_string[-1]
    unchanged_string = input_string[1:-1]
    return end_string + unchanged_string + start_string


print(changeLastFirst('Python'))