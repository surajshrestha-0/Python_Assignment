"""
Write a Python program to create Fibonacci series upto n using Lambda.
"""

from functools import reduce

fibonacciSeries = lambda n: reduce(lambda n, _: n + [n[-1] + n[-2]], range(n - 2), [0, 1])

print(fibonacciSeries(9))
