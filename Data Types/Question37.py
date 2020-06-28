"""
Write a Python program to multiply all the items in a dictionary.
"""

def multiplyDict(input_dict):
    total = 1
    for k in input_dict:
        total = total * input_dict[k]
    return total


multiply_dict = {'value1': 10, 'value2': 20, 'value3': 30}
print(multiplyDict(multiply_dict))