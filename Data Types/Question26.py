"""
Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
"""


def addString(input_list, input_string):
    num_str = []
    for item in input_list:
        item = input_string + str(item)
        num_str.append(item)
    return num_str


print(addString([1, 2, 3, 4], 'emp'))
