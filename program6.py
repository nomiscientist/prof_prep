"""
Mehtab and Balaj earn points in their steps to save the ship from pirates. Farrukh is
calculating the points. Let's denote Mehtab points by M and Balaj by B. Farrukh is
wondering how many positive integers are there that are divisors (common divisor)
to both numbers, M and B. Help him find the answer

"""

import math

def count_common_divisor(m: int, b:int) -> int:

    gcd_value = math.gcd(m,b)

