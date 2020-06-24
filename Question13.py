"""
Write a Python program that accepts a comma separated sequence
of words as input and prints the unique words in sorted form (alphanumerically).
"""


def sortWords(user_input):
    word_split = user_input.split(',')
    word_sorted = sorted(list(word_split))
    word_out = ','.join(word_sorted)
    return word_out


print(sortWords('red, white, black, red, green, black'))