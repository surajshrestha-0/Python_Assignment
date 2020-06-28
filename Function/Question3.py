"""
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""


def multiplyNumbers(input_list):
    result = 1
    for x in input_list:
        result *= x
    return result


print(multiplyNumbers([1, 2, 3, 4]))
