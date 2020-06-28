"""
Write a Python program to remove the nth index character from a nonempty string.
"""


# input arguments - nonempty string, nth index
def removeChar(input_string, a):
    previous_string = input_string[:a]
    after_string = input_string[a + 1:]
    return previous_string + after_string


input_string = 'Hello'
print(removeChar(input_string, 3))
