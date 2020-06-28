"""
Write a Python program to find intersection of two given arrays using Lambda.
"""

number_array1 = list(range(1, 20))
number_array2 = list(range(1, 10))

intersection = list(filter(lambda x: x in number_array1, number_array2))

print("Given arrays: \n {} \n {}".format(number_array1, number_array2))
print("\nIntersection of the given arrays: ", intersection)
