"""
Count total vowels in an array of strings
"""

def count_vowels(s: str) -> int:

    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count +=1
    return count

print(count_vowels("apple"))


"""
Find strings that contain at least one vowel
"""

def contains_vowel(s: str) -> bool:
    pass