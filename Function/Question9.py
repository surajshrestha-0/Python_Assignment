"""
Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that
has no positive divisors other than 1 and itself.
"""


def checkPrime(input_number):
    if input_number == 1:
        return '%s is not a Prime Number' % input_number
    elif input_number == 2:
        return '%s is a Prime Number' % input_number
    else:
        for x in range(2, input_number):
            if input_number % x == 0:
                return '%s is not a Prime Number' % input_number
        return '%s is Prime Number' % input_number


print(checkPrime(4))
print(checkPrime(9))
print(checkPrime(3))
print(checkPrime(7))
