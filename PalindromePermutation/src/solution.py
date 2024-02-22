"""
Given a string, write a function that check if it is a permutation of a palindrome. The palindrome does not need to be
limited to just dictionary words. Casing and non-letter characters can be ignored.
"""


def build_frequency(s: str) -> dict:
    res_dict = dict()
    for char in s:
        if not char.isnumeric():
            if char.lower() not in res_dict:
                res_dict[char.lower()] = 1
            else:
                res_dict[char.lower()] += 1

    return res_dict


def check_frequencies(freq: dict) -> bool:
    check = False
    for val in freq.values():
        if val % 2 == 1:
            if check:
                return False
            else:
                check = True

    return True


def has_palindrome_permutation(string: str) -> bool:
    if len(string) == 0:
        return False

    frequencies = build_frequency(string)

    return check_frequencies(frequencies)


"""
The solution is based on a mathematical consideration: a string to be palindrome can have at most one character with
an odd cardinality (which will be placed in the middle).
The algorithm therefore, instead going through the creation of every possible permutation of a string, goes just 
through this simple requisite.

The function "build_frequency" has a for loop that goes from 0 to len(string). The time complexity is therefore O(N),
where N is the length of the string.
The function "check_frequencies" goes through every character in the dictionary and checks the cardinality. In the worst
case, this loop iterates 26 times. The time complexity is therefore O(1).
The overall complexity of the algorithm is therefore O(N), which is the BCR.
"""
