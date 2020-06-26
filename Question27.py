"""
Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
"""


def replaceListItem(list1, list2):
    list1.pop(-1)
    list1 += list2[:]
    return list1


print(replaceListItem([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
