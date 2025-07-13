"""
Given a string of lowercase letters in the range [a-z] find the index of a character
that can be removed to make the string a palindrome. If the word is already a
palindrome or there is no solution return -1
"""

def palindrome_index(s: str) -> int:
    # Check if string is already a palindrome
    if s == s[::-1]:
        return -1
    
    # Iterate through string checking corresponding characters from start and end
    for i in range(len(s)):
        if s[i] != s[-(i+1)]:
            # Check if removing character at index i makes it a palindrome
            if s[i+1] == s[-(i+2)]:
                return i
            else:
                return len(s) - 1 - i
    return -1

if __name__ == "__main__":
    # Test cases
    print(palindrome_index("aaab"))  # Should print 3
    print(palindrome_index("baa"))   # Should print 0
    print(palindrome_index("eyee"))  # Should print 0
