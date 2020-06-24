"""
Write a Python program to remove the characters which have odd index values of a given string.
"""


def removeOddIndex(input_string):
    output_string = ''

    for i in range(len(input_string)):
        if i % 2 == 0:
            output_string = output_string + input_string[i]
    return output_string


print(removeOddIndex("Python"))