"""
Write a Python program to count the occurrences of each word in a given sentence.
"""


def wordFrequency(input_string):
    # Initiating empty Dictionary
    input_word = input_string.split(' ')
    dict = {}

    for n in input_word:
        keys = dict.keys()
        # if key exists increase by 1
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


print(wordFrequency('Write a Python program to count the occurrences of each word in a given sentence.'))
