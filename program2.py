"""
Given N Numbers, calculate sum of their factorial modulo 107
"""


import math

def factorial_sum_modulo(numbers, modulo=108):
    total = 0
    for number in numbers:
        total += math.factorial(number)
    return total % modulo

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = factorial_sum_modulo(numbers)
print(f"Sum of factorials modulo 108: {result}")

