"""
Given a string of lowercase letters in the range [a-z] find the index of a character
that can be removed to make the string a palindrome. If the word is already a
palindrome or there is no solution return -1
"""

def palindrome_index(s: str) -> int:
   left, right = 0, len(s) - 1

   while left < right:
      if s[left] != s[right]:
         left += 1
         right -= 1
      else:
         if is_palindrome_range(s, left + 1, right):
            return left
         if is_palindrome_range(s, left, right - 1):
            return right
      return -1
   return -1

def is_palindrome_range(s: str, i:int, j:int) -> bool:
   while i < j:
      if s[i] != s[j]:
         return False
      
      i += 1
      j -= 1

   return True


if __name__ == "__main__":
    # Test cases
    print(palindrome_index("aaab")) 
    print(palindrome_index("baa"))  
    print(palindrome_index("eyee"))
