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
    vowels = "aeiouAEIOU"

    for char in s:
        if char in vowels:
            return True
    return False

words = ["apple", "banana", "Orange", "sky"]
vowel_words = [word for word in words if contains_vowel(word)]
print(vowel_words)

"""
Replace vowels in strings with *
"""

def replace_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""

    for char in s:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result

words = ["apple", "banana", "Orange", "sky"]
replaced_words = [replace_vowels(word) for word in words]
print(replaced_words)


"""
Count number of vowels in each string
"""

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("apple"))

"""
 Find the string with the maximum number of vowels
"""

def max_vowels(words: list) -> str:
    max_count = 0
    max_word = ""
    for word in words:
        count = count_vowels(word)
        if count > max_count:
            max_count = count
            max_word = word
    return max_word

print(max_vowels(["apple", "banana", "Orange", "sky"]))

