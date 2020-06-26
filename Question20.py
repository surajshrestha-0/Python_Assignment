"""
Write a Python program to count the number of strings where the string length is 2
or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""


def checkLastCharacter(input_string):
    counter = 0
    for i in input_string:
        if len(i) > 1 and i[0] == i[-1]:
            counter += 1
    return counter


print(checkLastCharacter(['abc', 'xyz', 'aba', '1221']))
