"""
Considering only three types of edits:.
- insert a character
- remove a character
- replace a character

Given two strings, write a function to determine if they are one edit (or zero edits) away.
"""


def levenshtein_distance(s1: str, s2: str) -> bool:
    # Replace
    if len(s1)-len(s2) == 0:
        check = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if check:
                    return False
                else:
                    check = True
        return True

    # Add
    elif len(s1)-len(s2) == 1:
        check = 0
        for i in range(len(s2)):
            if s1[i+check] != s2[i]:
                if check == 1:
                    return False
                elif check == 0 and s1[i+1] == s2[i]:
                    check += 1
        return True

    # Remove
    elif len(s1)-len(s2) == -1:
        check = 0
        for i in range(len(s1)):
            if s1[i] != s2[i+check]:
                if check == 1:
                    return False
                elif check == 0 and s1[i] == s2[i+1]:
                    check += 1
        return True

    else:
        return False

"""
The time complexity is O(N), where N is the length of the shortest string.
The space complexity is O(1), since only the check and loops variables are used.
"""
