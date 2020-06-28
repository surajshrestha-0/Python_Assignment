"""
Write a python program to get a string from a given string where all occurrences of its first char
have been changed to $, except the first char itself
"""


def replace(user_input):
    char = user_input[0]  # first char
    user_input = user_input.replace(char, '$')  # replaced all char with $
    user_input = char + user_input[1:]  # segregated first char and replaced by z
    return user_input


print(replace('restart'))
print(replace('arrange'))
