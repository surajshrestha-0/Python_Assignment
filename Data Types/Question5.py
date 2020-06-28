"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
"""


def addString(input_string):
    # checking the length of the string
    if len(input_string) > 2:
        # checking the last 3 letters
        if input_string[-3:] == 'ing':
            # print('ing')
            # adding 'ly' if last 3 letters is equal 'ing'
            input_string += 'ly'
        else:
            # print('ly')
            # adding 'ing' if last 3 letters is not 'ing'
            input_string += 'ing'
    return input_string


print(addString('abc'))
print(addString('string'))