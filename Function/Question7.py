"""
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""


def countUpperLower(input_string):
    upper_count = 0
    lower_count = 0
    for letter in input_string:
        if letter.islower():
            lower_count += 1
        elif letter.isupper():
            upper_count += 1
    return 'No of Upper case character: {} \nNo of Lower case character: {}'.format(upper_count, lower_count)


print(countUpperLower('The quick Brow Fox'))
