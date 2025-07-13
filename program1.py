"""
    Given a string of 'A' and 'B', delete the minimum number of chars
    so that no two adjacent chars in the result are equal.
    Returns a tuple (num_deletions, alternating_string).
"""

def del_matching(s: str) -> (int, str):
    if not s:
        return 0, ""
    
    result = [s[0]]
    deletions = 0

    for c in s[1:]:
        if c == result[-1]:
            deletions += 1
        else:
            result.append(c)
    
    return deletions, "".join(result)



if __name__ == "__main__":

    print(del_matching("AABBBAA"))

