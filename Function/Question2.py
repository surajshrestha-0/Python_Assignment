"""
Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""


def sumList(input_list):
    total = 0
    for x in input_list:
        total += x
    return total


print(sumList([8, 2, 3, 0, 7]))
