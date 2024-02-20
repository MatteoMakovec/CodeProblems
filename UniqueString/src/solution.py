"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique(s: str) -> bool:
    if len(s) == 0:
        return False

    str_dict = dict()
    for c in s:
        if c in str_dict:
            return False
        else:
            str_dict[c] = 1

    return True


"""
The solution proposed is the BCR, since we have a time complexity of O(n), where n is the length of the string.
The complexity is given since we have to go through a new character of the string at every iteration of the for loop.
Obviously, if we encounter a repetitive character before reaching the end of the string, we don't go through the entire
length of the string.
At every iteration of the for loop we have to check if the character is present in the string. String we used a
dictionary, the lookup costs O(1) and thus it does not affect asymptotically the time complexity of the algorithm.
"""
