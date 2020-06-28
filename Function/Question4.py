"""
Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""


def reverse(input_string):
    out_string = input_string[::-1]
    return out_string


print(reverse("1234abcd"))
