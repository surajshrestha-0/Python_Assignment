"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""


def uniqueList(input_list):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


print(uniqueList([1, 2, 3, 3, 3, 3, 4, 5]))
