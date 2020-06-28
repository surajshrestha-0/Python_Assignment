"""
write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return empty string.
"""


def firstLastChar(user_input):
    if len(user_input) < 2:
        # return empty string
        return ''

    # return concatenation of first two and last two chars of the given string
    return user_input[0:2] + user_input[-2:]


print(firstLastChar('Python'))
print(firstLastChar('Py'))
print(firstLastChar('w'))
