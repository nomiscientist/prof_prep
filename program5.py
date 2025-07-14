"""
Calculate the sum of all of the palindrome numbers from 0 to 100
"""

def is_palindrome(num: int) -> bool:
    s = str(num)
    return s == s[::-1]    

def sum_palindromes(limit: int) -> int:
    total = 0
    for i in range(limit + 1):
        if is_palindrome(i):
            total += i
    return total

if __name__ == "__main__":
    print("sum of palindromes from 0 to 100:", sum_palindromes(100))