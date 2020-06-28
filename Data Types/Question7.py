""""
Write a Python function that takes a list of words and returns the length of the longest one.
"""


def longestOne(input_list):
    check_len = []
    for i in input_list:
        check_len.append((len(i), i))
        check_len.sort()
    return check_len[-1][1]


word_list = ['Earth', 'Universe', 'Galaxy']
print(longestOne(word_list))
