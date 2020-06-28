"""
Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
"""


def calculateFactorial(input_number):
    factorial = 1
    if input_number < 0:
        print("Sorry, factorial does not exist for negative numbers")

    elif input_number == 0:
        print("The factorial of 0 is 1")

    else:
        for i in range(1, input_number + 1):
            factorial = factorial * i
        print("The factorial of", input_number, "is", factorial)


calculateFactorial(5)
