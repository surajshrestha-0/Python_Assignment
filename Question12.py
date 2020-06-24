"""
Write a Python script that takes input from the user and displays that input back in upper and lower cases.
"""


def upperLower(user_input):
    up_word = user_input.upper()
    low_word = user_input.lower()
    return up_word + "\n"+low_word


a = input("Enter a string: ")
print(upperLower(a))
