"""
Mehtab and Balaj earn points in their steps to save the ship from pirates. Farrukh is
calculating the points. Let's denote Mehtab points by M and Balaj by B. Farrukh is
wondering how many positive integers are there that are divisors (common divisor)
to both numbers, M and B. Help him find the answer

"""

import math

def count_common_divisors(m: int, b:int) -> int:
    g = math.gcd(m,b)
    count = 0

    for i in range(1, int(g**0.5) + 1):
        if g % i == 0:
            count += 1
            if i != g // i:
                count += 1
    return count

# Example usage:
M = 12  # Mehtab's points
B = 18  # Balaj's points
result = count_common_divisors(M, B)
print(f"Number of common divisors for M={M}, B={B}: {result}")

