"""
Ali joined a social networking site to stay in touch with his friends. The signup
page required him to input a name and a password. However, the password must be
strong. The website considers a password to be strong if it satisfies the following
criteria:

a. Its length is at least 15 characters and maximum 30 characters.
b. It contains at least one digit
C. It contains at least one lowercase English character.
d. It contains at least one uppercase English character.
e. It contains at least one special character.
f. Take password as input from user and checks if it satisfies above conditions.
"""

import re

def is_strong_password(password: str) -> bool:
    if not (15 <= len(password) <= 30):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[^A-Za-z0-9]', password):
        return False
    return True

if __name__ == "__main__":
    #  password = input("Enter your password: ")
    #  if is_strong_password(password):
    #      print("Strong password")
    #  else:
    #      print("Weak password")

    # Sample test cases and expected results
    # Each tuple contains (test_password, expected_result)
    test_examples = [
        # Too short (length < 15)
        ("Ab1!shortPwd", False),
        # No digit
        ("PasswordWithoutDigit!", False),
        # No lowercase letter
        ("PASSWORD12345!@#", False),
        # No uppercase letter
        ("password12345!@#", False),
        # No special character
        ("Passw0rdWithNoSpecials", False),
        # Valid strong password (meets all criteria)
        ("Str0ngPassword!2025", True),
        # Edge case: exactly 15 characters, all criteria met
        ("A1b2C3d4E5f6!gH", True),
        # Edge case: exactly 30 characters, all criteria met
        ("Aa1!" * 7 + "Bb2@", True),
        # Too long (length > 30)
        ("A1b2C3d4E5f6!gH" * 3, False),
    ]

    # Run sample tests and print results
    print("\nRunning sample test cases:")
    for pwd, expected in test_examples:
        result = is_strong_password(pwd)
        print(f"Password: {pwd!r:30} | Expected: {expected} | Got: {result}")