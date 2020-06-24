"""
Write a python program to count the number of characters (character frequency) in a string.
"""


def charFrequency(input_string):
    # Initiating empty Dictionary
    dict = {}

    for n in input_string:
        keys = dict.keys()
        # if key exists increase by 1
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


print(charFrequency('google.com'))
