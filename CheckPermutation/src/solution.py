"""
Given two strings, write a method to decide if one is a permutation of the other.
"""


def is_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s1_dict = dict()
    for c in s1:
        if c not in s1_dict:
            s1_dict[c] = 1
        else:
            s1_dict[c] += 1

    for c in s2:
        if c not in s1_dict:
            return False
        else:
            s1_dict[c] -= 1
            if s1_dict[c] < 0:
                return False

    return True


"""
The first if statement is O(1).
The two for cycles have O(N) both, were N is the size of s1 (or s2).
The first cycle would go through each character of s1, adding it to a dictionary (keeping track of the cardinality).
The second, goes through the characters of s2 and would keep track of the cardinalities by subtracting one unit each
time from the dictionary.
At the end, we want to have a dictionary with all elements with a cardinality of 0, if not then the two strings are not
permutations of the same set of strings.

The overall time complexity therefore is O(1)+O(N)+O(N) ~= O(2*N) ~= O(N).
This is already an optimal solution for checking if two strings are permutations of each other, as you need to examine 
each character in both strings at least once.
Regarding the space complexity, we would have done better using arrays instead of a dictionary, but I find this solution
more elegant.
"""
